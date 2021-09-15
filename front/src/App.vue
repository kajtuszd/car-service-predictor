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
    import axios from 'axios'

    export default {
        name: 'App',
        components: {
            Navbar,
            Footer,
        },
        beforeCreate() {
            this.$store.commit('startStore')
            if (this.$store.state.token) {
                let token = "Token " + this.$store.state.token
                axios.defaults.headers.common['Authorization'] = token
            } else {
                axios.defaults.headers.common['Authorization'] = ""
            }
        }
    }
</script>


<style lang="scss">
@import '../node_modules/bulma';
</style>
