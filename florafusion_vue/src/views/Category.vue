<template>
    <div class="page-category container is-max-widescreen">
        <div class="columns is-multiline">
            <div class="column is-12 mb-5">
                <section class="hero is-medium is-dark mb-6">
                    <div class="hero-body" :style="{'background-image': `url(${category.get_gategory_image})`}">
                        <h2 class="title mb-4">
                            {{ category.name }}
                        </h2>
                        <p class="is-size-5">{{ category.description }}</p>
                    </div>
                </section>
            </div>

            <ProductBox
                v-for="product in category.products"
                v-bind:key="product.id"
                v-bind:product="product"
            />
        </div>
    </div>
</template>


<script>
import axios from 'axios';

import { toast } from 'bulma-toast';

import ProductBox from '../components/ProductBox';

export default {
    name: 'Category',
    components: {
        ProductBox
    },
    data() {
        return {
            category: {
                products: []
            }
        }
    },

    mounted() {
        this.getCategory()
    },

    watch: {
        $route(to, from) {
            if(to.name === 'Category') {
                this.getCategory()
            }
        }
    },

    methods: {
        async getCategory(){
            const categorySlug = this.$route.params.category_slug

            this.$store.commit('setIsloading', true)

            await axios
                .get(`/api/v1/products/${categorySlug}/`)
                .then(response => {
                    this.category = response.data

                    document.title = this.category.name + ' | FloraFusion'
                })
                .catch(error => {
                    console.log(error)

                    toast({
                        message: 'Etwas ist schiefgegangen! Bitte versuchen Sie es erneut.',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 3000,
                    })
                })



            this.$store.commit('setIsloading', false)
        }
    }
}
</script>


<style lang="scss">
.page-category {

    .hero-body {
        /* background-image: url('/home/dci-student/final_project/FloraFusion/florafusion_vue/src/assets/images/zimmerpflanzen.jpg'); */
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;

        .title {
            font-size: 40px;
        }
        p {
            font-size: 20px;
            font-weight: 800;
        }
    }
}
</style>