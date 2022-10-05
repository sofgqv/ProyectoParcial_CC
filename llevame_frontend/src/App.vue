<template>
  <the-navigation />
  <router-view :key="$route.path" />
</template>

<script>
import TheNavigation from "./components/TheNavigation.vue";

export default {
  name: 'App',
  components: {
    TheNavigation
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Poppins');

#app {
  font-family: "Poppins", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
