<template>
    <div class="container">
        <div class="column is-12">
            <h2 class="subtitle">
                <strong>Cars</strong>
            </h2>
        </div>

        <div class="column is-12">
            <table class="table is-fullwidth is-hoverable is-striped">
                <thead>
                    <tr>
                        <th>Brand</th>
                        <th>Model</th>
                        <th>Production year</th>
                        <th>Mileage</th>
                        <th>Daily mileage</th>
                    </tr>
                </thead>

                <tbody>
                    <tr v-for="car in cars" :key="car.id">
                        <td>{{ car.brand }}</td>
                        <td>{{ car.model }}</td>
                        <td>{{ car.production_year }}</td>
                        <td>{{ car.mileage }}</td>
                        <td>{{ car.daily_mileage }}</td>
                        <td>
                            <router-link :to="{ name: 'CarDetail', params: { slug: car.slug }}">
                                <button class="button is-dark is-outlined">More ...</button>
                            </router-link>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <router-link to="car-form">
            <button class="button is-success is-outlined">+ Add car</button>
        </router-link>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'CarList',
        mounted() {
            this.getCars()
        },
        data() {
            return {
                cars: []
            }
        },
        methods: {
            async getCars() {
                axios
                    .get('/cars/car/')
                    .then(response => {
                        this.cars = response.data
                    })
            }
        },
    }
</script>
