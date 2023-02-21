<!-- Autor: xdobro23, Edit: xhorky32 -->
<template>
 <div id="main">
  <root>
    <topbar>
      <div class="topbar">
        <img class="icon" src="../assets/logo.png">
        <h1 id="h1h2_trip">TravelPlanApp</h1>
        <h2 id="h1h2_trip"><a onclick="window.location.href='http://localhost:8080/#/Home'">Home</a> > Trip</h2>
        <div class="logout" onclick="window.location.href='http://localhost:8080/#/Login'"></div>
        <div class="settings" onclick="window.location.href='http://localhost:8080/#/Settings'"></div>
        <button class="button_menu" onclick="window.location.href='http://localhost:8080/#/NewTrip'">Plan new trip</button>
      </div>
    </topbar>
    <br> <br>
    <section>
      <img :src="require('@/assets/' + itinerary.image + '.jpg')" class="heading">
      <h1 class="u_head_f" style="text-align: center">{{ itinerary.name }}</h1>
      <div id="test"></div>
      <div v-for="(day, index) in itinerary.actions.days" class="day" :key="day">
        <h3 style="text-align:left;font-size: 1.3em">Day {{ index + 1 }}</h3>
        <div v-for="(action, index_act) in day" :key="action">
          <div class="dots" v-if="parseInt(index_act) > 0">•••</div>
          <div class="action">
            <img class="bin" :src="require('@/assets/bin.png')" v-on:click="DeleteLine(index, index_act)">
            <div v-if="action.type !== 'attraction'" style="margin-bottom: 1em">
              <img :src="require('@/assets/' + action.type + '.png')" class="transport"> <br>
              <!--div @focus="changeDuration(index, index_act)" tabindex="0"-->~{{ action.duration }}<!--/div-->
            </div>
            <div v-if="action.type === 'attraction'" style="margin-bottom: 1em">
              <div style="width: 30%;float:left;">
                <div class="show">
                  <img :src="require('@/assets/' + action.image + '.jpg')" v-if="action.type === 'attraction'" class="attractionimg">
                </div>
              </div>
              <div style="width: 70%;float:right;">
                <h4 v-if="action.type === 'attraction'">{{ action.name }}</h4>
                <p style="margin-left: 1em;text-align: left">{{ action.desc }}</p>
              </div>
            </div>
          </div>
        </div>

        <div>
          <div class="dots">•••</div>
          <div class="action">
            <div style="margin-bottom: 1em">
              <h4>Add</h4>
              <div class="trans">
                <h5>Transport</h5>
                <img :src="require('@/assets/walk.png')" class="transport" @click="AddTrans(index, 'walk')">
                <img :src="require('@/assets/bus.png')" class="transport" @click="AddTrans(index, 'bus')">
                <img :src="require('@/assets/car.png')" class="transport" @click="AddTrans(index, 'car')">
                <img :src="require('@/assets/air.png')" class="transport" @click="AddTrans(index, 'air')">
              </div>

              <div class="trans" style="float: right;min-width: 10em;width: 5em;left: -1.5em;margin-bottom: 2em;margin-right: 0">
                <h5>Destination</h5>
                <form @submit.prevent="addDest(index)">
                  <input v-model="form.name[index]" class="input" type="text" style="max-width: 100%" placeholder="Enter your next destination">
                  <input v-model="form.desc[index]" class="input" type="text" style="max-width: 100%" placeholder="Enter destination desc">
                  <button class="button is-primary" type="submit">Add</button>
                </form>
              </div>
            </div>
          </div>
        </div>

      </div>

      <div class="day">
        <h3 style="text-align:left;font-size: 1.3em">Manage days or changes in this trip</h3>
        <div>
          <div class="action">
            <img v-on:click="addDay()" :src="day_hover ? require('@/assets/day_hover.png') : require('@/assets/plus.png')" class="transport_del" @mouseover="day_hover = true"  @mouseout="day_hover = false">
            <img v-on:click="delDay()" :src="delday_hover ? require('@/assets/delday_hover.png') : require('@/assets/minus.png')" class="transport_del" @mouseover="delday_hover = true"  @mouseout="delday_hover = false">
            <img v-on:click="restoreLast()" :src="res_hover ? require('@/assets/undo_hover.png') : require('@/assets/undo.png')" class="transport_del" @mouseover="res_hover = true"  @mouseout="res_hover = false">
            <img v-on:click="resetTrip()" :src="rest_hover ? require('@/assets/reset_hover.png') : require('@/assets/reset.png')" class="transport_del" @mouseover="rest_hover = true"  @mouseout="rest_hover = false">
          </div>
        </div>
      </div>

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
      form: {
        name: [],
        desc: []
      },
      itinerary: {'actions': {'days': []}},
      loading: true,
      errored: false,
      trans: {
        walk: [],
        bus: [],
        air: [],
        car: []
      },
      walk: false,
      bus: false,
      air: false,
      car: false,
      day_hover: false,
      delday_hover: false,
      res_hover: false,
      rest_hover: false
    }
  },
  created () {
    axios
      .get('http://localhost:5000/trip/' + this.$route.query.id)
      .then(response => (this.itinerary = response.data))
  },
  methods: {
    setTransHL (i, type, hl) {
      if (type === 0) {
        this.trans.walk[i] = hl
      }
    },
    async AddTrans (Day, TransType) {
      let NewTrans
      NewTrans = {'name': '.', 'desc': '.', 'image': 'notre', 'type': TransType, 'duration': '15 minutes'}
      this.itinerary.actions.days[Day].push(NewTrans)
      const requestOptions = {
        method: 'POST',
        body: JSON.stringify(this.itinerary.actions.days)
      }
      const response = await fetch('http://localhost:5000/trip/' + this.$route.query.id + '/' + Day, requestOptions)
      const data = await response.json()
      console.log(data)
    },
    async DeleteLine (Day, Line) {
      this.itinerary.actions.days[Day].splice(Line, 1)
      this.form.name.splice(Line, 1)
      this.form.desc.splice(Line, 1)
      const requestOptions = {
        method: 'POST',
        body: JSON.stringify(this.itinerary.actions.days)
      }
      const response = await fetch('http://localhost:5000/trip/' + this.$route.query.id + '/' + Day, requestOptions)
      const data = await response.json()
      console.log(data)
    },
    handleFocus (Day) {
      alert(Day)
    },
    async addDest (Day, event) {
      let NewTrans
      NewTrans = {'desc': this.form.desc[Day], 'image': 'notre', 'name': this.form.name[Day], 'type': 'attraction'}

      this.itinerary.actions.days[Day].push(NewTrans)
      const requestOptions = {
        method: 'POST',
        body: JSON.stringify(this.itinerary.actions.days)
      }

      const response = await fetch('http://localhost:5000/trip/' + this.$route.query.id + '/' + Day, requestOptions)
      const data = await response.json()
      console.log(data)
      this.form.desc[Day] = ''
      this.form.name[Day] = ''
      // event.preventDefault()
    },
    async addDay () {
      this.itinerary.actions.days.push([])
      const requestOptions = {
        method: 'POST',
        body: JSON.stringify(this.itinerary.actions.days)
      }

      const response = await fetch('http://localhost:5000/trip/' + this.$route.query.id + '/' + this.itinerary.actions.days.length, requestOptions)
      const data = await response.json()
      console.log(data)
      this.form.desc = ''
      this.form.name = ''
    },
    async delDay () {
      if (this.itinerary.actions.days.length > 1) {
        this.itinerary.actions.days.pop()
        const requestOptions = {
          method: 'POST',
          body: JSON.stringify(this.itinerary.actions.days)
        }

        const response = await fetch('http://localhost:5000/trip/' + this.$route.query.id + '/' + this.itinerary.actions.days.length, requestOptions)
        const data = await response.json()
        console.log(data)
      }
    },
    async restoreLast () {
        const response = await fetch('http://localhost:5000/trip/restore/' + this.$route.query.id)
        const data = await response.json()

        axios
        .get('http://localhost:5000/trip/' + this.$route.query.id)
        .then(response => (this.itinerary = response.data))
    },
    async resetTrip () {
        const response = await fetch('http://localhost:5000/trip/reset/' + this.$route.query.id)
        const data = await response.json()

        axios
        .get('http://localhost:5000/trip/' + this.$route.query.id)
        .then(response => (this.itinerary = response.data))
    }
  }
}
</script>

<style>

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

.topbar > .right > .button_menu {
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

.topbar > .right > .button_menu:hover {
  background-color: #F6A526;
  color: black;
  box-shadow: 0 3px 6px 0 rgba(0,0,0,0.09);
  cursor:pointer;
}

.topbar > .right > .button_menu:active {
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
