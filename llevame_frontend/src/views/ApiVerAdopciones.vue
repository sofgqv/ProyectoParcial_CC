<template>
    <div class="row">
        <div class="col-md-12">
        <table class="table table-striped table-bordered">
            <thead>
            <tr>
                <th>ID</th>
                <th>Nombres</th>
                <th>Apellidos</th>
                <th>DNI</th>
                <th>FechaN</th>
                <th>Celular</th>
                <th>Correo</th>
                <th>IDM</th>
                <th>Aceptado</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="adopcion in adopciones" :key="adopcion.id">
                <td>{{adopcion.id}}</td>
                <td>{{adopcion.nombres}}</td>
                <td>{{adopcion.apellidos}}</td>
                <td>{{adopcion.dni}}</td>
                <td>{{adopcion.fecha_n}}</td>
                <td>{{adopcion.celular}}</td>
                <td>{{adopcion.correo}}</td>
                <td>{{adopcion.mascota_id}}</td>
                <td>
                    <input type="checkbox" v-model.number="adopcion.aceptado" @click="editarAceptado(adopcion.id, adopcion.aceptado)" :true-value=1 :false-value=0>
                </td>
            </tr>
            </tbody>
        </table>
        </div>
  </div>
</template>
  
<script>
    import axios from 'axios';
    
    export default {
        el: '#app',
        data() {
        return {
            adopciones: ''
        }},
        mounted(){
            axios.get('http://34.230.89.209:8003/adoptar',
            {headers: {  
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'}
            })
            .then(res => {
                this.adopciones = res.data
                console.log(res)
            })
            .catch(err => {
                console.log(err)
            })
        },
        methods: {
        editarAceptado(id, value) {
            axios.patch('http://34.230.89.209:8003/adoptarestado/' + id ,{
            aceptado : value
          },
            {headers: {  
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'}
            })
            .then(res => {
                console.log(res)
            })
            .catch(err => {
                console.log(err)
            })
            }
    }
    }
    
    </script>
