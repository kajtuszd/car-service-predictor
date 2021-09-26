<template>
    <nav class="navbar is-dark">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item">
                <strong>
                    Car Service Predictor
                </strong>
            </router-link>
        </div>

        <div class="navbar-menu">
            <div class="navbar-end">
                <div class="navbar-item">

                    <div class="buttons" v-if="this.$store.state.isAuthenticated">
                        <button @click="logOut" class="button is-warning is-outlined">
                            <strong>Log out</strong>
                        </button>
                    </div>

                    <div class="buttons" v-else>
                        <router-link to="/sign-up" class="button is-success is-outlined">
                            <strong>Sign up</strong>
                        </router-link>

                        <router-link to="/log-in" class="button is-light is-outlined">
                            <strong>Log in</strong>
                        </router-link>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
    import axios from 'axios'
    import {toast} from 'bulma-toast'

    export default {
        name: 'Navbar',
        methods: {
            async logOut() {
                await axios
                    .post('/auth/token/logout/')
                    .then(response => {
                        toast(
                            {
                                message: 'Successfully logged out.',
                                type: 'is-success',
                                dismissible: true,
                                pauseOnHover: true,
                                position: 'top-center',
                                animate: { in: 'fadeIn', out: 'fadeOut' },
                            }
                        )
                    })
                    .catch(error => {
                        toast(
                            {
                                message: 'An error occurred.',
                                type: 'is-danger',
                                dismissible: true,
                                pauseOnHover: true,
                                position: 'top-center',
                                animate: { in: 'fadeIn', out: 'fadeOut' },
                            }
                        )
                    })

                axios.defaults.headers.common['Authorization'] = ''
                localStorage.removeItem('authToken')
                this.$store.commit('cleanAuthToken')
                this.$router.push('/')
            }
        }
    }
</script>

<style>
.button {
    transition: 0.5s;
}
</style>
