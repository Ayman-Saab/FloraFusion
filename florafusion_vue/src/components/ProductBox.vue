<template>
    <div class="column is-3">
        <router-link v-bind:to="product.get_absolute_url" class="">
            <div class="box_product_container carousel__item">
                <figure class="image mb-4 mt-4">
                <!-- <img v-bind:src="product.get_image"> -->
                <div class="product_image" :style="{'background-image': `url(${product.get_thumbnail})`}"></div>
                </figure>
                <div class="box-details">
                    <div class="container_name_price">
                        <h3 class="is-size-4 product_name">{{ product.name }}</h3>
                        <p class="is-size-6">{{ product.price }} €</p>
                    </div>
                <p>{{ product.size }}</p>
                </div>
            </div>
        </router-link>
    </div>
</template>

<script>
export default {
    name: 'ProductBox',
    props: {
        product: Object
    }
}
</script>

 
<style lang="scss">
.box_product_container {
    background-color: #F7D08A;
    border-radius: 0;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    font-weight: 800;
    padding: 10px;


    .box-details {
        background-color: #627b47;
        color: #ffff;
        text-align: center;
        padding-bottom: 5px;
        .container_name_price {
            display: flex;
            justify-content: space-around;
            align-items: center;
        }
    }

        
    .product_name {
        font-weight: 800;
    }
    .product_image {
        width: 100%;
        height: 260px;
        background-position: center;
        background-repeat: no-repeat;
        background-size: contain;
    
    }
    .button {
        background-color: #627b47;
        font-weight: 600;
        border-radius: 0;
        color: #fff;
    }
}
</style>