<template>
    <section class="section">
        <div class="page-search container is-max-widescreen">
            <div class="columns is-multiline">
                <div class="column is-12">
                    <h1 class="title"><span>{{ products.length }}</span> Pflanzen gefunden mit <span class="name">{{ query }}</span></h1>
                </div>
                
                <ProductBox
                    v-for="product in products"
                    v-bind:key="product.id"
                    v-bind:product="product"
                />
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
import ProductBox from '../components/ProductBox';

export default {
    name: 'Search',
    components: {
        ProductBox
    },
    data() {
        return {
            products: [],
            query: ''
        }
    },
    mounted() {
        document.title = 'Search | FloraFusion'

        let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)

        if (params.get('query')) {
            this.query = params.get('query')

            this.performSearch()
        }
    },
    methods: {
        async performSearch() {

            this.$store.commit('setIsloading', true)

            await axios
                .post(`/api/v1/products/search/`, {'query': this.query})
                .then(response => {
                    this.products = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsloading', false)
        }
    }
    
}
</script>

 
<style lang="scss">
.page-search {
    .title {
        .name {
            color: #627b47;
        }
    }
}
</style>