<template>
  <div class="block">
    <img class="mars" src="/static/mars.png">
    <img class="ship" src="/static/ship.png" >
    <div class="line">
      <button class="start-btn"><span class="span-left"/>Начать путешествие<span class="span-right"/></button>
<!--      <svg id="mySVG" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"/>-->

      <svg :width="width_box" height="130" :viewBox="view_box">
        <path :d="path" stroke="url(#grad)" :stroke-width="width_line" fill="transparent"/>
        <defs>
          <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="white" stop-opacity="0" />
            <stop offset="100%" stop-color="white" stop-opacity="1" />
          </linearGradient>
        </defs>
      </svg>
      <div class="gradient-line"></div>
    </div>
    <div class="title">
      <h1 class="adventure">
        ПУТЕШЕСТВИЕ<p class="small">на красную планету</p>
      </h1>
      <h2 ></h2>
    </div>
    <ul class="table">
      <li class="grid" v-for="(text,index) in benefits" :key="index">
        <p class="text">{{text.top_text}}</p>
        <p class="integer" v-html="text.integer"></p>
        <p class="text">{{text.bot_text}}</p>
      </li>
    </ul>
  </div>


</template>

<script>
import {All_BENEFITS, All_MENU} from "@/queries";

export default {
  name: "home",
  data() {
    return {
      benefits: [
        // {
        //   top: 'мы',
        //   center: '1',
        //   bottom: 'на рынке',
        // },
        // {
        //   top: 'гарантируем',
        //   center: '50%',
        //   bottom: 'безопасность',
        // },
        // {
        //   top: 'календарик за',
        //   center: `2001<span style="font-size: 1.1vw;">г.</span>`,
        //   bottom: 'в подарок',
        // },
        // {
        //   top: 'путешествие',
        //   center: '597',
        //   bottom: 'дней',
        // },
      ],
      path: '',
      width_line: '',
      view_box: '',
      width_box: '',
      heigth_box:'',
    };
  },
  mounted() {
    this.updatePath();
    window.addEventListener('resize', this.updatePath);
  },
  methods: {
    updatePath() {
      const svgWidth = document.body.clientWidth;
      const endLine = (svgWidth * 0.34).toFixed(0)
      const radius = (svgWidth * 0.0026).toFixed(2)

      this.path = `M0,50 L140,140 L${endLine},140 A${radius},${radius} 0 1,1 ${parseFloat(endLine) + 0.01},140.1`;
      this.width_line = `${(svgWidth * 0.0013).toFixed(0)}`
      this.view_box = `0 0 ${parseFloat(endLine)+parseFloat(radius)*2} 150`
      this.width_box = `${(svgWidth * 0.297).toFixed(0)}`
      // console.log(this.path, '\n width_line', this.width_line, '\n view_box', this.view_box, '\n width_box', this.width_box, '\n svgWidth', svgWidth)
    },
  },
  beforeUnmount() {
    window.removeEventListener('resize', this.updatePath);
  },
  async created() {
    try {
      const benefits = await this.$apollo.query({
        query: All_BENEFITS,
      });
      this.benefits = benefits.data.all_benefits;
    } catch (error) {
      console.error('Ошибка при создании хука:', error);
    }
  }
};
</script>

<style>
.block {
  display: flex;
    align-items: center;
    min-height: 100vh;
    min-width: 100vw;
    flex-wrap: wrap;
    justify-content: center;
}
.table {
  display: grid;
  position: relative;
  grid-template-columns: auto auto;
  list-style-type: none;
  transform: translate(30vw, 0);
  opacity: 0;
  z-index: 4;
  animation: appearanceBtn 0.5s 1.4s forwards;
}
.table li {
  padding: 1vw;
  text-align: center;
  display: grid;
  align-items: center;
  justify-content: center;
  width: 12.5vw;
  aspect-ratio: 1;
  margin: 0.3vw;
}
.grid{
  background-image: linear-gradient(var(--gradient-rotation), rgba(0, 0, 0, 0), rgba(121, 121, 121, 0.02), var(--color-gradient));
  position: relative;
  overflow: hidden;
}
.grid:hover {
  --color-gradient: rgba(225, 225, 225, 0.20);
}
.grid:nth-child(1) {
  --gradient-rotation: 135deg;
  --color-int: #ffffff;
  --border-to-side: to right bottom;
  --border-bottom: 0;
  --border-top: none;
  --border-left: none;
  --border-right: 0;
  --border-before-width: 100%;
  --border-after-width: 1px;
  --border-before-height: 1px;
  --border-after-height: 100%;
  --border-before-transform-origin: right;
  --border-after-transform-origin: bottom;
}
.grid:nth-child(2) {
  --gradient-rotation: 225deg;
  --color-int: #c9c9c9;
  --border-to-side: to left bottom;
  --border-bottom: 0;
  --border-top: none;
  --border-left: 0;
  --border-right: none;
  --border-before-width: 100%;
  --border-after-width: 1px;
  --border-before-height: 1px;
  --border-after-height: 100%;
  --border-before-transform-origin: left;
  --border-after-transform-origin: bottom;
}
.grid:nth-child(3) {
  --gradient-rotation: 45deg;
  --color-int: #ffffff;
  --border-to-side: to right top;
  --border-bottom: none;
  --border-top: 0;
  --border-left: none;
  --border-right: 0;
  --border-before-width: 100%;
  --border-after-width: 1px;
  --border-before-height: 1px;
  --border-after-height: 100%;
  --border-before-transform-origin: right;
  --border-after-transform-origin: top;
}
.grid:nth-child(4) {
  --gradient-rotation: 315deg;
  --color-int: #c9c9c9;
  --border-to-side: to left top;
  --border-bottom: none;
  --border-top: 0;
  --border-left: 0;
  --border-right: none;
  --border-before-width: 100%;
  --border-after-width: 1px;
  --border-before-height: 1px;
  --border-after-height: 100%;
  --border-before-transform-origin: left;
  --border-after-transform-origin: top;
}
.grid:before,
.grid:after {
  content: '';
  position: absolute;
  background-image: linear-gradient(var(--border-to-side), rgba(255, 255, 255, 0), rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.5));
  pointer-events: none;
}
.grid:before {
  bottom: var(--border-bottom);
  left: var(--border-left);
  top: var(--border-top);
  right: var(--border-right);
  width: var(--border-before-width);
  height: var(--border-before-height);
  transform: scaleX(0);
  transform-origin: var(--border-before-transform-origin);
  transition: transform 0.3s ease;
}
.grid:after {
  bottom: var(--border-bottom);
  left: var(--border-left);
  top: var(--border-top);
  right: var(--border-right);
  width: var(--border-after-width);
  height: var(--border-after-height);
  transform: scaleY(0);
  transform-origin: var(--border-after-transform-origin);
  transition: transform 0.3s ease;
}
.grid:hover:before,
.grid:hover:after {
  transform: scaleX(1);
}
.text, .integer{
  font-family: Calibri, sans-serif;
}
.text{
  font-size: 1.1vw;
  font-weight: 200;
  line-height: 0.6;
  color: var(--color-text);
}
.integer{
  font-size: 4.2vw;
  font-weight: 600;
  line-height: 0.3;
  margin-bottom: -1.15vw;
  color: var(--color-int);
  height: 1.15vw;
}
.mars{
  position: absolute;
  height: 59.8vh;
  z-index: 3;
  transform: translate(0, 0.2vh);
  border-radius: 50%;
}
.ship{
  position: absolute;
  height: 18vh;
  z-index: 3;
  transform: translate(-0.5vw, 0.2vh);
  border-radius: 50%;
  animation: moveShip 1.3s ease-out forwards;
}
@keyframes moveShip {
    0% { bottom: 1vh; left: 50vw; } /* начальные координаты */
    100% { bottom: 22vh; left: 50vw; } /* конечные координаты */
}
.title {
  display: flex;
  align-items: flex-start;
  position: absolute;
  line-height: 1;
  transform: translate(-28vw, -10vh);
  opacity: 0;
  animation: slideTitle 1s 1.4s forwards;
}
@keyframes slideTitle {
    from { transform: translate(0, -10vh); opacity: 0; }
    to { transform: translate(-28vw, -10vh); opacity: 1; }
}
.adventure{
  font-family: Arial, sans-serif;
  letter-spacing: 0.2vw;
  font-size: 4vw;
  background: linear-gradient(110deg, #ffffff, #ffa167, #ff6200);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  line-height: 1;
}
.small{
  font-family: Arial, sans-serif;
  letter-spacing: 0;
  font-size: 1.9vw;
  font-weight: 200;
}
.line{
  position: absolute;
  left: 50vw;
  z-index: 5;
  transform: translate(-99.6%, 10vh);
  display: flex;
  animation: appearanceLine 1s 1.2s forwards;
}
.start-btn{
  width: 15vw;
  height: 2.9vw;
  font-family: Arial, sans-serif;
  color: var(--color-text-gray-h);
  font-size: 1vw;
  background-color: rgba(2, 12, 23, 0.75);
  border-image: linear-gradient(to right top, #23599c, #09213d, #09213d, #23599c) 1;
  border-width: 0.13vw;
  border-style: solid;
  position: relative;
  display: flex;
  justify-content: space-between;
  transform: translateY(-50%);
  animation: appearanceBtn 0.5s 1.4s forwards;
}
.line, .start-btn {
  opacity: 0;
}
@keyframes appearanceLine {
    from {  opacity: 0; }
    to {  opacity: 1; }
}
@keyframes appearanceBtn {
    from { opacity: 0; }
    to { opacity: 1; }
}
.span-left,
.span-right{
  position: relative;
  height: 100%;
}
.span-left::before,
.span-left::after,
.span-right::before,
.span-right::after {
  content: "";
  border: 0.13vw solid #fff;
  position: absolute;
  pointer-events: none;
  width: 0.3vw;
  aspect-ratio: 1;
  background: transparent;
}
.span-left::before {
  left: -2px;
  bottom: -2px;
  border-right: none;
  border-top: none;
  filter: blur(0.3vw);
}
.span-left::after {
  left: -2px;
  bottom: -2px;
  border-right: none;
  border-top: none;
}
.span-right::before {
  right: -1px;
  top: -1px;
  border-left: none;
  border-bottom: none;
  filter: blur(0.3vw);
}
.span-right::after {
  right: -1px;
  top: -1px;
  border-left: none;
  border-bottom: none;
}
.start-btn:hover {
  border-image: linear-gradient(to right top, #23599c, #23599c, #09213d, #23599c, #23599c) 1;
  transition: 0.5s ease;
  color: #f8f8f8;
  .span-right::before,
  .span-right::after,
  .span-left::before,
  .span-left::after {
    content: "";
    border-image: linear-gradient(to right top, #ffffff, rgba(111, 144, 183, 0), #ffffff) 1;
    border-width: 0.13vw;
    border-style: solid;
    position: absolute;
    pointer-events: none;
    width: 2.9vw;
    aspect-ratio: 2.5;
    background: transparent;
    transition: 0.5s ease;
  }
  .span-right::before {
    right: -1px;
    top: -1px;
    border-left: none;
    border-bottom: none;
    filter: blur(0.3vw);
  }
  .span-right::after {
    right: -1px;
    top: -1px;
    border-left: none;
    border-bottom: none;
  }
  .span-left::before {
    left: -2px;
    bottom: -2px;
    border-right: none;
    border-top: none;
    filter: blur(0.3vw);
  }
  .span-left::after {
    left: -2px;
    bottom: -2px;
    border-right: none;
    border-top: none;
  }
}
</style>