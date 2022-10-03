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
                <th>FN</th>
                <th>Celular</th>
                <th>Actividad</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="voluntario in voluntarios" :key="voluntario.id">
                <td>{{voluntario.id}}</td>
                <td>{{voluntario.nombres}}</td>
                <td>{{voluntario.apellidos}}</td>
                <td>{{voluntario.dni}}</td>
                <td>{{voluntario.fecha_n}}</td>
                <td>{{voluntario.celular}}</td>
                <td>{{voluntario.actividad}}</td>
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
        voluntarios: ''
    }},
    mounted(){
        axios.get('http://lb-prod-632583897.us-east-1.elb.amazonaws.com:8001/servoluntario',
        {headers: {  
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'}
        })
        .then(res => {
            this.voluntarios = res.data
            console.log(res)
        })
        .catch(err => {
            console.log(err)
        })
    }
}

</script>
  