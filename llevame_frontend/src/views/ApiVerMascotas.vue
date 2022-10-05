<template>
    <div class="row justify-content-center">
        <div class="col-3" style="margin:10px" v-for="mascota in mascotas" :key="mascota.id">
            <div class="card">
                <div class="card-header">{{mascota.nombre}}</div>
                <div class="card-body">
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item"><b>Raza: </b>{{mascota.raza}}</li>
                        <li class="list-group-item"><b>Nacimiento: </b>{{mascota.fecha_n}}</li>
                        <li class="list-group-item"><b>Sexo: </b>{{mascota.sexo}}</li>
                        <li class="list-group-item"><b>Tamaño: </b>{{mascota.size}}</li>
                        <li class="list-group-item"><b>Adopción: </b>
                            <p v-if="mascota.estado_adop = 1">Sí</p>
                            <p v-else>No</p>
                        </li>
                    </ul>
                    <router-link class="btn btn-success btn-sm" :to="{ name: 'ApiAdoptar', params: { new_mascota_id: mascota.id }}">Adoptar mascota</router-link>
                    <button class="btn btn-danger btn-sm" @click="eliminarMascota(mascota.id)">Eliminar</button>
                </div>
            </div>
        </div>
    </div>
    <div class="nuevaMascota">
        <router-link class="btn btn-success btn-sm" :to="{ name: 'ApiNuevaMascota'}">Nueva mascota</router-link>
    </div> 
</template>
        
    <script>
    import router from "@/router";
    import axios from 'axios';
    //import { auth } from "@/LoginService";
    export default {
        el: '#app',
        data() {
        return {
            mascotas: {}
        }},
        mounted(){
            axios.get('http://lb-prod-632583897.us-east-1.elb.amazonaws.com:8003/mascotas',
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
            eliminarMascota(mascota_id) {
                axios.delete('http://lb-prod-632583897.us-east-1.elb.amazonaws.com:8003/mascota/' + mascota_id ,
                {headers: {  
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'}
                })
                .then(res => {
                    console.log(res)
                    router.push("/");
                })
                .catch(err => {
                    console.log(err)
                })
                }
        }
    }

    </script>
      
    <style>
        .card-deck{
            margin-bottom: 10px;
            width: 18rem;
        }
    </style>