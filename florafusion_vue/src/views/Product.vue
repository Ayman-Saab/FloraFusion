<template>
    <div class="main_page_product_container">
        <section class="section">
            <div class="page_product container is-max-widescreen">
                <div class="columns is-9">
                    <div class="column mb-6">
                        <figure class="image mb-6">
                            <img v-bind:src="product.get_image">
                        </figure>
                        <h1 class="title">
                            Über {{ product.name }}
                        </h1>
                        <p class="description">
                            {{ product.description }}
                        </p>
                    </div>
                    <div class="to-add-border">
                        <div class="product-detail">
                            <h1 class="title">{{ product.name }}</h1>
                            <p class="has-text-weight-semibold is-size-5">{{ product.size }}</p>
                            <p class="has-text-weight-semibold is-size-5"><strong>Preis: </strong>{{ product.price }} €</p>

                            <div class="field mt-6 quantity_container">
                                <div class="control quantity">
                                    <input type="number" class="" min="1" v-model="quantity">
                                </div>

                                <div class="control">
                                    <a class="button addToCart" @click="addToCart">In den Pflanzenkorb</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>


<script>
import axios from 'axios'

import { toast } from 'bulma-toast'

export default {
    name: 'Product',
    data() {
        return {
            product: {},
            quantity: 1
        }   
    },
    mounted() {
       this.getProduct()
    },
    methods: {
        async getProduct() {

            this.$store.commit('setIsloading', true)

            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug
            
            await axios
                .get(`/api/v1/products/${category_slug}/${product_slug}`)
                .then(response => {
                    this.product = response.data

                    document.title = this.product.name + ' | FloraFusion'
                })
                .catch(error => {
                    console.log(error)
                })
            
            this.$store.commit('setIsloading', false)
            
        },

        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            const item = {
                product: this.product,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)
            

            toast({
                message: 'Dein neuer Freund ist hinzugefügt',
                dismissible: true,
                pauseOnHover: true,
                duration: 3000,
            })
        }
    }
}

</script>


<style>

.main_page_product_container {
    background-color: #f0e5aa;
    
    .page_product {
        .image {
            width: 40%;
        }

        .description {
            font-size: 20px;
            width: 80%;
        }
    }
    .notification {
        background-color: #627b47;
        color: #fff;
        top: 10rem;

        .delete {
            top: 4px;
            right: 4px;
        }
    }

    .to-add-border {
        align-self: center;
        border: .5px solid #627b47;
        padding: 2px 2px;
        .product-detail {
            align-self: center;
            border: .5px solid #627b47;
            padding: 50px 30px;
        }
    }


    .quantity_container {
        display: flex;
        justify-content: space-between;
        .quantity {
            /* Hide the default arrows */
            input[type=number]::-webkit-inner-spin-button,
            input[type=number]::-webkit-outer-spin-button {
            -webkit-appearance: none;
            margin: 0;
            }

            input[type=number] {
            
                padding: 12px;
                border: 1px solid #ccc;
                border-radius: 0x;
                font-size: 16px;
                width: 50px;
                text-align: center;
            }
        }

        .addToCart {
            background-color: #627b47;
            color: white;
            border-radius: 0;
            box-shadow: none;
            text-transform: uppercase;
            font-weight: bolder;
            padding: 10px 20px;
            border: none;
        }
            
    }

}

</style>