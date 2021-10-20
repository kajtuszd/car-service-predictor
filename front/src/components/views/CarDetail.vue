<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-narrow-4">
                <h1 class="title" :key="this.car">Car profile</h1>

                <div class="card" :key="this.car">
                    <div class="card-content">
                        <div class="media">
                            <div class="media-content">
                                <p class="title is-4">{{ this.car.brand }} {{ this.car.model }}</p>
                            </div>
                        </div>

                        <div class="content">
                            Production year: {{ this.car.production_year }} <br>
                            Mileage: {{ this.car.mileage }} <br>
                            Power: {{ this.car?.engine?.horsepower }} <br>
                            Engine capacity: {{ this.car?.engine?.capacity }} <br>
                            Drive type: {{ this.car?.engine?.engine_type }} <br>
                            License plate: {{ this.car.registration }}
                        </div>
                        <footer class="card-footer">
                            <a class="card-footer-item">
                                <router-link :to="{ name: 'UpdateCar'}">
                                    <button class="button is-success is-outlined">Edit</button>
                                </router-link>
                            </a>
                        </footer>
                    </div>
                </div>
            </div>
        </div>

        <CarPartList />

    </div>
</template>

<script>
    import axios from 'axios'
    import CarPartList from '../layout/CarPartList.vue'

    export default {
        name: 'Car',
        components: {
            CarPartList,
        },
        mounted() {
            this.getCar()
        },
        methods: {
            async getCar() {
                const carSlug = this.$route.params.slug

                await axios
                    .get(`cars/car/${carSlug}/`)
                    .then(response => {
                        this.car = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
            },
        },
        data() {
            return {
                car: [],
            }
        },
    }
</script>
