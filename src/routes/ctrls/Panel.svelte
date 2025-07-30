<script>
    import { slide } from "svelte/transition";
    import AvailableDjinn from "./AvailableDjinn.svelte";
    import Level from "./Level.svelte";

    let expanded = $state(false)
</script>

<div
    class="uibox container"
>
    {#if expanded}
        <div 
            class="uibox controls"
            transition:slide={{axis: "y"}}
        >
            <AvailableDjinn></AvailableDjinn>
            <Level></Level>
        </div>
    {/if}
    <button
        onclick={(evt) => {expanded = !expanded}}
        aria-label="Toggle prefs"
    >
        {expanded ? "▲" : "☰"}
    </button>
</div>



<style>

    .container {
        grid-row-start: tabs;
        position: relative;
        align-items: start;
        transition: height 1s;
        width: min-content;
        z-index: 10;
        margin: auto;
        padding: .5rem;
    }
    .controls {
        position: absolute;
        top: calc(100% + 1rem);
        right: 0;
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }
    button {
        border: none;
        background-color: transparent;
        font-size: 1.5rem;
        padding: 0;
        width: 2rem;
        height: 2rem;
        line-height: 1em;
        padding-bottom: .2rem;
    }
</style>