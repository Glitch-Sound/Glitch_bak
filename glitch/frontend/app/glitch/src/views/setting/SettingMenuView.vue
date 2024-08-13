<script setup lang="ts"></script>

<template>
  <v-navigation-drawer color="background" class="no-border">
    <v-sheet color="#1d1d1d" class="rounded-lg mt-1 ml-1 py-3">
      <v-list-item
        ><router-link to="/setting/"><v-icon icon="mdi-cog" />Setting</router-link></v-list-item
      >

      <v-list-item
        ><router-link to="/setting/user"
          ><v-icon icon="mdi-account" />User</router-link
        ></v-list-item
      >

      <v-list-item
        ><router-link to="/setting/project"
          ><v-icon icon="mdi-grain" />Project</router-link
        ></v-list-item
      >
    </v-sheet>
  </v-navigation-drawer>
</template>

<style scoped>
@import '@/assets/main.css';

.v-icon {
  margin: 0 15px 0 0;
}
</style>
