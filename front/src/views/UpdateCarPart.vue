<template>
    <div class="container">
        <div class="columns">
            <div class="column is-12">
                <h1 class="title">Update part</h1>

                <form @submit.prevent="carPartForm">

                    <div class="field">
                        <label>Latest fix date</label>
                        <div class="control has-icons-left">
                            <input type="date" name="latest_fix_date" class="input" v-model="this.carPart.latest_fix_date">
                            <span class="icon is-small is-left">
                                <i class="fas fa-tools"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Latest Fix Mileage</label>
                        <div class="control has-icons-left">
                            <input type="text" name="latest_fix_mileage" class="input" v-model="this.carPart.latest_fix_mileage">
                            <span class="icon is-small is-left">
                                <i class="fas fa-calendar-alt"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Fix Every Period</label>
                        <div class="control has-icons-left">
                            <input type="text" name="fix_every_period" class="input" v-model="this.carPart.fix_every_period">
                            <span class="icon is-small is-left">
                                <i class="fas fa-clock"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Fix Every Mileage</label>
                        <div class="control has-icons-left">
                            <input type="text" name="fix_every_mileage" class="input" v-model="this.carPart.fix_every_mileage">
                            <span class="icon is-small is-left">
                                <i class="fas fa-road"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Next Fix Date</label>
                        <div class="control has-icons-left">
                            <input type="date" name="next_fix_date" class="input" v-model="this.carPart.next_fix_date">
                            <span class="icon is-small is-left">
                                <i class="fas fa-calendar"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Next Fix Mileage</label>
                        <div class="control has-icons-left">
                            <input type="text" name="next_fix_mileage" class="input" v-model="this.carPart.next_fix_mileage">
                            <span class="icon is-small is-left">
                                <i class="fas fa-road"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Description</label>
                        <div class="control has-icons-left">
                            <input type="text" name="description" class="input" v-model="this.carPart.description">
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
        name: 'UpdateCarPart',
        methods: {
            async carPartForm() {
                this.errors = []

                if (!this.errors.length) {
                    const carPartSlug = this.$route.params.part_slug

                    const carPartData = {
                        latest_fix_date : this.carPart.latest_fix_date,
                        latest_fix_mileage : this.carPart.latest_fix_mileage,
                        fix_every_period : this.carPart.fix_every_period,
                        fix_every_mileage : this.carPart.fix_every_mileage,
                        next_fix_date : this.carPart.next_fix_date,
                        next_fix_mileage : this.carPart.next_fix_mileage,
                        description : this.carPart.description,
                    }

                    await axios
                        .patch(`cars/car-part/${carPartSlug}/`, carPartData)
                        .then(response => {
                            toast(
                                {
                                    message: 'Car part was updated successfully.',
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
            async getCarPart() {
                const carPartSlug = this.$route.params.part_slug

                await axios
                    .get(`cars/car-part/${carPartSlug}/`)
                    .then(response => {
                        this.carPart = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
            },
            async getCarPartCategories() {

                await axios
                    .get(`cars/car-part-category/`)
                    .then(response => {
                        this.carPartCategories = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
            },
        },
        mounted() {
            this.getCarPart()
            this.getCarPartCategories()
        },
        data() {
            return {
                errors: [],
                carPart: '',
                carPartCategories: ''
            }
        }
    }
</script>
