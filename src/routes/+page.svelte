<script>
    import classes from "$lib/classes.json";
    import ClassLine from "./ClassLine.svelte";
    import { Notebook, NotebookPage } from "./notebook";
</script>

<Notebook>
    {#each [...[
        ["venus", ["isaac", "felix"]],
        ["mars", ["garet", "jenna"]],
        ["jupiter", ["ivan", "sheba"]],
        ["mercury", ["mia", "piers"]]
    ]] as [adept, mugshots]}
        <NotebookPage
            adept={adept} 
            mugshots={mugshots}
        >
            {#each Object.keys(classes[adept]) as line}
                <ClassLine
                    line={line}
                ></ClassLine>
            {/each}
        </NotebookPage>
    {/each}
</Notebook>
