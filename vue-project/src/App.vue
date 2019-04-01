<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
  export default {
    name: 'App'
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    /*margin-top: 60px;*/
  }

  body {
    background-color: #fff;
    color: #2d2d2d;
    -webkit-font-smoothing: antialiased;
    max-width: 640px;
    margin: 0 auto;
  }
  a{
    color: #000;
  }
</style>
