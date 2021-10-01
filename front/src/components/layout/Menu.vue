<template>
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
                        Car Owner
                    </strong>
                </div>
            </div>
        </div>

        <div class="column">
            <div class="card" @click="redirectToWorkshop">
                <div class="card-image">
                    <figure class="image is-4by3">
                        <img src="https://picsum.photos/id/1079/2000" alt="Workshop image">
                    </figure>
                </div>
                <div class="card-content">
                    <strong>
                        Workshop
                    </strong>
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
            redirectToWorkshop() {
                return this.$router.push('/profile/workshop');
            },
        }
    }
</script>

<style scoped>
    .card:hover {
        box-shadow: 0 10px 30px rgba(20, 20, 20, 0.5);
        transition: 0.5s;
    }
</style>
