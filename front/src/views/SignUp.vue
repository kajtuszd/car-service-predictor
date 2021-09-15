<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Sign Up</h1>

                <form @submit.prevent="signUpForm">
                    <div class="field">
                        <label>Email</label>
                        <div class="control has-icons-left">
                            <input type="email" name="email" class="input" v-model="email">
                            <span class="icon is-small is-left">
                                <i class="fas fa-envelope"></i>
                            </span>
                        </div>
                    </div>

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
                            <input type="password" name="password1" class="input" v-model="password1">
                            <span class="icon is-small is-left">
                                <i class="fas fa-lock"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Repeat Password</label>
                        <div class="control has-icons-left">
                            <input type="password" name="password2" class="input" v-model="password2">
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
        name: 'SignUp',
        methods: {
            signUpForm() {
                this.errors = []

                if (this.email === '') {
                    this.errors.push('Email is required.')
                }
                
                if (this.username === '') {
                    this.errors.push('Username is required.')
                }

                if (this.password1 === '') {
                    this.errors.push('Password is required.')
                }

                if (this.password2 === '') {
                    this.errors.push('Password repeat is required.')
                }

                if (this.password1 !== this.password2) {
                    this.errors.push('Given passwords are different.')
                }

                if (!this.errors.length) {
                    const signUpData = {
                        email: this.email,
                        password: this.password1,
                        username: this.username,
                    }

                    axios
                        .post('auth/users/', signUpData)
                        .then(response => {
                            toast(
                                {
                                    message: 'Account was successfully created. ' +
                                             'Now you are able to log in.',
                                    type: 'is-success',
                                    dismissible: true,
                                    pauseOnHover: true,
                                    position: 'top-center',
                                }
                            )

                            this.$router.push('/log-in')
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
                email: '',
                username: '',
                password1: '',
                password2: '',
                errors: []
            }
        }
    }
</script>
