<template>
    <section class="section">
        <div class="page-my-account container is-max-widescreen">
            <div class="columns is-multiline">
                <h1 class="title">My Account</h1>
            </div>

            <div class="column is-12">
                <button @click="logout()" class="button is-danger">Log out</button>
            </div>
        </div>
    </section>
</template>


<script>
import axios from 'axios';

export default {
    name: 'MyAccount',
    components: {
        
    },
    data() {
        return {

        }
    },

    mounted() {
        
    },
  
    methods: {
        logout() {
            axios.defaults.headers.common['Authorization'] = ""

            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")

            this.$store.commit('removeToken')

            this.$router.push('/')
        }
    }
}
</script>


<style lang="scss">


</style>