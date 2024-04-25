<template>
    <section class="section">
        <div class="page-log-in container is-max-widescreen">
            <div class="columns">
                <div class="column is-4 is-offset-4">
                    <h1 class="title">
                        Log In
                    </h1>

                    <form @submit.prevent="submitForm">
                        <div class="field">
                            <div class="control">
                                <input type="text" class="input" placeholder="username" v-model="username">
                            </div>
                        </div>
                        <p class="notification is-danger"
                            v-if="errors.length"
                            v-for="error in errors"
                            v-bind:key="error" v-show="error === 'The username is missing'">
                            {{ error }}
                        </p>
                        

                        <div class="field">
                            <div class="control">
                                <input type="password" class="input" placeholder="password" v-model="password">
                            </div>
                        </div>
                        <p class="notification is-danger"
                            v-if="errors.length"
                            v-for="error in errors"
                            v-bind:key="error" v-show="error === 'The password is too short'">
                            {{ error }}
                        </p>


                        <div class="field">
                            <div class="control">
                                <button class="button is-dark">Log In</button>
                            </div>
                        </div>
                        <hr>

                        Or <routerLink to="/sign-up">click here</routerLink> to sign up!
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>


<script>
import axios from 'axios';

export default {
    name: 'LogIn',
    components: {
        
    },
    data() {
        return {
            username: "",
            password: "",
            errors: []
        }
    },

    mounted() {
        document.title = 'Log In | FloraFusion'
    },
    computed: {
        
    },
    methods: {
        async submitForm() {
            axios.defaults.headers.common['Authorization'] = ""

            localStorage.removeItem("token")

            const formData = {
                username: this.username,
                password: this.password
            }

            await axios
            .post("/api/v1/token/login/", formData)
            .then(response => {
                const token = response.data.auth_token

                this.$store.commit('setToken', token)

                axios.defaults.headers.common['Authorization'] = "Token" + token

                localStorage.setItem("token", token)

                const toPath = this.$route.query.to || '/cart'

                this.$router.push(toPath)
            })
            .catch(error => {
                if(error.response) {
                    for(const property in error.response.data) {
                        this.errors.push(`${property}: ${error.response.data[property]}`)
                    }

                    console.log(JSON.stringify(error.response.data))
                } else if (error.message) {
                    this.errors.push('Something went wrong, Please try again')

                    console.log(JSON.stringify(error))
                }
            }) 
        }
    }
}
</script>


<style lang="scss">

</style>