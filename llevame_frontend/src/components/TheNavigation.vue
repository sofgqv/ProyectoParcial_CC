<!DOCTYPE html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
</head>

<template>
  <div class="container">
  <nav class="navbar navbar-expand-lg fixed-top navbar-light bg-light">
    <a class="navbar-brand" href="#">ㅤㅤ
      <img src="https://www.seekpng.com/png/small/321-3215525_blue-penn-state-paw-penn-state-logo-paw.png" width="30" height="30" class="d-inline-block align-top" alt="">
      ¡Llevame pe!
    </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item active">
          <router-link class="nav-link" to="/">Home</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'ApiVerMascotas' }">Mascotas</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'ApiSerVoluntario' }">Ser Voluntario</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'ApiDonar' }">Donar</router-link>
        </li>
        <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'ApiVerAdopciones' }">Adopciones</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'ApiDonaciones' }">Donaciones</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'ApiVerVoluntarios' }">Voluntarios</router-link>
        </li>
      </ul>
    </div>
  </nav>
  </div>
<!--
  <nav class="navbar fixed-top navbar-expand-lg navbar-light bg-light">
    <router-link to="/">Home</router-link>
    <router-link :to="{ name: 'ApiVerMascotas' }">Mascotas</router-link>
    <router-link :to="{ name: 'ApiSerVoluntario' }">Ser Voluntario</router-link>
    <router-link :to="{ name: 'ApiDonar' }">Donar</router-link>
    <!-<div v-if="auth.authorized">->
    <router-link :to="{ name: 'ApiVerAdopciones' }">Adopciones</router-link>
    <router-link :to="{ name: 'ApiDonaciones' }">Donaciones</router-link>
    <router-link :to="{ name: 'ApiVerVoluntarios' }">Voluntarios</router-link>
    <!-</div>->
  </nav>
-->
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
  background-color: #ffee00;
}
nav a {
  font-weight: bold;
  color: #293a4a;
}
nav a.router-link-exact-active {
  color: #ff0000;
}
div {
  color: #ffee00;
}

</style>