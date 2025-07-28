<script>
    import { slide } from "svelte/transition";
    let {
        name,
        spec
    } = $props()

    let hovered = $state(false)
</script>

<div 
    class=psynergy
    onmouseenter={(evt) => hovered = true}
    onmouseleave={(evt) => hovered = false}
    role=none
>
    <img src="/assets/psynergy/{name}.png" alt={name} class=psynergy-icon />
    {#if hovered}
        <div class=psynergy-card transition:slide>
            <h4>{name} (level {spec.level})</h4>
            <p>{spec.description}</p>
        </div>
    {/if}
</div>

<style>
    .psynergy-icon {
        width: 6mm;
        height: 6mm;
    }
    .psynergy-card {
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