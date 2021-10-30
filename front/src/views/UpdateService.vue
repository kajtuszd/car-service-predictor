<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Update {{ this.service.title }}</h1>

                <form @submit.prevent="serviceForm">
                    <div class="field">
                        <label>Title</label>
                        <div class="control has-icons-left">
                            <input type="text" name="title" class="input" v-model="this.service.title">
                            <span class="icon is-small is-left">
                                <i class="fas fa-car"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Date</label>
                        <div class="control has-icons-left">
                            <input type="date" name="date" class="input" v-model="this.service.date">
                            <span class="icon is-small is-left">
                                <i class="fas fa-calendar-alt"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Time</label>
                        <div class="control has-icons-left">
                            <input type="time" name="time" class="input" v-model="this.service.time">
                            <span class="icon is-small is-left">
                                <i class="fas fa-registered"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Cost</label>
                        <div class="control has-icons-left">
                            <input type="text" name="cost" class="input" v-model="this.service.cost">
                            <span class="icon is-small is-left">
                                <i class="fas fa-registered"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label>Description</label>
                        <div class="control has-icons-left">
                            <input type="text" name="description" class="input" v-model="this.service.description">
                            <span class="icon is-small is-left">
                                <i class="fas fa-road"></i>
                            </span>
                        </div>
                    </div>

                    <label class="checkbox">Is active</label>
                    <div class="control">
                        <input type="checkbox" name="is_active" v-model="this.service.is_active">
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
        name: 'UpdateService',
        methods: {
            async serviceForm() {
                this.errors = []

                if (!this.errors.length) {

                    const serviceData = {
                        title: this.service.title,
                        date: this.service.date,
                        time: this.service.time,
                        description: this.service.description,
                        workshop_name: this.service.workshop_name,
                        car_part_slug: this.service.part,
                        cost: this.service.cost,
                        is_active: this.service.is_active,
                    }
                    
                    await axios
                        .patch(`services/service/${this.service.slug}/`, serviceData, 
                                {params: { username: localStorage.getItem('username') } }
                            )
                        .then(response => {
                            toast(
                                {
                                    message: 'Service was updated successfully.',
                                    type: 'is-success',
                                    dismissible: true,
                                    pauseOnHover: true,
                                    position: 'top-center',
                                    animate: { in: 'fadeIn', out: 'fadeOut' },
                                }
                            )
                            this.redirectToWorkshop()
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
            redirectToWorkshop() {
                return this.$router.back();
            },
            async getService() {
                const serviceSlug = this.$route.params.slug

                await axios
                    .get(`services/service/${serviceSlug}/`, {params: { username: localStorage.getItem('username') } })
                    .then(response => {
                        this.service = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
            },
        },
        mounted() {
            this.getService()
        },
        data() {
            return {
                errors: [],
                service: '',
            }
        }
    }
</script>
