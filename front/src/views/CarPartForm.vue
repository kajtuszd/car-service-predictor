<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Car part form</h1>

                <form @submit.prevent="carPartForm">

                    <div class="field">
                        <label>Category</label> <br/>
                        <div class="select">
                            <select v-model="category">
                                <option v-for="category in categories" v-bind:key="category.id">
                                    {{ category.name }}
                                </option>
                            </select>
                        </div>
                    </div>

                    <div class="field">
                        <label>Latest fix date</label>
                        <div class="control has-icons-left">
                            <input type="date" name="latest_fix_date" class="input" v-model="latest_fix_date">
                            <span class="icon is-small is-left">
                                <i class="fas fa-tools"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Latest Fix Mileage</label>
                        <div class="control has-icons-left">
                            <input type="text" name="latest_fix_mileage" class="input" v-model="latest_fix_mileage">
                            <span class="icon is-small is-left">
                                <i class="fas fa-calendar-alt"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Fix Every Period</label>
                        <div class="control has-icons-left">
                            <input type="text" name="fix_every_period" class="input" v-model="fix_every_period">
                            <span class="icon is-small is-left">
                                <i class="fas fa-clock"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Fix Every Mileage</label>
                        <div class="control has-icons-left">
                            <input type="text" name="fix_every_mileage" class="input" v-model="fix_every_mileage">
                            <span class="icon is-small is-left">
                                <i class="fas fa-road"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Next Fix Date</label>
                        <div class="control has-icons-left">
                            <input type="date" name="next_fix_date" class="input" v-model="next_fix_date">
                            <span class="icon is-small is-left">
                                <i class="fas fa-calendar"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Next Fix Mileage</label>
                        <div class="control has-icons-left">
                            <input type="text" name="next_fix_mileage" class="input" v-model="next_fix_mileage">
                            <span class="icon is-small is-left">
                                <i class="fas fa-road"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Description</label>
                        <div class="control has-icons-left">
                            <input type="text" name="description" class="input" v-model="description">
                            <span class="icon is-small is-left">
                                <i class="fas fa-pen"></i>
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
        name: 'CarPartForm',
        mounted() {
            this.getPartCategories()
        },
        methods: {
            async getPartCategories() {
                await axios
                    .get('/cars/car-part-category')
                    .then(response => {
                        this.categories = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
            },
            carPartForm() {
                this.errors = []

                if (!this.errors.length) {

                    let category = this.categories.find(elem => elem.name === this.category)

                    const carPartData = {
                        latest_fix_date: this.latest_fix_date,
                        latest_fix_mileage: this.latest_fix_mileage,
                        fix_every_period: this.fix_every_period,
                        fix_every_mileage: this.fix_every_mileage,
                        next_fix_date: this.next_fix_date,
                        next_fix_mileage: this.next_fix_mileage,
                        description: this.description,
                        category: category,
                    }
                    
                    axios
                        .post('cars/car-part/', carPartData, {params: { car_slug: this.$route.params.slug} })
                        .then(response => {
                            toast(
                                {
                                    message: 'Car part was created successfully.',
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
            cleanErrors() {
                this.errors = []
            },
            redirectToCarOwner() {
                return this.$router.push(`/profile/car-owner/${this.$route.params.slug}`)
            }
        },
        data() {
            return {
                latest_fix_date: '',
                latest_fix_mileage: '',
                fix_every_period: '',
                fix_every_mileage: '',
                next_fix_date: '',
                next_fix_mileage: '',
                description: '',
                categories: [],
                category: '',
                errors: []
            }
        }
    }
</script>
