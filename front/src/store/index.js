import { createStore } from 'vuex'

export default createStore({
    state: {
        isAuthenticated: false,
        authToken: '',
        username: '',
    },
    mutations: {
        startStore(state) {
            if (localStorage.getItem('authToken')) {
                state.authToken = localStorage.getItem('authToken')
                state.username = localStorage.getItem('username')
                state.isAuthenticated = true
            } else {
                state.authToken = ''
                state.username = ''
                state.isAuthenticated = false
            }
        },
        setAuthToken(state, authToken, username) {
            state.authToken = authToken
            state.isAuthenticated = true
            state.username = username
        },
        cleanAuthToken(state) {
            state.authToken = ''
            state.username = ''
            state.isAuthenticated = false
        }
    },
    actions: {
    },
    modules: {
    }
})
