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


<div class="class-line {adept} {line}">
    <h2>{line}</h2>
    {#each Object.keys(classes[adept][line]) as cls}
        <ClassSummary
            cls={cls}
        ></ClassSummary>
    {/each}
</div>

<style>
    .class-line {
        border: 1px solid rgba(255, 255, 255, 0.5);
        border-radius: .5rem;
        background-color: rgba(255, 255, 255, 0.25);
        padding: 1rem;
        z-index: 1;
        break-inside: avoid-page;
    }
</style>