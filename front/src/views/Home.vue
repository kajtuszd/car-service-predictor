<template>
    <div class="home">

        <div class="tile is-ancestor">
            <div class="tile is-vertical">
                <div class="tile">
                    <div class="tile is-parent is-vertical">
                        <article class="tile is-10 is-child notification is-primary">
                            <p class="title">All cars</p>
                            <p class="subtitle">registered in system</p>
                            <h1 class="title">{{this.allCars}}</h1>
                        </article>
                        <article class="tile is-10 is-child notification is-primary">
                            <p class="title">...tiles</p>
                            <p class="subtitle">Bottom tile</p>
                        </article>
                        <article class="tile is-10 is-child notification is-primary">
                            <p class="title">...tiles</p>
                            <p class="subtitle">Bottom tile</p>
                        </article>
                    </div>
                </div>
            </div>

            <div class="tile is-vertical">
                <div class="tile">
                    <div class="tile is-parent is-vertical">
                        <article class="tile is-10 is-child notification is-primary">
                            <p class="title">Vertical...</p>
                            <p class="subtitle">Top tile</p>
                        </article>
                        <article class="tile is-10 is-child notification is-primary">
                            <p class="title">...tiles</p>
                            <p class="subtitle">Bottom tile</p>
                        </article>
                        <article class="tile is-10 is-child notification is-primary">
                            <p class="title">...tiles</p>
                            <p class="subtitle">Bottom tile</p>
                        </article>
                    </div>
                </div>
            </div>

            <div class="tile is-vertical">
                <div class="tile">
                    <div class="tile is-parent is-vertical">
                        <article class="tile is-10 is-child notification is-primary">
                            <p class="title">Vertical...</p>
                            <p class="subtitle">Top tile</p>
                        </article>
                        <article class="tile is-10 is-child notification is-primary">
                            <p class="title">...tiles</p>
                            <p class="subtitle">Bottom tile</p>
                        </article>
                        <article class="tile is-10 is-child notification is-primary">
                            <p class="title">...tiles</p>
                            <p class="subtitle">Bottom tile</p>
                        </article>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'Home',
        mounted() {
            this.getAllCarsNumber()
        },
        methods: {
            async getAllCarsNumber() {
                await axios
                    .get('cars/car/all/')
                    .then(response => {
                        this.allCars = response.data
                    })
            }
        },
        data() {
            return {
                allCars: '',
            }
        }
    }
</script>
