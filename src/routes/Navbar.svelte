<nav>
    {#each ["venus", "mars", "jupiter", "mercury"] as adept}
    <a 
        href="#{adept}-adept"
    >
        <img src="assets/{adept}-energy.png" alt="{adept}-energy" class=energy />
    </a>
    {/each}
</nav>

<style>
    nav {
        position: fixed;
        top: 1rem;
        left: 1rem;
        display: flex;
        flex-direction: column;
    }
    a:hover img {
        opacity: .8;
    }
    nav a img {
        width: 5mm;
    }

</style>