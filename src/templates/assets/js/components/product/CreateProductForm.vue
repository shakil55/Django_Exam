<template>
    <section>
      <div v-for="variant in variants" :key="variant.id">
        <label>{{ variant.title }}</label>
        <input type="text" v-model="variant.value">
      </div>
    </section>
  </template>
  
  <script>
  export default {
    props: {
      variants: {
        type: Array,
        required: true
      }
    },
    data() {
      return {
    
      }
    },
    methods: {
      
    }
  }
  </script>