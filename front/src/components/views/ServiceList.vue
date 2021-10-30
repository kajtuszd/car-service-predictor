<template>
    <div class="container">
        <div class="column is-12">
            <h2 class="subtitle">
                <strong>Services</strong>
            </h2>
        </div>

        <div class="column is-12">
            <table class="table is-fullwidth is-hoverable is-striped">
                <thead>
                    <tr>
                        <th>Title</th>
                        <th>Cost</th>
                        <th>Car</th>
                        <th>Owner</th>
                        <th>Car part</th>
                        <th>Date start</th>
                        <th>Is active</th>
                        <th>Workshop</th>
                    </tr>
                </thead>

                <tbody>
                    <tr v-for="service in services" :key="service.id">
                        <td>{{ service.title }}</td>
                        <td>{{ service.cost }}</td>
                        <td>{{ service.car_part.car.brand }} {{ service.car_part.car.model }}</td>
                        <td>{{ service.car_part.car.owner.username }}</td>
                        <td>{{ service.car_part.category.name }}</td>
                        <td>{{ service.date }}</td>
                        <td>{{ service.is_active }}</td>
                        <td>{{ service.workshop.workshop_name }}</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <router-link to="service-form">
            <button class="button is-success is-outlined">+ Add service</button>
        </router-link>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'ServiceList',
        mounted() {
            this.getServices()
        },
        data() {
            return {
                services: [],
            }
        },
        methods: {
            async getServices() {
                await axios
                    .get('/services/service/')
                    .then(response => {
                        this.services = response.data
                    })
            },
        },
    }
</script>
