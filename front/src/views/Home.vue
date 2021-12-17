<template>
    <div class="home">

        <div class="tile is-ancestor">
            <div class="tile is-vertical">
                <div class="tile">
                    <div class="tile is-parent is-vertical">
                        <article class="tile is-11 is-child notification is-success">
                            <p class="title">Cars</p>
                            <p class="subtitle">registered in system</p>
                            <br/>
                            <h1 class="title has-text-centered">{{this.allCars}}</h1>
                            <br/>
                        </article>
                        <article class="tile is-11 is-child notification is-light">
                            <p class="title">Drive type</p>
                            <p class="subtitle">most popular</p>
                            <br/>
                            <h1 class="title has-text-centered">{{this.mostPopularDriveType}}</h1>
                            <br/>
                        </article>
                        <article class="tile is-11 is-child notification is-success">
                            <p class="title">Services</p>
                            <p class="subtitle">registered in system</p>
                            <br/>
                            <h1 class="title has-text-centered">{{this.allServices}}</h1>
                            <br/>
                        </article>
                        <article class="tile is-11 is-child notification is-light">
                            <p class="title">Car model</p>
                            <p class="subtitle">most popular</p>
                            <br/>
                            <h1 class="title has-text-centered">{{this.popularModel[0]}} {{this.popularModel[1]}}</h1>
                            <br/>
                        </article>
                    </div>
                </div>
            </div>

            <div class="tile is-vertical">
                <div class="tile">
                    <div class="tile is-parent is-vertical">
                        <article class="tile is-11 is-child notification is-light">
                            <p class="title">Users</p>
                            <p class="subtitle">registered in system</p>
                            <br/>
                            <h1 class="title has-text-centered">{{this.allUsers}}</h1>
                            <br/>
                        </article>
                        <article class="tile is-11 is-child notification is-success">
                            <p class="title">Workshops</p>
                            <p class="subtitle">registered in system</p>
                            <br/>
                            <h1 class="title has-text-centered">{{this.allWorkshops}}</h1>
                            <br/>
                        </article>
                        <article class="tile is-11 is-child notification is-light">
                            <p class="title">Workshop</p>
                            <p class="subtitle">most popular</p>
                            <br/>
                            <h1 class="title has-text-centered">{{this.popularWorkshop}}</h1>
                            <br/>
                        </article>
                        <article class="tile is-11 is-child notification is-success">
                            <p class="title">Various</p>
                            <p class="subtitle">car models</p>
                            <br/>
                            <h1 class="title has-text-centered">{{this.differentModelsNumber}}</h1>
                            <br/>
                        </article>
                    </div>
                </div>
            </div>

            <div class="tile is-vertical">
                <div class="tile">
                    <div class="tile is-parent is-vertical">
                        <article class="tile is-11 is-child notification is-success">
                            <p class="title">Car brand</p>
                            <p class="subtitle">most popular</p>
                            <br/>
                            <h1 class="title has-text-centered">{{this.popularBrand}}</h1>
                            <br/>
                        </article>
                        <article class="tile is-11 is-child notification is-light">
                            <p class="title">Car parts</p>
                            <p class="subtitle">registered in system</p>
                            <br/>
                            <h1 class="title has-text-centered">{{this.allCarParts}}</h1>
                            <br/>
                        </article>
                        <article class="tile is-11 is-child notification is-success">
                            <p class="title">Car part</p>
                            <p class="subtitle">most frequently fixed</p>
                            <br/>
                            <h1 class="title has-text-centered">{{this.mostFrequentlyFixedPart}}</h1>
                            <br/>
                        </article>
                        <article class="tile is-11 is-child notification is-light">
                            <p class="title">Car model</p>
                            <p class="subtitle">most frequently fixed</p>
                            <br/>
                            <h1 class="title has-text-centered">{{this.mostFrequentlyFixedModel[0]}} {{this.mostFrequentlyFixedModel[1]}}</h1>
                            <br/>
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
            this.getMostFrequentlyFixedModel()
            this.getMostPopularDriveType()
            this.getDifferentModelsNumber()
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
                        if(response.data === ''){
                            this.popularBrand = 'no data'
                        } else {
                            this.popularBrand = response.data
                        }
                    })
            },
            async getMostPopularModel() {
                await axios
                    .get('cars/car/most_popular_model/')
                    .then(response => {
                        if(response.data === ''){
                            this.popularModel = ['no', 'data']
                        } else {
                            this.popularModel = response.data
                        }
                    })
            },
            async getMostPopularWorkshop() {
                await axios
                    .get('services/service/most_popular_workshop/')
                    .then(response => {
                        if(response.data === ''){
                            this.popularWorkshop = 'no data'
                        } else {
                            this.popularWorkshop = response.data
                        }
                    })
            },            
            async getMostFrequentlyFixedPart() {
                await axios
                    .get('services/service/most_frequently_fixed_part/')
                    .then(response => {
                        if(response.data === ''){
                            this.mostFrequentlyFixedPart = 'no data'
                        } else {
                            this.mostFrequentlyFixedPart = response.data
                        }
                    })
            },
            async getMostFrequentlyFixedModel() {
                await axios
                    .get('services/service/most_frequently_fixed_model/')
                    .then(response => {
                        if(response.data === ''){
                            this.mostFrequentlyFixedModel = ['no', 'data']
                        } else {
                            this.mostFrequentlyFixedModel = response.data
                        }
                        console.log(this.mostFrequentlyFixedModel)
                    })
            },
            async getMostPopularDriveType() {
                await axios
                    .get('cars/engine/most_popular_drive_type/')
                    .then(response => {
                        if(response.data === ''){
                            this.mostPopularDriveType = 'no data'
                        } else {
                            this.mostPopularDriveType = response.data
                        }
                        console.log(this.mostPopularDriveType)
                    })
            },
            async getDifferentModelsNumber() {
                await axios
                    .get('cars/car/different_models_number/')
                    .then(response => {
                        this.differentModelsNumber = response.data
                        console.log(this.differentModelsNumber)
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
                mostFrequentlyFixedModel: '',
                mostPopularDriveType: '',
                differentModelsNumber: ''
            }
        }
    }
</script>
