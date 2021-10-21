<template>
    <div class="container">
        <h1 class="title">Car Owner</h1>
        <div class="buttons">
            <router-link to="/profile" class="button is-danger is-outlined">
                <i class="fas fa-arrow-left"></i>
            </router-link>
        </div>

        <CarList />
    </div>
</template>

<script>
    import CarList from '../components/views/CarList.vue'
    export default {
        name: 'CarOwner',
        components: {
            CarList,
        },
    }
</script>
