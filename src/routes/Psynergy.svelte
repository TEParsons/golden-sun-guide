<script>
    import { Tooltip } from "$lib/tooltip";
    import { level } from "./globals.svelte";
    let {
        name,
        spec
    } = $props()

    let hovered = $state(false)
    let viable = $derived(level.value >= spec.level)
</script>

<div 
    class=psynergy
    onmouseenter={(evt) => hovered = true}
    onmouseleave={(evt) => hovered = false}
    role=none
>
    <img 
        src="assets/psynergy/{name}.png" 
        alt={name} 
        class=psynergy-icon 
        style:opacity={viable ? 1 : 0.2}
    />
    <Tooltip bind:hovered={hovered}>
        <h4>{name} <span style:color={viable ? "var(--text)" : "red"}>(level {spec.level})</span></h4>
        <p>{spec.description}</p>
    </Tooltip>
</div>

<style>
    .psynergy {
        transition: opacity .5s;
    }
    .psynergy-icon {
        width: 6mm;
        height: 6mm;
    }
</style>