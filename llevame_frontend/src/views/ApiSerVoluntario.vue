<template>
    <div class="container" id="vuejscrudapp">
        <div class="row">
            <div class="col-md-12 mt-5">
            <h1 class="text-center">Voluntarios</h1>
            <hr>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
            <!-- Add Records -->
            <div>
                <b-button id="show-btn" @click="showModal('my-modal')">¡Únete a nosotros!</b-button>
    
                <b-modal ref="my-modal" hide-footer title="unete">
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
                        <label for="">DNI</label>
                        <input type="text" v-model="dni" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="">Fecha de nacimiento</label>
                        <input type="text" v-model="fecha_n" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="">Celular</label>
                        <input type="text" v-model="celular" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="">Actividad</label>
                        <select name="cars" v-model="actividad" class="form-control">
                            <option value="entrega de donaciones">Entrega de donaciones</option>
                            <option value="redes sociales">Manejo de redes sociales</option>
                            <option value="embajador">Ser embajador</option>
                          </select>
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
                    axios.post("http://54.82.45.96:8001/servoluntarios", 
                        { nombres : this.nombres, apellidos : this.apellidos, dni : this.dni, correo : this.correo, monto : this.monto}, config
                    )
                    .then(res => {
                        console.log(res)
                        alert('¡Gracias por inscribirte!')
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
            }
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
