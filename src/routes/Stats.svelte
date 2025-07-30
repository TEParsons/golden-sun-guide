<script>
    import { Tooltip } from "$lib/tooltip";

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
            style:background-color="var(--{attr})"
        ></div>
    {/each}
    <Tooltip bind:hovered={hovered}>
        {#each Object.keys(spec) as attr}
        <b style:color="var(--{attr})">{attr}:</b> {spec[attr]}<br>
        {/each}
    </Tooltip>
</div>

<style>
    .stats {
        position: relative;
        grid-column-end: span 2;
        margin: .5rem 0;
    }
    .stat-bar {
        height: .4rem;
        border: 1px solid rgba(0, 0, 0, 0.5);
    }
    .PP {
        margin-bottom: .5rem;
    }
</style>