<template>
    <div class="container" id="vuejscrudapp">
        <div class="row">
            <div class="col-md-12 mt-5">
            <h1 class="text-center">Python Flask Vuejs CRUD (Create, Read, Update and Delete) with PHP Mysql</h1>
            <hr>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
            <!-- Add Records -->
            <div>
                <div>
                    <form action="" @submit.prevent="onSubmit">
                    <div class="form-group">
                        <label for="">Nombres</label>
                        <input type="text" v-model="nombres" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="">Apellidos</label>
                        <input type="text" v-model="apellidos" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="">Dni</label>
                        <input type="text" v-model="dni" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="">Correo</label>
                        <input type="text" v-model="correo" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="">Monto</label>
                        <input type="text" v-model="monto" class="form-control">
                    </div>
                    <div class="form-group">
                        <button class="btn btn-sm btn-outline-info">Agregar donacion</button>
                    </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
  </template>
    
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        donaciones: [],
        errors: []
      }
    },
  
    // Fetches posts when the component is created.
    methods: {
            onSubmit(){
                if (this.nombres !== '' && this.apellidos !== '' && this.dni !== '' && this.correo !== '' && this.monto !== '') {
                    var config = { headers: {  
                        'Content-Type': 'application/json',
                        'Access-Control-Allow-Origin': '*'}
                    }
                    axios.post("http://54.82.45.96:8002/donaciones", 
                        { nombres : this.nombres, apellidos : this.apellidos, dni : this.dni, correo : this.correo, monto : this.monto}, config
                    )
                    .then(res => {
                        console.log(res)
                        alert('Donacion agregada exitosamente')
                    })
                    .catch(err => {
                        console.log(err)
                    })
                }else{
                  alert('empty')
                }
            }
        },
           
        mounted: function(){
          //this.getDonacion()
        },
  }
  </script>