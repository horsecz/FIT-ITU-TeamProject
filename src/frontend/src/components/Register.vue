<!-- Autor: xhorky32 -->
<template>
    <div class="log" id="login">
        <h1>New account registration</h1>
        <hr>
        <div class="rows_txt">
          <p>Please enter all credentials to create a new account.</p>
        </div>
        <br>
      <div class="rows">
        <input id="i1" type="search" name="newuser" v-model="input.newuser" placeholder="New username" />
        <br>
        <input id="i2" type="password" name="newpassword" v-model="input.newpassword" placeholder="Password" />
        <br>
        <input id="i3" type="password" name="repeatpassword" v-model="input.repeatpassword" placeholder="Password again" />
        <button type="button" v-on:click="reg()">Register</button>
      </div>
      <div id="imsg"></div>
        <meta name="viewport" content="width=device-width, initial-scale=1">
      <div class="reg">
        <h4>Already have an account? Log in <a @click="log_screen()">here</a>!</h4>
      </div>
    </div>
</template>

<script>
export default {
  name: 'Register',
  data () {
    return {
      input: {
        newuser: '',
        newpassword: '',
        repeatpassword: ''
      }
    }
  },
  methods: {
    log_screen () {
      this.$emit('registerPending', false)
      this.$router.replace({ name: 'login' })
    },
    reg () {
      if (this.input.newuser !== '' && this.input.newpassword !== '' && this.input.repeatpassword !== '') {
        if (this.input.newuser === this.$parent.mockAccount.username) {
          document.getElementById('imsg').innerHTML = '<br>This user already exists!'
          return false
        } else if (this.input.newpassword !== this.input.repeatpassword) {
          document.getElementById('imsg').innerHTML = '<br>Passwords does not match!'
          return false
        } else {
          this.$parent.mockAccount.username = this.input.newuser
          this.$parent.mockAccount.password = this.input.newpassword
          this.$emit('authenticated', true)
          this.$router.replace({ name: 'Home' })
          console.log('New account created.')
          return true
        }
      } else {
        console.log('A username and password must be present')
        document.getElementById('imsg').innerHTML = '<br>You have to enter all credentials in order to register!'
      }
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
        padding-bottom: 20px;
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
        width: 420px;
        padding: 20px;
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
        display: inline;
    }

    input {
        padding: 14px 30px;
        border: 2px solid #ac7339c0;
        background-color: rgb(255,255,255,200);
        border-radius: 9px;
        margin-bottom: 9px;
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
      text-align: left;
    }

    .log > .rows_login {
      position: relative;
      display: block;
      margin: auto;
      text-align: center;
    }

    body {
      background-image: url('../assets/home_bg.png');
      background-repeat: no-repeat;
      background-attachment: fixed;
      background-position: center;
    }
</style>
