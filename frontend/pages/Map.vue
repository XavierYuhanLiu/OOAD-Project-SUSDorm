<!-- App.vue -->
<template>
  <div id="app" class="flex-container">
    <div>
      <choose />
    </div>
    <div class="flex-item">
        <AMapTest />
    </div>
  </div>
</template>

<script>

export default {

};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.flex-container {
  display: flex;
  flex-direction: column; /* Stack items vertically */
}

.flex-item {
  margin-bottom: 20px; /* Adjust the spacing between the divs */
  align-items: center;
  justify-content: center;

}

</style>
