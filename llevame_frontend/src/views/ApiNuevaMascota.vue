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
            <h1 class="text-center">Nueva mascota</h1>
            <hr>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
            <!-- Add Records -->
            <div>
                <h4 id="show-btn" @click="showModal('my-modal')">¡Registro de mascotas!</h4>
    
                <div ref="my-modal" hide-footer title="nueva mascota">
                <div>
                    <form action="" @submit.prevent="onSubmit">
                    <div class="form-group">
                        <label for="">Nombre</label>
                        <input type="text" v-model="nombre" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="">Raza</label>
                        <input type="text" v-model="raza" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="">Fecha de nacimiento</label>
                        <input type="text" v-model="fecha_n" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="">Sexo</label>
                        <input type="text" v-model="sexo" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="">Size</label>
                        <input type="text" v-model="size" class="form-control">
                    </div>
                    <div class="form-group">
                        <button class="btn btn-sm btn-outline-info">Añadir</button>
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
      nombre: '',
      raza: '',
      fecha_n: '',
      sexo: '',
      size: '',
      errors: []
    }},
  methods: {
    onSubmit(){
      if (this.nombre !== '' && this.raza !== '' && this.fecha_n !== '' && this.sexo !== '' && this.size !== '') {
        axios.post("http://34.230.89.209:8003/mascotasadd",{
          nombre : this.nombre,
          raza : this.raza,
          fecha_n : this.fecha_n,
          sexo : this.sexo,
          size : this.size
        },
        {headers: {  
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'}
        })
        .then(res => {
            console.log(res)
            alert('¡Mascota añadida!')
        })
        .catch(err => {
            console.log(err)
        })
      }else{
        alert('No se pudo añadir. Inténtalo nuevamente.')
      }
    }
  }
}

</script>
