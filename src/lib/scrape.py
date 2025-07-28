import requests
import xml.etree.ElementTree as xml
import re
import json
from pathlib import Path


download_icons = True


def table2dict(table):
    """
    Parse a single-row XML table into a dict.

    Parameters
    ----------
    table : xml.etree.ElementTree
        XML tree for a table to parse into a dict
    """
    # blank arrays for headings and values
    heads = []
    vals = []
    # iterate through rows
    for node in table:
        # store heading values in heads
        if node.tag == "thead":
            for cell in node[0]:
                heads.append(cell.text)
        # store body values in vals
        if node.tag == "tbody":
            for cell in node[0]:
                vals.append(cell.text)
    # create dict
    return dict(zip(heads, vals))


def download_psynergy_icon(name, url):
    """
    Download a psynergy icon from a url

    Parameters
    ----------
    name : str
        Name of the psynergy
    url : str
        URL to download from
    
    Returns
    -------
    bool
        True if completed without error
    """
    # if flag is set not to download icons, do nothing
    if not download_icons:
        return
    # fail if given an invalid url
    if not isinstance(url, str):
        return False
    try:
        # get image data from url
        img = requests.get(url).content
        # write to file
        with Path(f"static/assets/psynergy/{name}.png").open('wb') as f:
            f.write(img)
    except:
        return False
    else:
        return True


output = {
    'venus': {},
    'mars': {},
    'jupiter': {},
    'mercury': {}
}

# get homepage
resp = requests.get("https://www.goldensun-syndicate.net/gs/classes/")
# iterate through links on homepage

for link, name in re.findall(
    pattern=r"<dd><a href=\"([\w/]*)\">([\w\s]*)</a></dd>",
    string=str(resp.content)
):
    # skip NPC
    if name == "NPC":
        continue
    # get content of this page
    resp = requests.get("https://www.goldensun-syndicate.net" + link)
    # for each adept type...
    for adeptType, adept in (
        ("venus", "isaac"), 
        ("mars", "garet"), 
        ("jupiter", "ivan"), 
        ("mercury", "mia")
    ):
        try:
            # array to store class info in
            line = name
            prog = [name]
            cls = {}
            # get tables on this page
            for table in re.findall(
                pattern="<table.*?</table>",
                string=str(resp.content)
            ):
                # catch unclosed cols
                table = re.sub(
                    pattern=r"<col class=(\"\w*\") ?>",
                    string=table,
                    repl=r"<col class=\1 />"
                )
                # catch unclosed images
                table = re.sub(
                    pattern=r"<img src=(\"[\/:\.\-_\w\d]*?\") ?>",
                    string=table,
                    repl=r"<img src=\1 />"
                )
                # parse table as xml
                try:
                    tree = xml.fromstring(table)
                except xml.ParseError as err:
                    print(
                        err, "\n", 
                        table[err.position[1]-50:err.position[1]], "|||", table[err.position[1]:err.position[1]+50]
                    )
                    continue
                
                # is it names?
                if tree.get('summary') and "Names for" in tree.get('summary'):
                    # add names to class
                    cls['names'] = table2dict(tree)
                
                # is it progression?
                if tree.get('summary') and "Progression for" in tree.get('summary'):
                    prog = []
                    cls['djinn'] = {}
                    # iterate through table elements
                    for node in tree:
                        if node.tag == "thead":
                            djinnCol = None
                            for col, cell in enumerate(node[0]):
                                try:
                                    if cell[0].get("href") and adept in cell[0].get("href"):
                                        djinnCol = col
                                except IndexError:
                                    pass
                            assert djinnCol is not None
                        if node.tag == "tbody":
                            for row in node:
                                # store line progression order
                                prog.append(row[0][0].text)
                                # skip other classes in progression
                                if row[0][0].text != name:
                                    continue
                                # get djinn for this class
                                for djinnType in ("venus", "mars", "jupiter", "mercury"):
                                    for img in row[djinnCol]:
                                        if djinnType in img.get("src"):
                                            # add 1 to djinn type for each matching icon
                                            if djinnType not in cls['djinn']:
                                                cls['djinn'][djinnType] = 0
                                            cls['djinn'][djinnType] += 1
                            # get line name from last item
                            line = node[-1][0][0].text
                
                # is it psynergy?
                if tree.get('class') == "classPsynergyTable":
                    cls['psynergy'] = {}
                    for node in tree:
                        if node.tag == "tbody":
                            # iterate through table rows...
                            for row in node:
                                try:
                                    # get psynergy details
                                    psyName = row[0][2][0].text
                                    psy = {
                                        'level': row[0][0].text,
                                        'description': row[0][3].text
                                    }
                                    # try to download the icon
                                    download_psynergy_icon(
                                        name=psyName,
                                        url=row[0][1][0].get("src")
                                    )
                                    # is psynergy unique to a higher class?
                                    if row[0][4].text == "Class must be higher than ":
                                        target = row[0][4][0].text
                                        assert prog.index(target) <= prog.index(name)
                                    # does psynergy change name at a higher class?
                                    if row[0][4].text == "Transforms to ":
                                        target = row[0][4][1].text
                                        # if we meet that class, change the name
                                        if prog.index(target) <= prog.index(name):
                                            psyName = row[0][4][0][0].tail.strip()
                                            # also try to download the new icon
                                            download_psynergy_icon(
                                                name=psyName,
                                                url=row[0][4][0][0].get("src")
                                            )
                                except:
                                    continue
                                else:
                                    # store psynergy
                                    cls['psynergy'][psyName] = psy
                
                # is it stats?
                if tree.get('summary') and "Stat Boosts for" in tree.get('summary'):
                    cls['stats'] = table2dict(tree)
        
        except AssertionError:
            pass
        else:
            if len(cls['djinn']):
                # make sure line is in output
                if line not in output[adeptType]:
                    output[adeptType][line] = {}
                # add class to output
                output[adeptType][line][name] = cls

Path("classes.json").write_text(
    json.dumps(output, indent=True)
)

