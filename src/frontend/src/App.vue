<template>
  <div id="app">
    <router-view @image="setbg" @authenticated="setAuthenticated" @registerPending="setRegister" @changeMockAccount="changeAcc" />
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      authenticated: false,
      registerPending: false,
      mockAccount: {
        username: 'test',
        password: 'test',
        public: false
      }
    }
  },
  mounted () {
    if (!this.authenticated || !this.registerPending) {
      this.$router.replace({ name: 'login' })
    }
    if (this.registerPending) {
      this.$router.replace({ name: 'Register' })
    }
  },
  methods: {
    setAuthenticated (status) {
      this.authenticated = status
    },
    logout () {
      this.authenticated = false
    },
    setRegister (status) {
      this.registerPending = status
    },
    changeAcc (up, value) {
      this.mockAccount.up = value
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

body {
  background-image: url('./assets/home_bg.png');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-position: center;
}

a {
  color: #ff0000;
  text-color: #ff0000;
}
</style>
