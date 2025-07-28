<script>
    import classes from "$lib/classes.json";
    import ClassLine from "./ClassLine.svelte";
    import { setContext } from "svelte";

    let {
        adept,
        mugshots=[]
    } = $props()

    // set context
    setContext("adept", adept)
</script>

<div 
    class=adept-type 
    id="{adept}-adept"
    class:venus={adept === "venus"}
    class:mars={adept === "mars"}
    class:jupiter={adept === "jupiter"}
    class:mercury={adept === "mercury"}
>
    <h1>
        {adept[0].toUpperCase() + adept.slice(1)} Adepts
        {#each mugshots as mugshot}
        <img src="assets/{mugshot}-mugshot.png" alt="{mugshot}" />
        {/each}
    </h1>
    {#each Object.keys(classes[adept]) as line}
        <ClassLine
            line={line}
        ></ClassLine>
    {/each}
    <img src="assets/{adept}-djinn.png" alt="{adept} djinn" class=djinn-img />
</div>

<style>
    .adept-type {
        position: relative;
        padding: 4rem;
        margin: 2rem auto;
        display: grid;
        grid-template-columns: min-content min-content min-content;
        gap: 1rem;
        border-radius: .5rem;
        box-shadow: 
            inset 0 0 1rem rgba(0, 0, 0, 0.25),
            .1rem .1rem .5rem rgba(0, 0, 0, 0.25)
        ;
        break-after: page;
    }
    @media print {
        .adept-type {
            box-shadow: none;
            grid-template-columns: min-content min-content;
        }
        .djinn-img {
            display: none;
        }
    }
    .adept-type.venus {
        background: 
            linear-gradient(
                135deg, rgba(200, 120, 6, 0.25), transparent
            ), url("/assets/parchment-background.avif");
        
    }
    .adept-type.mars {
        background: linear-gradient(
            135deg, rgba(255, 100, 40, 0.25), transparent
        ), url("/assets/parchment-background.avif");
    }
    .adept-type.jupiter {
        background: linear-gradient(
            135deg, rgba(120, 50, 200, 0.25), transparent 
        ), url("/assets/parchment-background.avif");
    }
    .adept-type.mercury {
        background: linear-gradient(
            135deg, rgba(80, 220, 255, 0.25), transparent 
        ), url("/assets/parchment-background.avif");
    }

    .adept-type h1 {
        grid-column-end: span 3;
        font-size: 3rem;
        margin-bottom: 1rem;
    }

    .djinn-img {
        position: absolute;
        pointer-events: none;
        bottom: 1rem;
        right: 1rem;
        z-index: 0;
    }
</style>