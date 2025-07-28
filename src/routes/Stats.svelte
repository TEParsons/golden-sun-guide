<script>
    import { slide } from "svelte/transition";
    let {
        spec
    } = $props()

    let hovered = $state(false)
</script>


<div 
    class=stats
    onmouseenter={(evt) => hovered = true}
    onmouseleave={(evt) => hovered = false}
    role=none
>
    {#each Object.keys(spec) as attr}
        <div 
            class="stat-bar {attr}"
            style:width="calc(({spec[attr]} - 80%) * 0.8)"
        ></div>
    {/each}
    {#if hovered}
    <div class=stats-card transition:slide>
        {#each Object.keys(spec) as attr}
        <b>{attr}:</b> {spec[attr]}<br>
        {/each}
    </div>
    {/if}
</div>

<style>
    .stats {
        position: relative;
        grid-column-end: span 2;
        margin: .5rem 0;
    }
    .stat-bar {
        height: .25rem;
    }

    .HP {
        background-color: red;
    }
    .PP {
        background-color: blue;
        margin-bottom: .25rem;
    }
    .ATK {
        background-color: orange;
    }
    .DEF {
        background-color: green;
    }
    .AGL {
        background-color: violet;
    }
    .LCK {
        background-color: gold
    }

    .stats-card {
        pointer-events: none;
        background-color: rgba(0, 0, 0, 0.75);
        border-radius: .5rem;
        padding: 1rem;
        color: white;
        position: absolute;
        min-width: 20rem;
        z-index: 1;
    }
</style>