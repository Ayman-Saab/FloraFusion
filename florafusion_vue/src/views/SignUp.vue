<template>
    <section class="section">
        <div class="page-sign-up container is-max-widescreen">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Sign Up</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <div class="control">
                            <input type="text" class="input" placeholder="username" v-model="username">
                        </div>
                    </div>
                    <p class="notification is-danger"
                        v-if="errors.length"
                        v-for="error in errors"
                        v-bind:key="error" v-show="error === 'The username is missing'">{{ error }}</p>
                    

                    <div class="field">
                        <div class="control">
                            <input type="password" class="input" placeholder="password" v-model="password">
                        </div>
                    </div>
                    <p class="notification is-danger"
                        v-if="errors.length"
                        v-for="error in errors"
                        v-bind:key="error" v-show="error === 'The password is too short'">{{ error }}</p>

                    <div class="field">
                        <div class="control">
                            <input type="password" class="input" placeholder="repeat password" v-model="password2">
                        </div>
                    </div>
                    <p class="notification is-danger"
                        v-if="errors.length"
                        v-for="error in errors"
                        v-bind:key="error" v-show="error === 'The password doesn\'t match'">{{ error }}</p>


                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Sign up</button>
                        </div>
                    </div>
                    <hr>

                    Or <routerLink to="/log-in">click here</routerLink> to log in!
                </form>
            </div>
        </div>
    </section>
</template>


<script>
import axios from 'axios';
import { toast } from 'bulma-toast';

export default {
    name: 'SignUp',
    components: {
        
    },
    data() {
        return {
            username: "",
            password: "",
            password2: "",
            errors: []
        }
    },

    mounted() {
        
    },
    computed: {
        
    },
    methods: {
        submitForm() {
            this.errors = []
            if(this.username === "") {
                this.errors.push('The username is missing')
            }
            if(this.password === "") {
                this.errors.push('The password is too short')
            }
            if(this.password !== this.password2) {
                this.errors.push('The password doesn\'t match')
            }

            if(!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password
                }

                axios
                .post("/api/v1/users/", formData)
                .then(response => {
                   
                    toast({
                        message: 'Account created, please log in!',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 3000,
                        position: 'bottom-right'
                    })

                    this.$router.push('/log-in')
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
}
</script>


<style lang="scss">

.page-sign-up {
    .notification {
        top: 0px;
        background-color: rgb(245, 106, 106);
    }
}

</style>