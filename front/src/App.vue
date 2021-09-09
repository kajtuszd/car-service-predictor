<template>
    <div>
        <Navbar />
        <router-view/>
    </div>
</template>

<script>
    import Navbar from './components/layout/Navbar.vue'
    export default {
        name: 'App',
        components: {
            Navbar
        }
    }
</script>


<style lang="scss">
@import '../node_modules/bulma';
</style>
