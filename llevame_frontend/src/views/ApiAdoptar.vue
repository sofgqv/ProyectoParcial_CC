<template>
    <div class="container" id="vuejscrudapp">
      <br>
        <div class="row">
            <div class="col-md-12 mt-5">
            <h1 class="text-center">Adoptar</h1>
            <hr>
            </div>
        </div>
        <div class="row">
          <div class="col-md-3">
          </div>
            <div class="col-md-6">
            <!-- Add Records -->
            <div>
                <h4 id="show-btn" @click="showModal('my-modal')">¡No adoptes uno de raza, adopta uno sin casa!</h4>
    
                <div ref="my-modal" hide-footer title="adoptar">
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
                        <input type="text" length="8" v-model="dni" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="">Fecha de nacimiento</label>
                        <input type="date" v-model="fecha_n" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="">Celular</label>
                        <input type="text" v-model="celular" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="">Correo</label>
                        <input type="text" v-model="correo" class="form-control">
                    </div>
                    <div class="form-group">
                        <button class="btn btn-sm btn-outline-info">Solicitar adopción</button>
                    </div>
                    </form>
                </div>
              </div>
            </div>
        </div>
    </div>
</div>
</template>
    
<script>
import axios from 'axios';

export default {
  props: {
    new_mascota_id: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      nombres: '',
      apellidos: '',
      dni: '',
      fecha_n: '',
      celular: '',
      correo: '',
      errors: []
    }},
  methods: {
    onSubmit(){
      if (this.nombres !== '' && this.apellidos !== '' && this.dni !== '' && this.fecha_n !== '' && this.celular !== '' && this.correo !== '') {
        axios.post("http://lb-prod-632583897.us-east-1.elb.amazonaws.com:8003/adoptar" ,{
          nombres : this.nombres,
          apellidos : this.apellidos,
          dni : this.dni,
          fecha_n : this.fecha_n,
          celular : this.celular,
          correo : this.correo,
          mascota_id : this.new_mascota_id,
        },
        {headers: {  
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'}
        })
        .then(res => {
            console.log(res)
            alert('¡Gracias por solicitar una adopción!')
        })
        .catch(err => {
            console.log(err)
        })
      }else{
        alert('Solicitud no enviada. Inténtalo nuevamente.')
      }
    }
  }
}

</script>
