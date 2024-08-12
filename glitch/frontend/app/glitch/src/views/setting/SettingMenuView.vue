<script setup lang="ts"></script>

<template>
  <v-navigation-drawer color="background" class="no-border">
    <v-sheet>
      <v-list-item><router-link to="/setting/">Setting</router-link></v-list-item>
      <v-list-item><router-link to="/setting/user">User</router-link></v-list-item>
      <v-list-item><router-link to="/setting/project">Project</router-link></v-list-item>
    </v-sheet>
  </v-navigation-drawer>
</template>

<style scoped>
@import '@/assets/main.css';
</style>
