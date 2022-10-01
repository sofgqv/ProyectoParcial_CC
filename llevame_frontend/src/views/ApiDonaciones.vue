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
            <tr v-for="(donacion, i) in donaciones" :key="donacion.id">
                <td>{{i + 1}}</td>
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
      donaciones: '',
      errors: []
  }},
  mounted(){
      axios.get('http://34.230.89.209:8002/donaciones',
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
