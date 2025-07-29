<script>
    import classes from "$lib/classes.json";
    import ClassSummary from "./ClassSummary.svelte";
    import { getContext, setContext } from "svelte";

    let {
        line
    } = $props()

    // get context
    let adept = getContext("adept")
    // set context
    setContext("line", line)
</script>


<div class="uibox class-line {adept} {line}">
    <h2>{line}</h2>
    {#each Object.keys(classes[adept][line]) as cls}
        <ClassSummary
            cls={cls}
        ></ClassSummary>
    {/each}
</div>

<style>
    .class-line {
        padding: 1rem;
        z-index: 0;
        break-inside: avoid-page;
    }
    .class-line:hover {
        z-index: 1;
    }
</style>