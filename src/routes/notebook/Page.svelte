<script>
    import classes from "$lib/classes.json";
    import { getContext, onMount, setContext } from "svelte";

    let {
        adept,
        mugshots=[],
        children
    } = $props()

    // set context
    setContext("adept", adept)
    // get context
    let siblings = getContext("siblings")

    onMount(() => {
        if (siblings.current === undefined) {
            siblings.current = adept;
        }
        siblings.all.push(adept)
    })
</script>


<button
    class="uibox notebook-tab"
    class:current={siblings.current === adept}
    onclick={() => siblings.current = adept}
>
    <h3>{adept[0].toUpperCase() + adept.slice(1)} adept</h3>
    {#each mugshots as mugshot}
        <img src="assets/{mugshot}-mugshot.png" alt="{mugshot}" />
    {/each}
</button>
{#if siblings.current === adept}
    <div 
        class="notebook-page"
        id="{adept}-adept"
        style:border-color="var(--{adept})"
        style:grid-column-end="span {siblings.all.length + 2}"
    >
        {@render children()}
    </div>
{/if}

<style>
    .notebook-tab {
        color: var(--text);
        display: flex;
        flex-direction: row;
        gap: .5rem;
        align-items: center;
        grid-row-start: tabs;
    }
    .notebook-tab.current {
        border-color: var(--hltext);
    }
    .notebook-page {
        position: relative;
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
        gap: 1rem;
        break-after: page;
        grid-row-start: pages;
    }
</style>