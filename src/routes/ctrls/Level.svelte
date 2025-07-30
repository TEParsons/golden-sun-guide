<script>
    import { level } from "../globals.svelte";
</script>

<div
    class="level-ctrl"
>
    <h2>Level</h2>
    <input type=number bind:value={level.value} max=100 min=0>
</div>

<style>
    h2 {
        grid-column-end: span 2;
    }
    .level-ctrl {
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