<template>
  <h3>Task Tracker is a tool that helps manage everyday work more efficiently. It is suitable for standalone professionals, teams and also to keep track of your personal chores !</h3>
  <h5>Version 1.0</h5>
  <h5>Developed: Vatazhok and Korostelev</h5>
  <div class="link">
    <router-link to="/">Go Back</router-link>
  </div>
</template>

<script>
export default {
  name: 'About',
  inheritAttrs: false,
};
</script>
<style scoped>
h3{
  padding-bottom: 25px;
}
.link{
  padding-top: 25px;
  text-align: center;
}
</style>
