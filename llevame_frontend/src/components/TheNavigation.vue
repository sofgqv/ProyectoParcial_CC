<!DOCTYPE html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
</head>

<template>
  <nav>
    <router-link to="/">Home</router-link> | 
    <router-link :to="{ name: 'ApiMascotas' }">Mascotas</router-link> | 
    <router-link :to="{ name: 'ApiAdoptar' }">Adoptar</router-link> | 
    <router-link :to="{ name: 'ApiSerVoluntario' }">Ser Voluntario</router-link> | 
    <!--<router-link :to="{ name: 'ApiDonar' }">Donar</router-link>-->
    <!--<div v-if="auth.authorized">-->
      | <router-link :to="{ name: 'ApiAdopciones' }">Adopciones</router-link>
      | <router-link :to="{ name: 'ApiDonaciones' }">Donaciones</router-link>
    <!--</div>-->
  </nav>
</template>

<script>/*
import { auth } from "@/LoginService";
export default {
  name: "TheNavigation",
  data() {
    return {
      auth,
    };
  },
};*/
</script>

<style>
nav {
  padding: 30px;
}
nav a {
  font-weight: bold;
  color: #2c3e50;
}
nav a.router-link-exact-active {
  color: #42b983;
}
</style>