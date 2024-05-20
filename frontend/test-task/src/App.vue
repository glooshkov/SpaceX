<template>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <div class="menu">
    <div class="logo">
      <img class="spacex" src="/static/лого.png" alt="Логотип">
    </div>
    <div style="left: 0">
      <li class="menu-item" v-for="(title,index) in menu" :key="index"><a href="#">{{ title.text }}</a></li>
    </div>


  </div>
  <div class="app">
    <router-view />
  </div>
</template>

<script>
import {All_MENU, SITE_INFO} from "@/queries";

export default {
  name: "AppView",
  data() {
    return {
      mySite: null,
      menu: [
        //{text:'Главная'}, {text:'Технология'}, {text:'График полетов'}, {text:'Гарантии'}, {text:'О компании'}, {text:'Контакты'}
      ],
    };
  },
  async created() {
    const menu = await this.$apollo.query({
      query: All_MENU,
    });
    this.menu = menu.data.all_menu;
  },
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  align-items: center;
  justify-content: flex-start;
  scrollbar-width: thin;
  scrollbar-color: var(--color-btn-h) var(--color-bg-total);
  --color-bg-total: #111827;
  --color-btn: #6366f1;
  --color-btn-h: #8386eb;
  --color-event-border: rgba(94, 92, 230, 0.8);
  --color-text-white: #fff;
  --color-text-gray: #9e9ea4;
  --color-text-gray-h: #b4b4b4;
  --color-md: #ff9f0a;
  --color-disabled:#283144;
  --color-active:#303177;
  --color-pole:#1d2432;
  --color-border:#414141;
  --color-border-btn:#fff;
  --color-bm-lider:#1d2331;

  --color-gradient:rgba(150, 150, 150, 0.11);
  --color-transparent: rgba(0, 0, 0, 0);

  --color-red: #ff453a;
  --color-orange: #ff9f0a;
  --color-yellow: #ffd60a;
  --color-light-green: #b5f25a;
  --color-green: #32d74b;
  --color-blue: #64d2ff;
  --color-darkblue: #0a84ff;
  --color-darkpurp: #5e5ce6;
  --color-purp: #bf5af2;
  --color-pink: #f25ad9;
  --color-darkpink: #d73264;
}
body {
  background-image: url('/static/background.jpg');
  min-height: 100vh;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  background-attachment: fixed;
  color: var(--color-text-white);
  transition:
    color 0.5s,
    background-color 0.5s;
  line-height: 6;
  font-size: 18px;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}


.menu {
  list-style-type: none;
  align-items: center;
  justify-content: center;
  display: flex;
  background-color: rgba(0, 0, 0, 0.35);
  overflow: hidden;
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
  border-bottom: 1px solid var(--color-border);
  height: 7vw;
}

.menu-item {
  float: left;
}

.menu-item a {
  color: var(--color-text-white);
  text-align: center;
  padding: 0.4vw 0.3vw;
  margin: 0 1.2vw;
  text-decoration: none;
  height: 20vw;
  font-family:
    Candara,
    sans-serif;
  font-weight: 100;
  font-size: 1.2vw;
}


.menu-item a:hover {
  border-bottom: 1px solid var(--color-text-gray-h);
  color: var(--color-text-gray-h);
}

.logo{
  border: 1px solid var(--color-text-white);
  top: 0;
  position: relative;
  height: 98%;
  z-index: 2;
  margin: 0.1vw 4vw 0 4vw;
  padding: 0 1vw;
  display: flex;
  align-items: center;
}
.logo::after,
.logo::before {
  content: "";
  display: block;
  border: 1.5px solid var(--color-border);
  z-index: 10;
  position: absolute;
}

.logo::after {
  left: -1.2px;
  top: 0.8vw;
  right: -1px;
  bottom: 0.8vw;
  border-top: none;
  border-bottom: none;
}

.logo::before {
  border: 3px solid #020c17;
  left: 0.8vw;
  top: -2px;
  right: 0.8vw;
  bottom: -1px;
  border-left: none;
  border-right: none;
}
.spacex{
  transform: translateY(-15%);
  height: 2vw;

}
</style>