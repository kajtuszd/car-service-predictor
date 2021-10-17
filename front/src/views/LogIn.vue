<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Log In</h1>

                <form @submit.prevent="logInForm">
                    <div class="field">
                        <label>Username</label>
                        <div class="control has-icons-left">
                            <input type="text" name="username" class="input" v-model="username">
                            <span class="icon is-small is-left">
                                <i class="fas fa-at"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control has-icons-left">
                            <input type="password" name="password" class="input" v-model="password">
                            <span class="icon is-small is-left">
                                <i class="fas fa-lock"></i>
                            </span>
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <button class="delete" v-on:click="cleanErrors"></button>
                        <p v-for="e in errors" :key="e">{{e}}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success is-outlined">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import {toast} from 'bulma-toast'

    export default {
        name: 'LogIn',
        methods: {
            async logInForm() {
                this.errors = []

                if (this.username === '') {
                    this.errors.push('Username is required.')
                }

                if (this.password === '') {
                    this.errors.push('Password is required.')
                }

                axios.defaults.headers.common['Authorization'] = ''
                localStorage.removeItem('authToken')

                if (!this.errors.length) {
                    const logInData = {
                        username: this.username,
                        password: this.password,
                    }

                    await axios
                        .post('auth/token/login/', logInData)
                        .then(response => {
                            const authToken = response.data.auth_token
                            this.$store.commit('setAuthToken', authToken, this.username)
                            axios.defaults.headers.common['Authorization'] = 'Token ' + authToken
                            localStorage.setItem('authToken', authToken)
                            localStorage.setItem('username', this.username)

                            toast(
                                {
                                    message: 'Successfully logged in. ',
                                    type: 'is-success',
                                    dismissible: true,
                                    pauseOnHover: true,
                                    position: 'top-center',
                                    animate: { in: 'fadeIn', out: 'fadeOut' },
                                }
                            )

                            this.$router.push('/profile')
                        })
                        .catch(error => {
                            if (error.response) {
                                for (const e in error.response.data) {
                                    this.errors.push(`${e}: ${error.response.data[e]}`)
                                } 
                            } else if (error.message) {
                                this.errors.push('An error occurred. Please try again.')
                            }
                        })
                }
            },
            cleanErrors() {
                this.errors = []
            }
        },
        data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    }
}
</script>
