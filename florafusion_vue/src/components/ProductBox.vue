<template>
    <div class="column is-3">
        <div class="box_product_container carousel__item">
            <figure class="image mb-4 mt-4">
              <!-- <img v-bind:src="product.get_image"> -->
              <div class="product_image" :style="{'background-image': `url(${product.get_thumbnail})`}"></div>
            </figure>
            <div>
              <h3 class="is-size-4 product_name">{{ product.name }}</h3>
              <p>{{ product.size }}</p>
              <p class="is-size-6 has-text-grey">${{ product.price }}</p>
              <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">View Details</router-link>
            </div>
        </div>
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
    text-align: center;
    background-color: #F7D08A;
    border-radius: 0;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    font-weight: 800;
    padding: 20px;
        
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
}
</style>