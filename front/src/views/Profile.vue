<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-narrow-4">
                <h1 class="title">Profile</h1>
            </div>
        </div>
        <Menu />

        <router-link to="user-form">
            <button class="button is-success is-outlined">User info form</button>
        </router-link>

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
