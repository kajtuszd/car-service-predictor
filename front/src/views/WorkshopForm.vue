<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Workshop form</h1>

                <form @submit.prevent="workshopForm">
                    <div class="field">
                        <label>Workshop name</label>
                        <div class="control has-icons-left">
                            <input type="text" name="workshopName" class="input" v-model="workshopName">
                            <span class="icon is-small is-left">
                                <i class="fas fa-signature"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>City</label>
                        <div class="control has-icons-left">
                            <input type="text" name="city" class="input" v-model="city">
                            <span class="icon is-small is-left">
                                <i class="fas fa-city"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Street</label>
                        <div class="control has-icons-left">
                            <input type="text" name="street" class="input" v-model="street">
                            <span class="icon is-small is-left">
                                <i class="fas fa-road"></i>
                            </span>
                        </div>
                    </div>


                    <div class="field">
                        <label>House number</label>
                        <div class="control has-icons-left">
                            <input type="text" name="house_number" class="input" v-model="house_number">
                            <span class="icon is-small is-left">
                                <i class="fas fa-home"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Flat number</label>
                        <div class="control has-icons-left">
                            <input type="text" name="flat_number" class="input" v-model="flat_number">
                            <span class="icon is-small is-left">
                                <i class="fas fa-home"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Zip code</label>
                        <div class="control has-icons-left">
                            <input type="text" name="zip_code" class="input" v-model="zip_code">
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
        name: 'WorkshopForm',
        methods: {
            workshopForm() {
                this.errors = []

                if (this.workshopName === '') {
                    this.errors.push('Workshop name is required.')
                }

                if (this.city === '') {
                    this.errors.push('City is required.')
                }

                if (this.street === '') {
                    this.errors.push('Street is required.')
                }

                if (this.house_number === '') {
                    this.errors.push('House number is required.')
                }

                if (this.zip_code === '') {
                    this.errors.push('Zip code is required.')
                }

                if (!this.errors.length) {
                    const workshopData = {
                        workshop_name: this.workshopName,
                        city: this.city,
                        street: this.street,
                        house_number: this.house_number,
                        flat_number: this.flat_number,
                        zip_code: this.zip_code,

                    }

                    const workshop = {
                        workshop: workshopData,
                    }

                    const usernameStored = localStorage.getItem('username')

                    axios
                        .patch(`users/user/${usernameStored}/`, workshop)
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

                            this.$router.push('/profile/workshop')
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
            },
        },
        data() {
            return {
                workshopName: '',
                errors: []
            }
        }
    }
</script>
