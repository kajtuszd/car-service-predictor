<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-narrow-4">
                <h1 class="title" :key="this.workshop">Workshop profile</h1>

                <div class="card" :key="this.workshop">
                    <div class="card-content">
                        <div class="media">
                            <div class="media-content">
                                <p class="title is-4">{{ this.workshop.workshop_name }}</p>
                                <p class="subtitle is-6">{{ this.workshop.email }} | {{ this.workshop.phone }}</p>
                            </div>
                        </div>

                        <div class="content">
                            {{ this.workshop.zip_code }}
                            {{ this.workshop.city }} <div v-if="this.workshop.flat_number">
                                {{ this.workshop.street }}
                                {{ this.workshop.house_number }}/
                                {{ this.workshop.flat_number }} <br>
                            </div>
                            <div v-else>
                                {{ this.workshop.street }}
                                {{ this.workshop.house_number }}
                            </div>
                        </div>
                        <footer class="card-footer">
                            <a class="card-footer-item">
                                <router-link to="workshop-form">
                                    <button class="button is-success is-outlined">Edit</button>
                                </router-link>
                            </a>
                        </footer>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'Workshop',
        mounted() {
            this.isWorkshopCreated()
        },
        methods: {
            async isWorkshopCreated() {
                const usernameStored = localStorage.getItem('username')
                await axios
                    .get(`users/user/${usernameStored}/`)
                    .then(response => {
                        if(!response.data['workshop']) {
                            this.$router.push('/profile/workshop-form') 
                        } else {
                            this.workshop = response.data['workshop']
                        }
                    })
            },
        },
        data() {
            return {
                workshop: ''
            }
        }
    }
</script>
