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
        mascotas: ''
    }},
    mounted(){
        axios.get('',
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
    }
}

</script>
  