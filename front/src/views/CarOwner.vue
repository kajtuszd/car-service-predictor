<template>
    <div class="container">
        <h1 class="title">Car Owner</h1>
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
