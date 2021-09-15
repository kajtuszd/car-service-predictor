import { createStore } from 'vuex'

export default createStore({
    state: {
        isLoading: false,
        isAuthenticated: false,
        authToken: '',
    },
    mutations: {
        startStore(state) {
            if (localStorage.getItem('authToken')) {
                state.authToken = localStorage.getItem('authToken')
                state.isAuthenticated = true
            } else {
                state.authToken = ''
                state.isAuthenticated = false
            }
        },
        setLoadingStatus(state, status) {
            state.isLoading = status
        },
        setIsAuthenticatedStatus(state, authToken) {
            state.authToken = authToken
            state.isAuthenticated = true
        },
        cleanAuthToken(state) {
            state.authToken = ''
            state.isAuthenticated = false
        }
    },
    actions: {
    },
    modules: {
}
})
