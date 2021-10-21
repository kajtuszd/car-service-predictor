<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Update your {{ this.car.brand }} {{ this.car.model }}</h1>

                <form @submit.prevent="carForm">
                    <div class="field">
                        <label>Registration</label>
                        <div class="control has-icons-left">
                            <input type="text" name="registration" class="input" v-model="this.car.registration">
                            <span class="icon is-small is-left">
                                <i class="fas fa-registered"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Car mileage</label>
                        <div class="control has-icons-left">
                            <input type="text" name="carMileage" class="input" v-model="this.car.mileage">
                            <span class="icon is-small is-left">
                                <i class="fas fa-road"></i>
                            </span>
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <button class="delete" v-on:click="cleanErrors"></button>
                        <p v-for="e in errors" :key="e">{{e}}</p>
                    </div>

                    <br/>
                    
                    <div class="buttons">
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
        name: 'UpdateCar',
        methods: {
            async carForm() {
                this.errors = []

                if (this.car.registration === '') {
                    this.errors.push('Registration is required.')
                }

                if (this.car.mileage === '') {
                    this.errors.push('Car mileage number is required.')
                }

                if (!this.errors.length) {
                    
                    axios
                        .patch(`cars/car/${this.car.slug}/`, this.car)
                        .then(response => {
                            toast(
                                {
                                    message: 'Car was updated successfully.',
                                    type: 'is-success',
                                    dismissible: true,
                                    pauseOnHover: true,
                                    position: 'top-center',
                                    animate: { in: 'fadeIn', out: 'fadeOut' },
                                }
                            )
                            this.redirectToCarProfile()
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
            redirectToCarProfile() {
                return this.$router.back();
            },
            async getCar() {
                const carSlug = this.$route.params.slug

                axios
                    .get(`cars/car/${carSlug}/`)
                    .then(response => {
                        this.car = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
            },
        },
        mounted() {
            this.getCar()
        },
        data() {
            return {
                errors: [],
                car: '',
            }
        }
    }
</script>
