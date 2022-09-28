<template>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link type="text/css" rel="stylesheet" href="https://unpkg.com/bootstrap/dist/css/bootstrap.min.css" />
    <link type="text/css" rel="stylesheet" href="https://unpkg.com/bootstrap-vue@latest/dist/bootstrap-vue.min.css" />
  </head>

    <div class="container" id="vuejscrudapp">
        <div class="row">
            <div class="col-md-12 mt-5">
            <h1 class="text-center">Ser Voluntario</h1>
            <hr>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
            <!-- Add Records -->
            <div>
                <h4 id="show-btn" @click="showModal('my-modal')">¡Únete a nosotros!</h4>
    
                <div ref="my-modal" hide-footer title="unete">
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
                        <label for="">Actividad</label>
                        <select v-model="actividad" class="form-control">
                            <option value="entrega de donaciones">Entrega de donaciones</option>
                            <option value="redes sociales">Manejo de redes sociales</option>
                            <option value="embajador">Ser embajador</option>
                          </select>
                    </div>
                    <div class="form-group">
                        <button class="btn btn-sm btn-outline-info">Inscribirme</button>
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
  data() {
    return {
      nombres: '',
      apellidos: '',
      dni: '',
      fecha_n: '',
      celular: '',
      actividad: '',
      errors: []
    }},
  methods: {
    onSubmit(){
      if (this.nombres !== '' && this.apellidos !== '' && this.dni !== '' && this.fecha_n !== '' && this.celular !== '' && this.actividad !== '') {
        axios.post("http://54.82.45.96:8001/servoluntarios",{
          nombres : this.nombres,
          apellidos : this.apellidos,
          dni : this.dni,
          fecha_n : this.fecha_n,
          celular : this.celular,
          actividad : this.actividad
        },
        {headers: {  
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'}
        })
        .then(res => {
            console.log(res)
            alert('¡Gracias por inscribirte!')
        })
        .catch(err => {
            console.log(err)
        })
      }else{
        alert('Inscripción no funcionó. Inténtalo nuevamente.')
      }
    }
  }
}

</script>
