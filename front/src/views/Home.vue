<template>
    <div class="home">

        <div class="tile is-ancestor">
            <div class="tile is-vertical">
                <div class="tile">
                    <div class="tile is-parent is-vertical">
                        <article class="tile is-10 is-child notification is-primary">
                            <p class="title">Cars</p>
                            <p class="subtitle">registered in system</p>
                            <h1 class="title">{{this.allCars}}</h1>
                        </article>
                        <article class="tile is-10 is-child notification is-primary">
                            <p class="title">Car parts</p>
                            <p class="subtitle">registered in system</p>
                            <h1 class="title">{{this.allCarParts}}</h1>
                        </article>
                        <article class="tile is-10 is-child notification is-primary">
                            <p class="title">Services</p>
                            <p class="subtitle">registered in system</p>
                            <h1 class="title">{{this.allServices}}</h1>
                        </article>
                    </div>
                </div>
            </div>

            <div class="tile is-vertical">
                <div class="tile">
                    <div class="tile is-parent is-vertical">
                        <article class="tile is-10 is-child notification is-primary">
                            <p class="title">Users</p>
                            <p class="subtitle">registered in system</p>
                            <h1 class="title">{{this.allUsers}}</h1>
                        </article>
                        <article class="tile is-10 is-child notification is-primary">
                            <p class="title">Workshops</p>
                            <p class="subtitle">registered in system</p>
                            <h1 class="title">{{this.allWorkshops}}</h1>
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
            this.getAllCarPartsNumber()
            this.getAllServicesNumber()
            this.getAllUsersNumber()
            this.getAllWorkshopsNumber()
            this.getMostPopularBrand()
            this.getMostPopularModel()
            this.getMostPopularWorkshop()
            this.getMostFrequentlyFixedPart()
        },
        methods: {
            async getAllCarsNumber() {
                await axios
                    .get('cars/car/all/')
                    .then(response => {
                        this.allCars = response.data
                    })
            },
            async getAllCarPartsNumber() {
                await axios
                    .get('cars/car-part/all/')
                    .then(response => {
                        this.allCarParts = response.data
                    })
            },
            async getAllServicesNumber() {
                await axios
                    .get('services/service/all/')
                    .then(response => {
                        this.allServices = response.data
                    })
            },
            async getAllUsersNumber() {
                await axios
                    .get('users/user/all/')
                    .then(response => {
                        this.allUsers = response.data
                    })
            },
            async getAllWorkshopsNumber() {
                await axios
                    .get('users/workshop/all/')
                    .then(response => {
                        this.allWorkshops = response.data
                    })
            },
            async getMostPopularBrand() {
                await axios
                    .get('cars/car/most_popular_brand/')
                    .then(response => {
                        this.popularBrand = response.data
                    })
            },
            async getMostPopularModel() {
                await axios
                    .get('cars/car/most_popular_model/')
                    .then(response => {
                        this.popularModel = response.data
                    })
            },
            async getMostPopularWorkshop() {
                await axios
                    .get('services/service/most_popular_workshop/')
                    .then(response => {
                        this.popularWorkshop = response.data
                    })
            },            
            async getMostFrequentlyFixedPart() {
                await axios
                    .get('services/service/most_frequently_fixed_part/')
                    .then(response => {
                        this.mostFrequentlyFixedPart = response.data
                    })
            },
        },
        data() {
            return {
                allCars: '',
                allCarParts: '',
                allWorkshops: '',
                allUsers: '',
                allServices: '',
                popularModel: '',
                popularBrand: '',
                popularWorkshop: '',
                mostFrequentlyFixedPart: '',
            }
        }
    }
</script>
