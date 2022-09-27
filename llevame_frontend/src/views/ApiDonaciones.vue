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
                <b-button id="show-btn" @click="showModal('my-modal')">Agregar donacion</b-button>
    
                <b-modal ref="my-modal" hide-footer title="Agregar donacion">
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
                <b-button class="mt-3" variant="outline-danger" block @click="hideModal('my-modal')">Cierrame</b-button>
                </b-modal>
            </div>
        </div>
        
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
    methods: {
            showModal(id) {
                this.$refs[id].show()
            },
            hideModal(id) {
                this.$refs[id].hide()
            },
  
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
                        this.nombres = ''
                        this.apellidos = ''
                        this.dni = ''
                        this.correo = ''
                        this.monto = ''
          
                        this.hideModal('my-modal')
                        this.getDonacion()
                    })
                    .catch(err => {
                        console.log(err)
                    })
                }else{
                  alert('empty')
                }
            },
  
            getDonacion(){
                axios({
                  url: 'http://54.82.45.96:8002/donar',
                  method: 'get'
                })
                .then(res => {
                  console.log(res)
                  this.donaciones = res.data.members
                })
                .catch(err => {
                  console.log(err)
                })
            },
         
        },
           
        mounted: function(){
          this.getDonacion()
        },
    // Fetches posts when the component is created.
    created() {
      axios.get(``)
      .then(response => {
        // JSON responses are automatically parsed.
        this.mascotas = response.data
      })
      .catch(e => {
        this.errors.push(e)
      })
    }
  }

  </script>
