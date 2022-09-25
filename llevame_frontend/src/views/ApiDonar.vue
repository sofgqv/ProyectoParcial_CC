<!--
<template>
  <div>
    <input type="text" v-model="postBody" @change="postPost()" />
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
  name: 'ApiDonar',
  data() {
    return {
      postBody: '',
      errors: []
    }
  },

  methods: {
    // Pushes posts to the server when called.
    postPost() {
      axios.post(``, {
        body: this.postBody
      })
      .then(response => {})
      .catch(e => {
        this.errors.push(e)
      })
    }
  }
}
</script>
-->