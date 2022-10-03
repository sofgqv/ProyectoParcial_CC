<template>
    <div class="row">
        <div class="col-md-12">
        <table class="table table-striped table-bordered">
            <thead>
            <tr>
                <th>ID</th>
                <th>Nombres</th>
                <th>Apellidos</th>
                <th>Dni</th>
                <th>Correo</th>
                <th>Monto</th>
            </tr>
            </thead>
            <tbody>
                <tr v-for="donacion in donaciones" :key="donacion.id">
                <td>{{donacion.id}}</td>
                <td>{{donacion.nombres}}</td>
                <td>{{donacion.apellidos}}</td>
                <td>{{donacion.dni}}</td>
                <td>{{donacion.correo}}</td>
                <td>{{donacion.monto}}</td>
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
        donaciones: ''
    }},
    mounted(){
        axios.get('http://lb-prod-632583897.us-east-1.elb.amazonaws.com:8002/donaciones',
        {headers: {  
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'}
        })
        .then(res => {
            this.donaciones = res.data
            console.log(res)
        })
        .catch(err => {
            console.log(err)
        })
    }
}

</script>
