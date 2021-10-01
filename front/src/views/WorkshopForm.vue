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

                if (!this.errors.length) {
                    const workshopName = {
                        workshop_name: this.workshopName,
                    }

                    const workshop = {
                        workshop: workshopName,
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
