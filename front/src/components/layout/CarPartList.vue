<template>
    <div class="container">
        <div class="column is-12">
            <h2 class="subtitle">
                <strong>Parts</strong>
            </h2>
        </div>

        <div class="column is-12">
            <table class="table is-fullwidth is-hoverable is-striped">
                <thead>
                    <tr>
                        <th>Category</th>
                        <th>Latest fix date</th>
                        <th>Latest fix mileage</th>
                        <th>Fix every period</th>
                        <th>Fix every mileage</th>
                        <th>Next fix date</th>
                        <th>Next fix mileage</th>
                        <th>Description</th>
                    </tr>
                </thead>

                <tbody>
                    <tr v-for="part in parts" :key="part.id">
                        <td>{{ part.category }}</td>
                        <td>{{ part.latest_fix_date }}</td>
                        <td>{{ part.latest_fix_mileage }}</td>
                        <td>{{ part.fix_every_period }}</td>
                        <td>{{ part.fix_every_mileage }}</td>
                        <td>{{ part.next_fix_date }}</td>
                        <td>{{ part.next_fix_mileage }}</td>
                        <td>{{ part.description }}</td>
                        <!-- <td>
                            <router-link :to="{ name: 'CarDetail', params: { slug: car.slug }}">
                                <button class="button is-dark is-outlined">More ...</button>
                            </router-link>
                        </td> -->
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- <router-link to="car-form">
            <button class="button is-success is-outlined">+ Add part</button>
        </router-link> -->
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'CarPartList',
        mounted() {
            this.getParts()
            this.getCategories()
        },
        data() {
            return {
                parts: [],
                categories: []
            }
        },
        methods: {
            async getParts() {
                await axios
                    .get('/cars/car-part/', {params: { car_slug: this.$route.params.slug } })
                    .then(response => {
                        this.parts = response.data
                    })
            },
            async getCategories() {
                await axios
                    .get('/cars/car-part-category')
                    .then(response => {
                        var categories = response.data
                        this.parts.forEach(function (elem, ind) {
                            elem["category"] = categories[ind].name
                        })
                    })
                    .catch(error => {
                        console.log(error)
                    })
            },
        },
    }
</script>
