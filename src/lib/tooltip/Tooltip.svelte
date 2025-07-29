<script>
    import { slide } from "svelte/transition";

    let {
        hovered=$bindable(),
        children
    } = $props();
</script>

{#if hovered}
    <div class="uibox tooltip" transition:slide>
        {@render children()}
    </div>
{/if}

<style>
    .tooltip {
        pointer-events: none;
        padding: 1rem;
        position: absolute;
        min-width: 20rem;
        z-index: 1;
    }
</style>