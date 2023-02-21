<!-- Autor: xhorky32 -->
<template>
 <div id="main">
  <root>
    <topbar>
      <div class="topbar">
        <img class="icon" src="../assets/logo.png">
        <h1 id="h1h2_trip">TravelPlanApp</h1>
        <h2 id="h1h2_trip"><a onclick="window.location.href='http://localhost:8080/#/Home'">Home</a> > Planning new trip</h2>
        <div class="logout" onclick="window.location.href='http://localhost:8080/#/Login'"></div>
        <div class="settings" onclick="window.location.href='http://localhost:8080/#/Settings'"></div>
        <button class="button_menu_d" >Plan new trip</button>
      </div>
    </topbar>
    <br> <br>
    <section>
      <h1 class="u_head_f" style="text-align: center">New trip to: <input v-model="input.cityname" type="text" class="tripname_box" placeholder="Enter your desired location"></input></h1>
      
      <div class="day" :key="day">
        <h3 style="text-align:left;font-size: 1.3em">Basics</h3>
        <p>Please enter how many days are you willing to spend on the trip and the name of city or country, which you want to travel to.
        You can choose between random and default image of the trip, which is seen primarly on homepage.
        </p>
        <br>
        <h4>Length (in days):</h4><input v-model="input.triplength" type="number" placeholder=1 min="1"></input><br><br>
        <h4>Trip image:</h4>
        <input type="radio" name="one" id="one" value="default" v-model="picked" checked>
        <label for="one">Default</label>
        <br><br>
        <input type="radio" name="one" id="two" value="random" v-model="picked">
        <label for="two">Random</label>
        <br><br>
        <div id="preview"><img v-if="imgurl" :src="imgurl" /></div>
        <br><br><br>
        <button class="tripcreate_button" v-on:click="setVarText()">Confirm</button>
        <button class="tripcreate_button" onclick="window.location.href='http://localhost:8080/#/Home'">Cancel</button>
        <br>
      </div>
      <h2><br><div id="varText" class="varText"></div></h2>
    </section>
  </root>
 </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Trip',
  data: function () {
    return {
      input: {
        cityname: '',
        triplength: 1
      },
      picked: "default"
    }
  },
  methods: {
    setTransHL (i, type, hl) {
      if (type === 0) {
        this.trans.walk[i] = hl
      }
    },
    setVarText() {
      let img = this.input.cityname
      let x = 0
      document.getElementById('varText').innerHTML = ''
      if (this.input.cityname !== '') {
        if (this.picked == "random") {
          x = Math.floor(Math.random() * 5);
          img = 'trp_' + String(x)
        } else {
          img = 'none'
        }
        axios
        .get('http://localhost:5000/new%' + this.input.cityname + '%' + img.toLowerCase() + '%' + this.input.triplength)
        .then(response => (this.itinerary = response.data))
        this.$router.replace({ name: 'Home' })
      } else {
        document.getElementById('varText').innerHTML = '<div class="succTextD">You have not entered trip location!</div>'
      }
    },
  }
}
</script>

<style>
#preview {
  display: flex;
  justify-content: center;
  align-items: center;
}

#preview img {
  max-width: 100%;
  max-height: 500px;
}

  .succTextD {
    display: center;
    flex-wrap:wrap;
    text-align:center;
    margin:0px auto;
    padding-left: 15px;
    padding-right: 15px;
    padding-bottom: 7px;
    padding-top: 7px;
    width: 500px;
    font-size:20px;
    color:black;
    border: 1px solid rgb(134, 134, 134, 200);
    border-radius: 3px;
    background: linear-gradient(to bottom, #ffffffee 0%, #fefefedd 100%);
    align: center;
  }

.tripname_box {
    height: 1.75em;
    border-radius: 6px;
    width: 300px;
    font-size: 20px;
}

body{
  margin:0;
  height: 100%;
}
section{
  width: 40%;
  margin: auto;
}
.heading{
  width: 100%;
  height: 10em;
  object-fit: none;
  margin-left: 1em;
  margin-right: 1em;
}
.transport
{
  margin-top: 0.5em;
  margin-left: 0.1em;
  margin-right: 0.1em;
  width: 50px;
}
.transport_del
{
  margin-top: 1em;
  margin-bottom: 1em;
  margin-left: 1em;
  margin-right: 1em;
  width: 50px;
}
.trans{
  float: left;
  padding-left: 2em;
  padding-right: 2em;
  margin-top: 0;
  background-color: white;
  border-radius: 10px;
  margin-right: 4em;
  margin-bottom: 2em;
  left: 2em;
  position: relative;
}
.trans > .transport{
  width: 40px
}
.trans > img:hover{
  cursor: pointer;
}
.bin {
  width: 20px;
  float: right;
  margin-right: 1em;
  margin-top: 1em;
}
.bin:hover{
  cursor: pointer;
}
.action > img.transport:hover{
  cursor: pointer;
}
.action > img.transport_del:hover{
  cursor: pointer;
}
.dots{
  transform: translate(-50%, -50%) rotate(90deg);
  font-size: 15px;
  letter-spacing: 4px;
  margin-left:50%;
  width: fit-content;
  text-align: center;
}

.day {
  width: 100%;
  background-color: #ffffff;
  border-radius: 15px;
  padding-left: 1em;
  padding-right: 1em;
  padding-bottom: 1em;
  margin-bottom: 2em;
  border:1px solid black;
}
.action{
  width: 95%;
  border-radius: 10px;
  background-color: #f3f4f5;
  margin: auto;
  margin-bottom: 2em;
  overflow: hidden;
  max-height: 14em;
}
.show{
  overflow: hidden;
  height: 100%;
}
.attractionimg{
  height: 100%;
  position: relative;
  /*top: 50%;*/
  transform: translateX(-20%);
}

.right{
  margin-left: auto;
  margin-right: 0;
  width: 15em;
}

.topbar {
  width: 100%;
  background-color: #eeeeee;
  float: left;
  height: 3em;
  margin: auto
}

.radio_s {
  margin: .4rem;
  align-items: flex-start;
}

.radio_s > label {
  margin-right: 15px;
}

.topbar > .icon {
  width: 100%;
  max-width: 40px;
  float: left;
  margin-left: 2em;
  margin-top: 0.1em;
}

.topbar > .right > .settings {
  background-image: url('../assets/settings.png');
  float: left;
  margin-top: 0.3em;
  margin-right: 0.5em;
  opacity: 1;
  padding: 18px 18px;
  background-size: 35px;
  background-repeat: no-repeat;
  transition: 0.8s;
}

.topbar > .right > .settings:hover {
  opacity: 0.8;
  transition: 0.8s;
  background-image: url('../assets/settings_orange.png');
  cursor:pointer;
}
.topbar > .right > .logout {
  background-image: url('../assets/logout.png');
  float: left;
  margin-top: 0.3em;
  opacity: 1;
  padding: 18px 18px;
  background-size: 35px;
  background-repeat: no-repeat;
  transition: 0.8s;
}

.topbar > .right > .logout:hover {
  opacity: 0.8;
  transition: 0.8s;
  background-image: url('../assets/logout_orange.png');
  cursor:pointer;
}

.topbar > h1 {
  float: left;
  margin-top: 6px;
  font-variant: small-caps;
}

.topbar > .button_menu_d {
  background-color: #F9991633;
  border: none;
  color: black;
  padding: 10px 25px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  transition-duration: 0.1s;
  margin: 2px 2px;
  border: 1px solid orange;
  box-shadow: 0 3px 4px 0 rgba(0,0,0,0.08,99);
  border-radius: 10px;
  float: right;
  cursor: not-allowed;
}


.tripcreate_button {
  background-color: #F49516;
  border: none;
  color: black;
  padding: 10px 25px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  transition-duration: 0.1s;
  margin: 2px 2px;
  border: 1px solid orange;
  box-shadow: 0 3px 4px 0 rgba(0,0,0,0.08);
  border-radius: 10px;
}

.tripcreate_button:hover {
  background-color: #F6A526;
  color: black;
  box-shadow: 0 3px 6px 0 rgba(0,0,0,0.09);
  cursor:pointer;
}

tripcreate_button:active {
  background-color: #F7B546;
  box-shadow: 0 3px 6px 0 rgba(0,0,0,0.1);
}

.u_head_f {
  font-weight: normal;
  display: block;
  color: black;
  text-align: left;
  text-indent: 5em;
}

hr {
  color: black;
  border-width: 1px;
}

#h1h2trip {
  font-weight: normal;
}

figcaption {
  line-height: 3;
  font-weight: bold;
}

li {
  display: inline-block;
}

ul.images li.text-cycler {
  display: block;
  float: left;
  width: 96px;
  height: 96px;
  margin: 2px;
}

body {
  background-image: url('../assets/home_bg.png');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-position: center;
}

a {
  color: #42b983;
}
</style>
