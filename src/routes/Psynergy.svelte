<script>
    import { Tooltip } from "$lib/tooltip";
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
    <img src="assets/psynergy/{name}.png" alt={name} class=psynergy-icon />
    <Tooltip bind:hovered={hovered}>
        <h4>{name} (level {spec.level})</h4>
        <p>{spec.description}</p>
    </Tooltip>
</div>

<style>
    .psynergy-icon {
        width: 6mm;
        height: 6mm;
    }
</style>