<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="container is-max-widescreen pt-3 pb-3 navigation">
        <div class="brand">
          <ul class="under_line">
            <li>
              <router-link to="/">
                <strong class="image_logo is-size-4">
                  FloraFusion                 
                </strong>
              </router-link>
            </li>
          </ul> 

          <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>

        <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
          <div class="navbar-start">
            <ul class="under_line">
              <li>
                <router-link to="/zimmerpflanzen">
                  Zimmerpflanzen
                </router-link>
                <router-link to="/outdoor-pflanzen">
                  Outdoor-Pflanzen
                </router-link>
              </li>
            </ul>
          </div>
          <div class="navbar-end">
            <div class="navbar-item">
              <form method="get" action="/search">
                <div class="field has-addons">
                  <div class="control">
                    <input type="text" class="input" placeholder="Pflanzen suchen" name="query">
                  </div>

                  <div class="control">
                    <button class="button">
                      <span class="icon">
                        <i class="fas fa-search"></i>
                      </span>
                    </button>
                  </div>
                </div>
              </form>
            </div>
        
            <div class="navbar-item">
              <div class="buttons">
                <template v-if="$store.state.isAuthenticated">
                  <router-link to="/my-account" class="mr-4">
                    <i class="fa-solid fa-user"></i>
                  </router-link>
                </template>

                <template v-else>
                  <router-link to="/log-in" class="mr-4">
                    <i class="fa fa-sign-in" aria-hidden="true"></i>
                  </router-link>
                </template>

                <router-link to="/cart">
                  <div class="icon">
                    <i class="fas fa-shopping-cart"></i>
                    <span class="cartTotal">{{ cartTotalLenght }}</span>
                  </div>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading}">
      <div class="lds-dual-ring"></div>
    </div>

    <div>
      <router-view/>
    </div>

    <footer class="footer">
      <strong><p class="has-text-centered">&copy; {{ currentYear }} FloraFusion</p></strong>
    </footer>
  </div>
</template>

<script>
import axios from 'axios';

  export default {
    data(){
      return {
        showMobileMenu: false,
        cart: {
          items: []
        },
        currentYear: new Date().getFullYear()
      }
    },
    beforeCreate() {
      this.$store.commit('initializeStore')

      const token = this.$store.state.token

      if(token) {
        axios.defaults.headers.common['Authorization'] = "Token" + token
      } else {
        axios.defaults.headers.common['Authorization'] = ""
      }
    },
    mounted() {
      this.cart = this.$store.state.cart
    },
    computed: {
      cartTotalLenght() {
        let totalLenght = 0

        for (let i = 0; i < this.cart.items.length; i++) {
          totalLenght += this.cart.items[i].quantity
        }

        return totalLenght
      }
    }
  }
</script>

<style lang="scss">

@import "../node_modules/bulma";

body {
  font-family: geomanistregular, Helvetica, sans-serif;
}

.brand {
  display: flex;
  align-items: center;
}

.under_line { 
  list-style: none;
  display: flex;
  align-items: center;

  a {
    color: #fff;
    text-decoration: none;
    display: inline-block;
    position: relative;
    font-weight: 800;
    padding-right: 20px;
  }
  a:after {    
    background: none repeat scroll 0 0 transparent;
    bottom: 0;
    content: "";
    display: block;
    height: 2px;
    left: 50%;
    position: absolute;
    background: #fff;
    transition: width 0.3s ease 0s, left 0.3s ease 0s;
    width: 0;
  }
  a:hover:after { 
    width: 80%; 
    left: 0;
    right: 0; 
  }
}
  

.navbar {
  background-color: #627b47;

  .navbar-end {
    input {
      border-radius: 0;
      &:focus {
        box-shadow: none;
        border-color: #627b47;
      }
    }
    .button {
      border-radius: 0;
    }

    .buttons {
      
      a {
        color: #fff;
        font-size: 25px;
      }
      .cartTotal {
        color: #fff;
        font-weight: 900;
        position: absolute;
        top: 0;
        left: 80px;
        font-size: 15px;
        background: #F7D08A;
        border-radius: 50%;
        height: 20px;
        width: 20px;
        text-align: center;
        
      }
    }
  }
}


.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring::after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #627b47;
  border-color: #627b47 transparent #627b47 transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transform: all 0.3s;
  transition:  all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
</style>
