<template>
  <section class="section">
    <div class="home container is-max-widescreen">
      <section class="hero is-medium is-dark mb-6">
        <div class="hero-body">
          <h1 class="title">
            Hol dir frische Pflanzen nach Hause!
          </h1>
          <div class="hero_side">
            <router-link class="" to="/zimmerpflanzen">
              <div class="_content_in_door"> 
                Zimmerpflanzen
              </div>
            </router-link>
            <router-link class="" to="/outdoor-Pflanzen">
              <div class="_content_out_door btn btn-3 hover-border-4">
                Outdoor-Pflanzen
              </div>
            </router-link>
          </div>
        </div>
      </section>

      <!-- Products -->

      <div class="products-container is-multiline">

        <div class="title-container is-12">
          <h2 class="is-size-3">Zimmerpflanzen</h2>
        </div>

        <swiper
          :slidesPerView="4"
          :spaceBetween="30"
          :autoplay="{
            delay: 2500,
            disableOnInteraction: false,
          }"
          :navigation="true"
          :pagination="{
            clickable: true,
          }"
          :mousewheel="true"
          :keyboard="true"
          :modules="modules"
          class="mySwiper"
        >
          <swiper-slide
          v-for="product in ProductsList"
          v-bind:key="product.id"
          v-show="product.name_category === 'in'"
          >
          <router-link v-bind:to="product.get_absolute_url" class="">
              <div class="box carousel__item">
                <figure class="image mb-4">
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
          </swiper-slide>
        </swiper>

    
        <div class="title-container is-12">
          <h2 class="is-size-3">Outdoor-Pflanzen</h2>
        </div>
        <swiper
          :slidesPerView="4"
          :spaceBetween="30"
          :autoplay="{
            delay: 3000,
            disableOnInteraction: false,
          }"
          :navigation="true"
          :pagination="{
            clickable: true,
          }"
          :mousewheel="true"
          :keyboard="true"
          :modules="modules"
          class="mySwiper"
        >
          <swiper-slide
          v-for="product in ProductsList"
          v-bind:key="product.id"
          v-show="product.name_category === 'out'"
          >
            <router-link v-bind:to="product.get_absolute_url" class="">
              <div class="box carousel__item">
                <figure class="image mb-4">
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
          </swiper-slide>
        </swiper>
      </div>
    </div>
  </section>
</template>

<script>

import axios from 'axios';
import 'swiper/css';

import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';
import 'swiper/css/effect-fade';

import { Navigation, Pagination, Mousewheel, Keyboard, Autoplay } from 'swiper/modules';

import { Swiper, SwiperSlide } from 'swiper/vue';

export default {
  name: 'HomeView',
  data() {
    return {
      ProductsList: [],
    }
  },

  components: {
    Pagination,
    Navigation,
    Swiper,
    SwiperSlide,
  },

  setup() {
    return {
      modules: [Navigation, Pagination, Mousewheel, Keyboard, Autoplay],
    };
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

    },
  }
}
</script>

<style lang="scss">

.home {

  .hero-body {
    
    background-image: url('/home/dci-student/final_project/FloraFusion/florafusion_vue/src/assets/images/hero.jpg');
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;

    .title {
      font-size: 40px;      
    }

    ._content_out_door {
      padding: 10px;
      background-color: #fff;  
      text-transform: uppercase;
      font-weight: 800;
      text-align: center;
      width: 300px;
      color: #627b47;
    }
    ._content_in_door {
      text-align: center;
      background-color: #627b47;
      text-transform: uppercase;
      padding: 10px;
      font-weight: 800;
      width: 300px;
      margin-bottom: 10px;
      color: #fff;
    }
     
  }

  .products-container {
    

    .title-container {
      margin-top: 60px;
      h2 {
        font-weight: 800;
        margin-bottom: 20px;
      }
    }
    
    .swiper-button-prev, .swiper-button-next {
      color: #627b47;
      &::after {
        font-size: 25px;
        font-weight: 800;
      }
    }
    
    .swiper-pagination-bullet-active {
        opacity: var(--swiper-pagination-bullet-opacity, 1);
        background: #627b47;
    }
    .swiper-horizontal > .swiper-pagination-bullets, .swiper-pagination-bullets.swiper-pagination-horizontal {
      bottom: 0;
      top: var(--swiper-pagination-top, auto);
      left: 0;
      width: 100%;
    }

    .box {
      background-color: #F7D08A;
      border-radius: 0;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      font-weight: 800;
      text-align: center;
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
    }
    .button {
      background-color: #627b47;
      font-weight: 600;
      border-radius: 0;
    }
    
  }
}

</style>