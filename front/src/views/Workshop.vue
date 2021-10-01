<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-narrow-4">
                <h1 class="title" :key="this.workshop_name">Workshop {{ this.workshop_name }}</h1>
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
                            this.workshop_name = response.data['workshop'].workshop_name
                        }
                    })
            },
        },
        data() {
            return {
                workshop_name: ''
            }
        }
    }
</script>
