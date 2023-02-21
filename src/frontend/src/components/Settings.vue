<!-- Autor: xhomol28, Edit: xhorky32 -->
<template>
 <root>
   <meta name="viewport" content="width=device-width, initial-scale=1" />
   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <topbar>
     <div class="topbar">
        <img class="icon" src="../assets/logo.png" onclick="window.location.href='http://localhost:8080/#/Home'">
        <h1>TravelPlanApp</h1>
        <h2><a onclick="window.location.href='http://localhost:8080/#/Home'">Home</a> > Settings</h2>
            <div class="logout" onclick="window.location.href='http://localhost:8080/#/Login'"></div>
            <div class="settings" onclick="window.location.href='http://localhost:8080/#/Settings'"></div>
           <button class="button_menu" onclick="window.location.href='http://localhost:8080/#/NewTrip'">Plan new trip</button>
     </div>
    </topbar>
    <br> <br>
     <h1>Change your account password or profile status</h1>
    <div class="set" id="nastaveni">
      <h2>Set new password</h2>
      <hr>
      <p>Enter your current password and then new password twice. If you wanna change your profile publicity, click on button below.</p>
      <p>You need to click confirm after every change you made!</p>
        <div>
        <div id="pw">
        <section class="container">
                <div class="control is-expanded">
                  <input name="currpass" id="currpass" v-if="showPassword" type="text" class="input" v-model="input.currpass"  />
                  <input name="currpass" id="currpass" v-else type="password" class="input" v-model="input.currpass" placeholder="Current password">
                </div>
                <div class="control">
                    <button class="button" @click="toggleShow1"><span class="icon is-small is-right">
                        <i style="font-size:20px" class="fa">&#xf06e;</i>
                </span>
                    </button>
                </div>
        </section>
        <section class="container">
                <div class="control is-expanded">
                  <input name="password" id="password" v-if="showPassword" type="text" class="input" v-model="input.password"  />
                  <input name="password" id="password" v-else type="password" class="input" v-model="input.password" placeholder="New password">
                </div>
        </section>
        <section class="container">
                <div class="control is-expanded">
                <input name="repeat" id="repeat" v-if="showPassword" type="text" class="input" v-model="input.repeat"  />
                <input name="repeat" id="repeat" v-else type="password" class="input" v-model="input.repeat" placeholder="Repeat new password">
                </div>
        </section>
              <button type="button" v-on:click="set()" class="confirm">CONFIRM</button>
            </div>
        </div>
        <div>
            <h2> Public profile: </h2>
            <label class="switch">
                <input name="public" id="public" v-model="input.pcheck" type="checkbox">
                <span class="slider round"></span>
            </label>
        </div>
    </div>
    <h2><br><div id="succText" class="succText"></div></h2>
    <meta name="viewport" content="width=device-width, initial-scale=1">
 </root>
</template>

<script>
export default {
  data () {
    return {
      showPassword: false,
      password: null,
      input: {
        currpass: '',
        newpassword: '',
        repeat: '',
        pcheck: this.$parent.mockAccount.public
      }
    }
  },
  computed: {
    buttonLabel () {
      return (this.showPassword) ? 'Hide' : 'Show'
    }
  },
  methods: {
    toggleShow1 () {
      this.showPassword = !this.showPassword
    },
    set () {
      var x = false
      if (this.input.password !== '' && this.input.repeat !== '' && this.input.currpass !== '') {
        x = true
        if (this.input.currpass === this.$parent.mockAccount.password) {
          if (this.input.password === this.input.repeat) {
            if (this.input.password !== this.$parent.mockAccount.password) {
              this.$parent.mockAccount.password = this.input.password
              document.getElementById('succText').innerHTML = '<div class="succTextC">Password changed.</div>'
            } else {
              document.getElementById('succText').innerHTML = '<div class="succTextC">New password is same as old one. Nothing changed.</div>'
            }
          } else {
            document.getElementById('succText').innerHTML = '<div class="succTextC">Passwords does not match.</div>'
          }
        } else {
          document.getElementById('succText').innerHTML = '<div class="succTextC">You have entered wrong current password.</div>'
        }
      }
      if (this.input.pcheck !== this.$parent.mockAccount.public) {
        this.$parent.mockAccount.public = this.input.pcheck
        if (x) {
          document.getElementById('succText').innerHTML += '<br><div class="succTextC">Profile status updated.</div>'
        } else {
          document.getElementById('succText').innerHTML = '<div class="succTextC">Profile status updated.</div>'
        }
      }
      document.getElementById('succText').innerHTML += '</div>'
    }
  }
}
</script>

<style>

body{
  background-image: url('../assets/home_bg.png');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-position: center;
}

  .succTextC {
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
  /********************************* */

  /* SETTING container */
  #nastaveni{
    display: center;
    flex-wrap:wrap;
    text-align:center;
    margin:0px auto;
    padding-left: 15px;
    padding-right: 15px;
    width: 300px;
    font-size:12px;
    color:black;
    border: 1px solid rgb(134, 134, 134, 200);
    border-radius: 12px;
    background: linear-gradient(to bottom, #ffffffee 0%, #e0e0ebdd 100%);
    align: center;
  }

  #nastaveni > div{
    display: flex;
    flex-direction: row;
    padding-top: 20px;
    float: center;
  }

  #pw{
      display: flex;
      flex-direction: column;
  }

  #pw > .confirm {
    background-color: #F49516;
    color: black;
    padding: 13px;
    text-align: center;
    text-decoration: none;
    font-size: 16px;
    transition-duration: 0.1s;
    margin-top: 20px;
    margin-bottom: 10px;
    margin-right: -1em;
    margin-left: 4.5em;
    border: 1px solid orange;
    box-shadow: 0 3px 4px 0 rgba(0,0,0,0.08);
    border-radius: 10px;
  }

  #pw > .confirm:hover{
    background-color: #F6A526;
    color: black;
    box-shadow: 0 3px 6px 0 rgba(0,0,0,0.09);
    cursor:pointer;
  }

  .container{
      display: flex;
      flex-direction: row;
      margin-bottom:11px;
  }

  .control.is-expanded > .input{
      height: 2.9em;
      border-radius: 5px;
      margin-right: 5px;
      margin-left: 0px;
      width: 170px;
  }

  #nastaveni > div > h2{
    margin-top: 10px;
    padding-right: 10px;
    align-items: center;
  }

  #nastaveni > div > input{
    height: 3em;
    border-radius: 5px;
  }

  .control > .button {
      height: 3em;
      margin-bottom: 15px;
  }

    .set > .h1 {
    text-align: center;
  }

  .set > .txt {
    text-align: center;
    text-color: red;
    text-decoration: bold;
  }

  /* SLIDER STYLING */
   /* The switch - the box around the slider */
.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

/* The slider */
.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ffd480;
  -webkit-transition: .4s;
  transition: .4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
}

input:checked + .slider {
  background-color: #ff9900;
}

input:focus + .slider {
  box-shadow: 0 0 1px #ff9900;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
}

.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}
</style>
