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
                <td>{{donacion.monto}}</td>
                <td>{{donacion.correo}}</td>
            </tr>
            </tbody>
        </table>
        </div>
    </div>
</template>
    
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        nombres: '',
        apellidos: '',
        dni: '',
        correo: '',
        monto: '',
        donaciones: [],
        errors: []
      }},
    
    created() {
      axios.get('http://54.87.191.172:8002/donar')
      .then(response => {
        console.log(response)
        // JSON responses are automatically parsed.
        this.donaciones = response.data
      })
      .catch(e => {
        this.errors.push(e)
      })
    }
  }

  </script>
