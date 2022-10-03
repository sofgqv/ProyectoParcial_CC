<template>
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <link type="text/css" rel="stylesheet" href="https://unpkg.com/bootstrap/dist/css/bootstrap.min.css" />
      <link type="text/css" rel="stylesheet" href="https://unpkg.com/bootstrap-vue@latest/dist/bootstrap-vue.min.css" />
    </head>
  
      <div class="container" id="vuejscrudapp">
          <div class="row">
              <div class="col-md-3">
              </div>
              <div class="col-md-6">
              <!-- Add Records -->
              <div>
                <br>
                  <h4 id="show-btn" @click="showModal('my-modal')">¡Tu contribución es importante!</h4>
                  <br>
                  <div ref="my-modal" hide-footer title="unete">
                  <div>
                      <form action="" @submit.prevent="onSubmit">
                      <div class="form-group">
                          <label for="">Nombres</label>
                          <input type="text" v-model="nombres" class="form-control">
                          <br>
                      </div>
                      <div class="form-group">
                          <label for="">Apellidos</label>
                          <input type="text" v-model="apellidos" class="form-control">
                          <br>
                      </div>
                      <div class="form-group">
                          <label for="">DNI</label>
                          <input type="text" length="8" v-model="dni" class="form-control">
                          <br>
                      </div>
                      <div class="form-group">
                          <label for="">Correo</label>
                          <input type="text" v-model="correo" class="form-control">
                          <br>
                      </div>
                      <div class="form-group">
                          <label for="">Monto</label>
                          <input type="int" v-model="monto" class="form-control">
                          <br>
                      </div>
                      <br>
                      <div class="form-group">
                          <button class="btn btn-sm btn-outline-info">Donar</button>
                      </div>
                      </form>
                  </div>
                </div>
              </div>
          </div>
          <div class="col-md-3">
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
      errors: []
    }},
  methods: {
    onSubmit(){
      if (this.nombres !== '' && this.apellidos !== '' && this.dni !== '' && this.correo !== '' && this.monto !== '') {
        axios.post("http://52.207.240.235:8002/donar",{
          nombres : this.nombres,
          apellidos : this.apellidos,
          dni : this.dni,
          correo : this.correo,
          monto : this.monto
        },
        {headers: {  
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'}
        })
        .then(res => {
            console.log(res)
            alert('¡Gracias por donar!')
        })
        .catch(err => {
            console.log(err)
        })
      }else{
        alert('Donación no procesada. Inténtalo nuevamente.')
      }
    }
  }
}

</script>
  