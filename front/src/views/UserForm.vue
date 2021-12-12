<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">User form</h1>

                <form @submit.prevent="userForm">
                    <div class="field">
                        <label>Name</label>
                        <div class="control has-icons-left">
                            <input type="text" name="first_name" class="input" v-model="this.user.first_name">
                            <span class="icon is-small is-left">
                                <i class="fas fa-signature"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Surname</label>
                        <div class="control has-icons-left">
                            <input type="text" name="last_name" class="input" v-model="this.user.last_name">
                            <span class="icon is-small is-left">
                                <i class="fas fa-signature"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Phone</label>
                        <div class="control has-icons-left">
                            <input type="phone" name="phone" class="input" v-model="this.user.phone">
                            <span class="icon is-small is-left">
                                <i class="fas fa-phone"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>City</label>
                        <div class="control has-icons-left">
                            <input type="text" name="city" class="input" v-model="this.user.city">
                            <span class="icon is-small is-left">
                                <i class="fas fa-city"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Street</label>
                        <div class="control has-icons-left">
                            <input type="text" name="street" class="input" v-model="this.user.street">
                            <span class="icon is-small is-left">
                                <i class="fas fa-road"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>House number</label>
                        <div class="control has-icons-left">
                            <input type="text" name="house_number" class="input" v-model="this.user.house_number">
                            <span class="icon is-small is-left">
                                <i class="fas fa-home"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Flat number</label>
                        <div class="control has-icons-left">
                            <input type="text" name="flat_number" class="input" v-model="this.user.flat_number">
                            <span class="icon is-small is-left">
                                <i class="fas fa-home"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Zip code</label>
                        <div class="control has-icons-left">
                            <input type="text" name="zip_code" class="input" v-model="this.user.zip_code">
                            <span class="icon is-small is-left">
                                <i class="fas fa-sort-numeric-up-alt"></i>
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
        name: 'UserForm',
        mounted() {
            this.getUser()
        },
        methods: {
            userForm() {
                this.errors = []

                if (!this.errors.length) {

                    const userData = {
                        first_name: this.user.first_name,
                        last_name: this.user.last_name,
                        city: this.user.city,
                        street: this.user.street,
                        phone: this.user.phone,
                        house_number: this.user.house_number,
                        flat_number: this.user.flat_number,
                        zip_code: this.user.zip_code,
                    }

                    const usernameStored = localStorage.getItem('username')
                    
                    axios
                        .patch(`users/user/${usernameStored}/`, userData)
                        .then(response => {
                            toast(
                                {
                                    message: 'Form was sent successfully.',
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
            async getUser() {
                const usernameStored = localStorage.getItem('username')

                axios
                    .get(`users/user/${usernameStored}/`)
                    .then(response => {
                        this.user = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
            },
            cleanErrors() {
                this.errors = []
            }

        },
        data() {
            return {
                user: '',
                errors: []
            }
        }
    }
</script>
