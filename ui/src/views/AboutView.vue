<script setup>

import axios from 'axios';


axios
  .get('http://localhost:8000/api/agents')
  .then((response) => {
    console.log(response);
  }).catch((error) => {
    console.log(error);
  });

</script>


<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>
