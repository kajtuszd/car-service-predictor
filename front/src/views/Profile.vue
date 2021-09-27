<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-narrow-4">
                <h1 class="title">Profile</h1>
            </div>
        </div>
        <Menu />
    </div>
</template>

<script>
    import Menu from '../components/layout/Menu.vue'

    export default {
        name: 'Profile',
        components: {
            Menu,
        },
    }
</script>
