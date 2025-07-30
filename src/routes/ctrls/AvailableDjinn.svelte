<script>
    import { availableDjinn } from "../globals.svelte";
</script>

<div
    class="available-djinn-ctrl"
>
    <h2>Available Djinn</h2>
    {#each Object.keys(availableDjinn) as emt}
        <label for="available-{emt}">
            <img src="assets/{emt}-djinn.png" alt="{emt}-energy" class=energy />
            {emt}
        </label>
        <input id="available-{emt}" type=number bind:value={availableDjinn[emt]} max=18 min=0>
    {/each}
</div>

<style>
    h2 {
        grid-column-end: span 2;
    }
    .available-djinn-ctrl {
        display: grid;
        grid-template-columns: min-content min-content;
        gap: .5rem;
    }
    input[type=number] {
        background-color: transparent;
        border: none;
        outline: none;
        margin-left: .5rem;
    }
    label {
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: .5rem;
    }
</style>