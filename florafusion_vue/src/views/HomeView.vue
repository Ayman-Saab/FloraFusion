<template>
  <div class="home container is-max-widescreen">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body">
        <h1 class="title">
          Hol dir frische Pflanzen nach Hause!
        </h1>
        <div class="hero_side">
          <div class="_content_in_door"> 
            <router-link class="" to="/zimmerpflanzen">
              Zimmerpflanzen
            </router-link>
          </div>
          <div class="_content_out_door btn btn-3 hover-border-4">
            <router-link class="" to="/outdoor-Pflanzen">
              Outdoor-Pflanzen
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- Products -->

    <div class="products-container is-multiline">

      <!-- Zimmerpflanzen slide show -->

      <div class="column is-12">
        <h2 class="is-size-3">Zimmerpflanzen</h2>
      </div>
      
      <carousel v-bind="settings" :breakpoints="breakpoints">
        <slide
          class="slider"
          v-for="product in ProductsList"
          v-bind:key="product.id"
          v-show="product.category === 1"
        >
        
          <div class="box carousel__item">
            <figure class="image mb-4">
              <div class="product_image" :style="{'background-image': `url(${product.get_thumbnail})`}"></div>
            </figure>
            <div>
              <h3 class="is-size-4 product_name">{{ product.name }}</h3>
              <p>{{ product.size }}</p>
              <p class="is-size-6 has-text-grey">${{ product.price }}</p>
              <div>{{ product.category }}</div>
              <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">View Details</router-link>
            </div>
          </div>
        </slide>

        <template #addons>
          <navigation />
          <pagination />
        </template>
      </carousel>


      <!-- Outdoor-Pflanzen slide show -->

      <div class="column is-12 mt-4">
        <h2 class="is-size-3">Outdoor-Pflanzen</h2>
      </div>
      
      <carousel v-bind="settings" :breakpoints="breakpoints">
        <slide
          class="slider"
          v-for="product in ProductsList"
          v-bind:key="product.id"
          v-show="product.category === 3"
        >
        
          <div class="box carousel__item">
            <figure class="image mb-4">
              <div class="product_image" :style="{'background-image': `url(${product.get_thumbnail})`}"></div>
            </figure>
            <div>
              <h3 class="is-size-4 product_name">{{ product.name }}</h3>
              <p>{{ product.size }}</p>
              <p class="is-size-6 has-text-grey">${{ product.price }}</p>
              <div>{{ product.category }}</div>
              <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">View Details</router-link>
            </div>
          </div>
        </slide>

        <template #addons>
          <navigation />
          <pagination />
        </template>
      </carousel>
    </div>
  </div>
</template>

<script>

import axios from 'axios';

import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'

export default {
  name: 'HomeView',
  data() {
    return {
      ProductsList: [],
    
      settings: {
        itemsToShow: 1,
        snapAlign: 'center',
      },
      breakpoints: {
        400: {
          itemsToShow: 2,
          snapAlign: 'center',
        },
        700: {
          itemsToShow: 3.5,
          snapAlign: 'center',
        },
        1024: {
          itemsToShow: 4.5,
          snapAlign: 'start',
        },
      },
    }
  },

  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },

  mounted() {
    this.getProductsList()

    document.title = 'FloraFusion'
  },
  methods: {
    async getProductsList() {
      this.$store.commit('setIsloading', true)

      await axios
        .get('/api/v1/latest-products/')
        .then(response =>{
          this.ProductsList = response.data
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

.home {

  .hero-body {
    display: flex;
    justify-content: space-between;
    background-image: url('/home/dci-student/final_project/FloraFusion/florafusion_vue/src/assets/images/hero.jpg');
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;

    .title {
      font-size: 40px;
      
    }

    ._content_in_door, ._content_out_door {
      a {
        color: #fff;
      }
    }
     
  }

  .products-container {
    
    .carousel__viewport {

      .carousel__slide {
        display: block;
        
      }
      .carousel__slide:not(:last-child) {
        padding-right: 10px;
      }

      .box {
        background-color: #F7D08A;
        border-radius: 0;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        font-weight: 800;
        
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
    }
    
  }


}

</style>