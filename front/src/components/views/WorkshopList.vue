<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-narrow-4">
                <h1 class="title">Workshop list</h1>
            </div>
        </div>

        <div class="columns center" v-for="workshop in this.workshops" :key="workshop">
                <div class="column is-8">
                    <div class="card">
                        <div class="card-content">
                            <div class="media">
                                <div class="media-content">
                                    <p class="title is-4">{{ workshop.workshop_name }}</p>
                                    <p class="subtitle is-6">{{ workshop.email }} | {{ workshop.phone }}</p>
                                </div>
                            </div>

                            <div class="content">
                                {{ workshop.zip_code }}
                                {{ workshop.city }}
                                <div v-if="workshop.flat_number">
                                    {{ workshop.street }}
                                    {{ workshop.house_number }}/
                                    {{ workshop.flat_number }} <br>
                                </div>
                                <div v-else>
                                    {{ workshop.street }}
                                    {{ workshop.house_number }}
                                </div>
                            </div>

                            <footer class="card-footer" v-if="this.$store.state.isAuthenticated">
                                <a class="card-footer-item">
                                    <!-- <router-link to="workshop-form"> -->
                                        <button class="button is-success is-outlined">Link to workshop</button>
                                    <!-- </router-link> -->
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
        name: 'WorkshopList',
        mounted() {
            this.getWorkshops()
        },
        data() {
            return {
                workshops: []
            }
        },
        methods: {
            async getWorkshops() {
                axios
                    .get('users/workshop/')
                    .then(response => {
                        this.workshops = response.data
                    })
            }
        },
    }
</script>

<style scoped>
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>