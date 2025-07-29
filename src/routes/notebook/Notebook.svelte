<script>
    import { setContext } from "svelte";

    let {
        children
    } = $props()

    let pages = $state({
        current: undefined,
        all: []
    })
    setContext("siblings", pages)
</script>

<div 
    class=notebook
    style:grid-template-columns="auto repeat({pages.all.length}, min-content) auto"
>
    <div class=notebook-tab-filler></div>
    {@render children()}
    <div class=notebook-tab-filler></div>
</div>

<style>
    .notebook {
        display: grid;
        grid-template-rows: [tabs] max-content [pages] auto;
        gap: 1rem;
        justify-items: center;
        align-items: stretch;
        max-width: 1280px;
        margin: auto;
        padding: 2rem;
    }
    .notebook-tab-filler {
        grid-row-start: tabs;

    }
</style>