<script>
    import classes from "$lib/classes.json";
    import Panel from "./ctrls/Panel.svelte";
    import ClassLine from "./ClassLine.svelte";
    import { Notebook, NotebookPage } from "./notebook";
</script>

<div class=page>
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
        <Panel></Panel>
    </Notebook>
</div>

<style>
    .page {
        position: relative;
    }
</style>
