<template>
    <div>
        <Navbar />
        <div class="section">
            <router-view/>
        </div>
        <Footer />
    </div>
</template>

<script>
    import Navbar from './components/layout/Navbar.vue'
    import Footer from './components/layout/Footer.vue'

    export default {
        name: 'App',
        components: {
            Navbar,
            Footer
        }
    }
</script>


<style lang="scss">
@import '../node_modules/bulma';
</style>
