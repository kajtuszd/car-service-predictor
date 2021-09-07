<template>
    <div>
        Hello
        <button v-on:click="getCars()">Get cars</button>
        <div v-for="car in results" v-bind:key="car.slug">
            {{ car.brand }} {{ car.model }}
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'HelloWorld',
    data () {
        return {
            results: []
        }
    },

    // mounted() {
    //     this.getCars()
    // },

    methods: {
        getCars() {
            axios.get('cars/car/').then(response => {
                this.results = response.data
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
}
</script>

<style scoped>
h3 {
    margin: 40px 0 0;
}
ul {
    list-style-type: none;
    padding: 0;
}
li {
    display: inline-block;
    margin: 0 10px;
}
a {
    color: #42b983;
}
</style>
