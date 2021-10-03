<template>
    <div class="container">
        <div class="columns">
            <div class="column">
                <div class="card" @click="redirectToCarOwner">
                    <div class="card-image">
                        <figure class="image is-4by3">
                            <img src="https://picsum.photos/id/0/2000" alt="Car owner image">
                        </figure>
                    </div>
                    <div class="card-content">
                        <strong>
                            My Cars
                        </strong>
                    </div>
                </div>
            </div>

            <div class="column">
                <div class="card" @click="redirectToMyWorkshop">
                    <div class="card-image">
                        <figure class="image is-4by3">
                            <img src="https://picsum.photos/id/1079/2000" alt="Workshop image">
                        </figure>
                    </div>
                    <div class="card-content">
                        <strong>
                            My Workshop
                        </strong>
                    </div>
                </div>
            </div>
        </div>
        <div class="columns">
            <div class="column is-half is-offset-one-quarter">
                <div class="card" @click="redirectToWorkshops">
                    <div class="card-image">
                        <figure class="image is-4by3">
                            <img src="https://picsum.photos/id/1072/2000" alt="Car owner image">
                        </figure>
                    </div>
                    <div class="card-content">
                        <strong>
                            All Workshops
                        </strong>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
</template>

<script>
    export default {
        name: 'Menu',
        methods: {
            redirectToCarOwner() {
                return this.$router.push('/profile/car-owner');
            },
            redirectToMyWorkshop() {
                return this.$router.push('/profile/workshop');
            },
            redirectToWorkshops() {
                return this.$router.push('/workshop-list');
            },
        }
    }
</script>

<style scoped>
    .card:hover {
        box-shadow: 0 10px 30px rgba(20, 20, 20, 0.5);
        transition: 0.5s;
    }
    
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>
