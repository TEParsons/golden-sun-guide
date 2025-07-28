<script>
    import classes from "$lib/classes.json";
    import Psynergy from "./Psynergy.svelte";
    import { getContext } from "svelte";
    import Stats from "./Stats.svelte";

    let {
        cls=undefined
    } = $props();

    // get context
    let adept = getContext("adept")
    let line = getContext("line")

    let spec = classes[adept][line][cls];
</script>

<div class="class {adept} {line}">
    <h3>{cls}</h3>
    <div class="djinn-requirements">
        {#each ["venus", "mars", "jupiter", "mercury"] as emt}
            {#if spec.djinn[emt]}
                {#each [...Array(spec.djinn[emt]).keys()] as _}
                    <img src="assets/{emt}-energy.png" alt="{emt}-energy" class=energy />
                {/each}
            {/if}
        {/each}
    </div>
    <Stats
        spec={spec.stats}
    ></Stats>
    <div class=psynergies>
        {#each Object.keys(spec.psynergy) as psynergy}
            <Psynergy
                name={psynergy}
                spec={spec.psynergy[psynergy]}
            ></Psynergy>
        {/each}
    </div>
</div>

<style>
    .class {
        display: grid;
        grid-template-columns: auto min-content;
        padding: .5rem;
        width: 20rem;
    }
    .djinn-requirements, .psynergies {
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 1mm;
    }
    .psynergies {
        position: relative;
        flex-wrap: wrap;
        grid-column-end: span 2;
    }
    .energy {
        height: 3mm;
        width: 3mm;
    }
    
</style>