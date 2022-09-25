<!--
  <template>
  <div>
    <ul v-if="donaciones && donaciones.length">
      <li v-for="donacion of donaciones">
        <p><strong>{{donacion.monto}}</strong></p>
        <p>{{donacion.nombres}}</p>
        <p>{{donacion.apellidos}}</p>
      </li>
    </ul>

    <ul v-if="errors && errors.length">
      <li v-for="error of errors">
        {{error.message}}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name : 'ApiVerDonaciones',
  data() {
    return {
      donaciones: [],
      errors: []
    }
  },

  // Fetches posts when the component is created.
  created() {
    axios.get(``)
    .then(response => {
      this.donaciones = response.data
    })
    .catch(e => {
      this.errors.push(e)
    })
  }
}
</script>
-->