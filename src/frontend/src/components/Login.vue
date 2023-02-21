<!-- Autor: xhomol28, Edit: xhorky32 -->
<template>
    <div class="log" id="login">
        <h1>Traveller bucket list app</h1>
        <hr>
        <div class="rows_txt">
          <p>Please enter your login credentials.</p>
        </div>
        <br>
      <div class="rows">
        <input id="i1" type="text" name="username" v-model="input.username" placeholder="Username" />
        <input id="i2" type="password" name="password" v-model="input.password" placeholder="Password" />
        <button type="button" v-on:click="login()">Login</button>
      </div>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <br><br><br><br><br><br>
        <div id="imsg"></div>
        <h4>Don't have an account? Register <a @click="reg_screen()">here</a>.</h4>
    </div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      input: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    login () {
      if (this.input.username !== '' && this.input.password !== '') {
        if (this.input.username === this.$parent.mockAccount.username && this.input.password === this.$parent.mockAccount.password) {
          this.$emit('authenticated', true)
          this.$router.replace({ name: 'Home' })
        } else {
          console.log('The username or password is incorrect')
          document.getElementById('imsg').innerHTML = '<br>The username or password is incorrect'
          return false
        }
      } else {
        console.log('A username and password must be present')
        document.getElementById('imsg').innerHTML = '<br>A username and password must be present!'
      }
    },

    reg_screen () {
      this.$emit('registerPending', true)
      this.$router.replace({ name: 'Register' })
    }
  }
}
</script>

<style scoped>
    @viewport {
        width: device-width;
        zoom: 1.0;
}
  /* Error message after wrong input */
    #imsg {
        color: #e83f3f;
        font-weight: bold;
        padding-bottom: 10px;
    }
    /* Login container styling */
    #login {
        border: 5px solid #ac733950;
        border-radius: 25px;
        background-color: #dfbf9ff0;
        background-opacity: 10%;
        margin-left: auto;
        margin-right: auto;
        position: fixed;
        top: 50%;
        left:50%;
        transform: translate(-50%, -50%);
        width: 390px;
        padding: 20px;
        padding-left: 30px;
        padding-right: 30px;
        padding-bottom: 5px;
        padding-top: 10px;
        background-size: cover;
    }

    .log > .rows_txt {
      text-align: center;
      align: center;
    }

    a {
      cursor:pointer;
      color: #000022;
    }

    .log > .rows_txt > p {
        display: inline;
        color: #000033;
      }

    .log > .reg > h4 {
        text-align: left;
    }

    .log > .rows > input {
        padding: 14px 30px;
        border: 2px solid #ac7339c0;
        background-color: rgb(255,255,255,200);
        border-radius: 9px;
        margin-bottom: 8px;
        float: left;
    }

    /* BUTTON STYLING */
    button {
        background: linear-gradient(to bottom right, #EF4765, #FF9A5A);
        border: 0;
        border-radius: 12px;
        color: #FFFFFF;
        cursor: pointer;
        display: inline-block;
        font-family: -apple-system,system-ui,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
        font-size: 20px;
        font-weight: 500;
        line-height: 2.5;
        outline: transparent;
        padding: 0 3rem;
        text-align: center;
        touch-action: manipulation;
        white-space: nowrap;
        float: right;
      }

    button:not([disabled]):focus {
        box-shadow: 0 0 .25rem rgba(0, 0, 0, 0.5), -.125rem -.125rem 1rem rgba(239, 71, 101, 0.5), .125rem .125rem 1rem rgba(255, 154, 90, 0.5);
      }

    button:not([disabled]):hover {
        box-shadow: 0 0 .25rem rgba(0, 0, 0, 0.5), -.125rem -.125rem 1rem rgba(239, 71, 101, 0.5), .125rem .125rem 1rem rgba(255, 154, 90, 0.5);
      }
    .log > .rows{
      position: relative;
      display: block;
      margin: auto;
      text-align: center;
    }

    .log > .rows_login {
      position: relative;
      display: block;
      margin: none;
      text-align: right;
    }

  body {
    background-image: url('../assets/home_bg.png');
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
  }

  #login {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
