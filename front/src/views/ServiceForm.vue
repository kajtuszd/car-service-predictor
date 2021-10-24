<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Service form</h1>

                <form @submit.prevent="serviceForm">
                    <div class="field">
                        <label>Title</label>
                        <div class="control has-icons-left">
                            <input type="text" name="title" class="input" v-model="title">
                            <span class="icon is-small is-left">
                                <i class="fas fa-car"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Car part</label> <br/>
                        <div class="select">
                            <select v-model="part">
                                <option v-for="part in parts" v-bind:key="part">
                                    {{ part.car.brand }} {{ part.car.model }} - {{ part.category.name }}
                                </option>
                            </select>
                        </div>
                    </div>

                    <div class="field">
                        <label>Date</label>
                        <div class="control has-icons-left">
                            <input type="date" name="date" class="input" v-model="date">
                            <span class="icon is-small is-left">
                                <i class="fas fa-calendar-alt"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Time</label>
                        <div class="control has-icons-left">
                            <input type="time" name="time" class="input" v-model="time">
                            <span class="icon is-small is-left">
                                <i class="fas fa-registered"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Description</label>
                        <div class="control has-icons-left">
                            <input type="text" name="description" class="input" v-model="description">
                            <span class="icon is-small is-left">
                                <i class="fas fa-road"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Workshop</label> <br/>
                        <div class="select">
                            <select v-model="workshop">
                                <option v-for="workshop in workshops" v-bind:key="workshop">
                                    {{ workshop.workshop_name }}
                                </option>
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
        name: 'ServiceForm',
        mounted() {
            this.getWorkshops()
            this.getCarParts()
        },
        methods: {
            serviceForm() {
                this.errors = []

                if (!this.errors.length) {
                    
                    let workshop = this.workshops.find(elem => elem.workshop_name === this.workshop)
                    let partTextWordsArray = this.part.split(" ")
                    // let partCategoryName = partTextWordsArray[partTextWordsArray.length - 1] 
                    
                    let partCategoryName = ''
                    for (let i = partTextWordsArray.length - 1; partTextWordsArray[i] !== '-'; i--) {
                        partCategoryName = (partTextWordsArray[i] + ' ').concat(partCategoryName)
                    }
                    var lastIndex = partCategoryName.lastIndexOf(" ");
                    partCategoryName = partCategoryName.substring(0, lastIndex)
                    console.log(partCategoryName)
                    let part = this.parts.find(elem => elem.category.name === partCategoryName)

                    const serviceData = {
                        title: this.title,
                        date: this.date,
                        time: this.time,
                        description: this.description,
                        workshop_name: workshop.workshop_name,
                        car_part_slug: part.slug,
                        cost: 0,
                    }
                    
                    axios
                        .post('services/service/', serviceData, {params: { car_part_slug: part.slug, workshop_name: workshop.workshop_name}})
                        .then(response => {
                            toast(
                                {
                                    message: 'Service was created successfully.',
                                    type: 'is-success',
                                    dismissible: true,
                                    pauseOnHover: true,
                                    position: 'top-center',
                                    animate: { in: 'fadeIn', out: 'fadeOut' },
                                }
                            )
                            this.redirectToCarOwner()
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
            async getWorkshops() {
                await axios
                    .get('/users/workshop')
                    .then(response => {
                        this.workshops = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
            },
            async getCarParts() {
                await axios
                    .get('/cars/car-part')
                    .then(response => {
                        this.parts = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
            },
            cleanErrors() {
                this.errors = []
            },
            redirectToCarOwner() {
                return this.$router.push('car-owner')
            }
        },
        data() {
            return {
                title: '',
                part: '',
                date: '',
                time: '',
                description: '',
                workshop: '',
                errors: [],
                workshops: [],
                parts: [],
            }
        }
    }
</script>
