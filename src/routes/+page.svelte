<script>
    import Adept from "./Adept.svelte";
    import Navbar from "./Navbar.svelte";
</script>

<div class=page>
    <Navbar></Navbar>
    <Adept 
        adept=venus 
        mugshots={["isaac", "felix"]}
    ></Adept>
    <Adept 
        adept=mars 
        mugshots={["garet", "jenna"]}
    ></Adept>
    <Adept 
        adept=jupiter 
        mugshots={["ivan", "sheba"]}
    ></Adept>
    <Adept 
        adept=mercury 
        mugshots={["mia", "piers"]}
    ></Adept>
</div>

<style>
    .page {
        display: flex;
        flex-direction: column;
    }
</style>