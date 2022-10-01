<template>
    <div class="row">
        <div class="col-md-12">
        <table class="table table-striped table-bordered">
            <thead>
            <tr>
                <th>ID</th>
                <th>Nombre</th>
                <th>Raza</th>
                <th>FN</th>
                <th>Sexo</th>
                <th>Size</th>
                <th>Estado de adopción</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="mascota in mascotas" :key="mascota.id">
                <td>{{mascota.id}}</td>
                <td>{{mascota.nombre}}</td>
                <td>{{mascota.raza}}</td>
                <td>{{mascota.fecha_n}}</td>
                <td>{{mascota.sexo}}</td>
                <td>{{mascota.size}}</td>
                <td>{{mascota.estado_adop}}</td>
                <td>
                    <!--<div v-if="auth.authorized"></div>-->
                    <!--<router-link class="btn btn-success btn-sm" :to="{ name: 'EditarMascota', params: { mascotaId: mascota.id }}">Editar mascota</router-link>-->
                    <button class="btn btn-danger btn-sm" @click="eliminarMascota(mascota.id)">Eliminar</button>
                </td>
                <td>
                    <router-link class="btn btn-success btn-sm" :to="{ name: 'ApiAdoptar', params: { mascotaId: mascota.id }}">Adoptar mascota</router-link>
                </td>
            </tr>
            </tbody>
        </table>
        </div>
        <div class="nuevaMascota">
            <router-link class="btn btn-success btn-sm" :to="{ name: 'ApiNuevaMascota'}">Nueva mascota</router-link>
        </div>
    </div>
</template>
    
<script>
import axios from 'axios';
//import { auth } from "@/LoginService";
export default {
    el: '#app',
    data() {
    return {
        mascotas: ''
    }},
    mounted(){
        axios.get('http://54.87.191.172:8003/mascotas',
        {headers: {  
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'}
        })
        .then(res => {
            this.mascotas = res.data
            console.log(res)
        })
        .catch(err => {
            console.log(err)
        })
    },
    methods: {
        eliminarMascota(mascotaId) {
            this.axios.delete('ip:8003${mascotaId}',
            {headers: {  
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'}
            })
            .then(res => {
                let i = this.mascotas.map(data => data.id).indexOf(mascotaId);
                this.mascotas.splice(i, 1)
                console.log(res)
            })
            .catch(err => {
                console.log(err)
            })
            }
    }
}

</script>
  