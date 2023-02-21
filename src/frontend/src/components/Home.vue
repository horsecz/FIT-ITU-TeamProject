<!--Autor: xhorky32 - webova stranka, edit,  xhomol32 - mobilna verzia, upravy css-->
<template>
<div id="main">
 <root>
   <meta name="viewport" content="width=device-width, initial-scale=1" />
    <topbar>
     <div class="topbar">
        <img class="icon" src="../assets/logo.png">
        <h1>TravelPlanApp</h1>
        <h2><div class="varEditT" id="varEditT">Home</div></h2>
            <div class="logout" @click="logout()"></div>
            <div class="settings" onclick="window.location.href='http://localhost:8080/#/Settings'"></div>
           <button class="button_menu" onclick="window.location.href='http://localhost:8080/#/NewTrip'">Plan new trip</button>
           <button class="button_menu" v-on:click="setEdit()">Delete trips</button>
     </div>
    </topbar>
    <br> <br>
    <div class="h1_div"><h1 class="u_head">Your trips</h1><hr></div>
   <div class="centered">
     <div class="u_trip" id="upc" >
       <figure v-for="(trip) in mytrips" :key="trip.id" @click="openTrip(trip.id)">
         <img :src="require('@/assets/' + trip.image + '.jpg')" class="trip_btn">
         <h3 class="figtxt">{{ trip.name }}</h3>
       </figure>
     </div>
   </div>

    <div class="h1_div"><h1 class="u_head">Recommended</h1><hr></div><br>
   <div class="centered">
     <div class="u_trips" id="upc" >
      <figure v-for="(tripp) in alltrips" :key="tripp.id" @click="openTrip(tripp.id)">
        <div id="div">
        <img :src="require('@/assets/' + tripp.image + '.jpg')" class="trip_btn">
       <h3 class="figtxt">{{ tripp.name }}</h3>
       </div>
      </figure>
     </div>
   </div>
    <br>
    <footer>
      <p class="copyright">© ITU PROJEKT 2021</p>
    </footer>
 </root>
 </div>
</template>

<script>
import image from '../assets/none.jpg'
import axios from 'axios'
export default {
  name: 'Home',
  data: function () {
    return {
      image: image,
      mytrips: null,
      alltrips: null,
      loading: true,
      errored: false,
      delmode: false
    }
  },
  created () {
    axios
      .get('http://localhost:5000/trips/0')
      .then(response => (this.mytrips = response.data))
    axios
      .get('http://localhost:5000/trips')
      .then(response => (this.alltrips = response.data))
  },
  methods: {
    setEdit() {
      this.delmode = !this.delmode
      if (this.delmode)
        document.getElementById('varEditT').innerHTML = 'Home (trip removal mode)'
      else
        document.getElementById('varEditT').innerHTML = 'Home'
    },
    async openTrip (TripId) {
      if (this.delmode) {
        const response = await fetch('http://localhost:5000/delete%' + TripId)
        const data = await response.json()

        axios
      .get('http://localhost:5000/trips/0')
      .then(response => (this.mytrips = response.data))
        axios
      .get('http://localhost:5000/trips')
      .then(response => (this.alltrips = response.data))
      } else {
        this.$router.push({path: 'Trip', query: {id: TripId}})
      }      
    },
    logout () {
      this.$emit('authenticated', false)
      this.$router.replace({ name: 'login' })
    }
  }
}
</script>

<style>
body{
  margin:auto;
  background-image: url('../assets/home_bg.png');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-position: center;
}

.h1_div {
    display: center;
    flex-wrap:wrap;
    text-align:center;
    margin:0px auto;
    padding-left: 7px;
    padding-right: 7px;
    padding-bottom: 0px;
    padding-top: 2px;
    width: 500px;
    font-size:15px;
    color:black;
    border: 1px linear-gradient(to bottom, #ffffffee 0%, #ffffffff 88%);
    border-radius: 10px;
    background: linear-gradient(to bottom, #00000000 0%, #ffffffff 88%);
    align: center;
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.right{
  margin-left: auto;
  margin-right: 0;
  width: 15em;
}

  a {
    cursor: pointer;
    color: black;
  }

/******** TOP BAR ************/
  .topbar {
    width: 100%;
    background-color: #eeeeee;
    float: left;
    height: 3em;
    margin: auto;
  }

  .topbar > .icon {
    width: 100%;
    max-width: 40px;
    float: left;
    margin-left: 0.5em;
    margin-top: 0.1em;
  }

  .settings {
    background-image: url('../assets/settings.png');
    float: right;
    margin-top: 0.3em;
    margin-right: 0.5em;
    margin-left: 1em;
    opacity: 1;
    padding: 18px 18px;
    background-size: 35px;
    background-repeat: no-repeat;
    transition: 0.8s;
  }

  .settings:hover {
    opacity: 0.8;
    transition: 0.8s;
    background-image: url('../assets/settings_orange.png');
    cursor:pointer;
  }
  .logout {
    background-image: url('../assets/logout.png');
    float: right;
    margin-top: 0.3em;
    margin-right: 0.3em;
    opacity: 1;
    padding: 18px 18px;
    background-size: 35px;
    background-repeat: no-repeat;
    transition: 0.8s;
  }

  .logout:hover {
    opacity: 0.8;
    transition: 0.8s;
    background-image: url('../assets/logout_orange.png');
    cursor:pointer;
  }

  .topbar > h1 {
    float: left;
    margin-left: 1em;
    margin-top: 6px;
    font-variant: small-caps;
  }

  .topbar > h2 {
    float: left;
    margin-left: 4em;
    margin-top: 10px;
  }

  .topbar > .button_menu {
    background-color: #F49516;
    border: none;
    color: black;
    padding: 10px 25px;
    text-align: center;
    text-decoration: none;
    float: right;
    font-size: 16px;
    transition-duration: 0.1s;
    margin: 2px 2px;
    border: 1px solid orange;
    box-shadow: 0 3px 4px 0 rgba(0,0,0,0.08);
    border-radius: 10px;
  }

  .topbar > .button_menu:hover {
    background-color: #F6A526;
    color: black;
    box-shadow: 0 3px 6px 0 rgba(0,0,0,0.09);
    cursor:pointer;
  }

  .topbar >.button_menu:active {
    background-color: #F7B546;
    box-shadow: 0 3px 6px 0 rgba(0,0,0,0.1);
  }

  @media screen and (max-width: 600px) {
    .topbar > h1 {
    display: none;
    }
  }

/******************************* */

/* SECTION "YOUR TRIP"  */
figure{
  cursor: pointer;
}
.u_trip > figure > .trip_btn{
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 5px;
  object-fit: cover;
  width: 300px;
  height: 300px;
  flex-shrink: 0;
}

.trip_btn:hover{
  color: white;
  box-shadow: 0 12px 16px 0 rgba(0,0,0,0.33), 0 15px 50px 0 rgba(0,0,0,0.19);
}
.u_trip{
  display: flex;
  overflow-x: auto;
}

/* SECTION "RECOMMENDED" */
#div > .trip_btn{
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 5px;
  width: 150px;
  height: 150px;
  object-fit: cover;
}
.u_trips{
  background-size: cover;
  display: flex;
  overflow:hidden;
  -webkit-overflow-scrolling: touch;
}
#div{
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  animation: slide-it 15s infinite;
}

@keyframes slide-it {
  0%    { transform: translateX(0); }
  25%   { transform: translateX( calc(-50% - 100px) ); }
  50%   { transform: translateX( calc(-200% - 200px) ); }
  100%  { transform: translateX( calc(-300% - 300px) ); }
}

  footer {
    position: relative;
    height: 40px;
    width: 100%;
    background-color: #333333;
  }
  p.copyright{
    position:absolute;
    width: 100%;
    color: #fff;
    line-height: 25px;
    font-size: 0.8em;
    text-align: left;
  }

  #main {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
