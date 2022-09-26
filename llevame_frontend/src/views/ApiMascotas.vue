<template>
  <div>
    <ul v-if="mascotas">
      <li v-for="mascota of mascotas" :key="mascota">
        <p><strong>{{mascota.title}}</strong></p>
        <p>{{mascota.body}}</p>
      </li>
    </ul>

    <ul v-if="errors && errors.length">
      <li v-for="error of errors" :key="error">
        {{error.message}}
      </li>
    </ul>
  </div>
</template>
  
<script>
import axios from 'axios';

export default {
  data() {
    return {
      mascotas: [],
      errors: []
    }
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
