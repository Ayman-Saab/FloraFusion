<template>
  <div class="home container is-max-widescreen">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body">
        <div class="title">
          Hol dir frische Pflanzen nach Hause!
        </div>
        <div class="hero_side">
          <div class="_content_in_door">
            <router-link class="navbar-item" to="/zimmerpflanzen">
              Zimmerpflanzen
            </router-link>
          </div>
          <div class="_content_out_door">
            <router-link class="navbar-item" to="/outdoor-Pflanzen">
            Outdoor-Pflanzen
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- Products -->

    <div class="products-container columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-3">Zimmerpflanzen</h2>
      </div>
    
      <carousel :items-to-show="3.5">
        <slide
          class="slider column is-3"
          v-for="product in latestProducts"
          v-bind:key="product.id"
        >
          <div class="box">
            <figure class="image mb-4">
              <img v-bind:src="product.get_image">
            </figure>

            <h3 class="is-size-4">{{ product.name }}</h3>
            <p class="is-size-6 has-text-grey">${{ product.price }}</p>
            <span>view details</span>
          </div>

          <!-- </div> -->
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
      latestProducts: []
    }
  },
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },

  mounted() {
    this.getLatestProducts()
  },
  methods: {
    getLatestProducts() {
      axios
      .get('/api/v1/latest-products/')
      .then(response =>{
        this.latestProducts = response.data
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
}
</script>



<style lang="scss">

.home {


  .hero-body {
    display: flex;
    justify-content: space-between;
  }

  .products-container {

    .carousel__viewport {

      .box {
        background-color: #E5CEDC;
        border-radius: 0;   
        .image {
          img {
           height: 350px;
          }
        }
      }
    }
    
  }


}

</style>