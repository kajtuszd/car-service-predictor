<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Car form</h1>

                <form @submit.prevent="carForm">
                    <div class="field">
                        <label>Brand</label>
                        <div class="control has-icons-left">
                            <input type="text" name="brand" class="input" v-model="brand">
                            <span class="icon is-small is-left">
                                <i class="fas fa-car"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Model</label>
                        <div class="control has-icons-left">
                            <input type="text" name="model" class="input" v-model="model">
                            <span class="icon is-small is-left">
                                <i class="fas fa-car-side"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Production year</label>
                        <div class="control has-icons-left">
                            <input type="text" name="productionYear" class="input" v-model="productionYear">
                            <span class="icon is-small is-left">
                                <i class="fas fa-calendar-alt"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Registration</label>
                        <div class="control has-icons-left">
                            <input type="text" name="registration" class="input" v-model="registration">
                            <span class="icon is-small is-left">
                                <i class="fas fa-registered"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Car mileage</label>
                        <div class="control has-icons-left">
                            <input type="text" name="carMileage" class="input" v-model="carMileage">
                            <span class="icon is-small is-left">
                                <i class="fas fa-road"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Engine Capacity</label>
                        <div class="control has-icons-left">
                            <input type="text" name="capacity" class="input" v-model="capacity">
                            <span class="icon is-small is-left">
                                <i class="fas fa-tools"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Horsepower</label>
                        <div class="control has-icons-left">
                            <input type="text" name="horsepower" class="input" v-model="horsepower">
                            <span class="icon is-small is-left">
                                <i class="fas fa-horse"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Drive type</label> <br/>
                        <div class="select">
                            <select v-model="driveType">
                                <option value="Petrol">Petrol</option>
                                <option value="Diesel">Diesel</option>
                                <option value="Hybrid">Hybrid</option>
                                <option value="LPG">LPG</option>
                            </select>
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
                            <button class="button is-danger is-outlined" @click="redirectToCarOwner">Cancel</button>
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
        name: 'CarForm',
        methods: {
            carForm() {
                this.errors = []

                if (this.brand === '') {
                    this.errors.push('Brand is required.')
                }
                
                if (this.model === '') {
                    this.errors.push('Model is required.')
                }

                if (this.productionYear === '') {
                    this.errors.push('Production year is required.')
                }

                if (this.registration === '') {
                    this.errors.push('Registration is required.')
                }

                if (this.carMileage === '') {
                    this.errors.push('Car mileage number is required.')
                }

                if (!this.errors.length) {

                    const engineData = {
                        horsepower: this.horsepower,
                        capacity: this.capacity,
                        engine_type: this.driveType,
                    }

                    const carData = {
                        brand: this.brand,
                        model: this.model,
                        production_year: this.productionYear,
                        registration: this.registration,
                        mileage: this.carMileage,
                        engine: engineData,
                    }
                    console.log(carData)
                    
                    axios
                        .post('cars/car/', carData)
                        .then(response => {
                            toast(
                                {
                                    message: 'Car was created successfully.',
                                    type: 'is-success',
                                    dismissible: true,
                                    pauseOnHover: true,
                                    position: 'top-center',
                                    animate: { in: 'fadeIn', out: 'fadeOut' },
                                }
                            )
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
            redirectToCarOwner() {
                return this.$router.push('car-owner');
            }

        },
        data() {
            return {
                brand: '',
                model: '',
                productionYear: '',
                registration: '',
                carMileage: '',
                engine: '',
                horsepower: '',
                capacity: '',
                driveType: '',
                errors: []
            }
        }
    }
</script>
