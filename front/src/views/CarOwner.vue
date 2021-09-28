<template>
    <div class="container">
        <h1 class="title">Car Owner</h1>
        <Cars />
    </div>
</template>

<script>
    import Cars from '../components/views/Cars.vue'
    export default {
        name: 'CarOwner',
        components: {
            Cars,
        },
    }
</script>
