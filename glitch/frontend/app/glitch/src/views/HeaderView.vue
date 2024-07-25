<script setup lang="ts"></script>

<template>
  <v-app-bar class="elevation-0">
    <v-app-bar-title> Project name </v-app-bar-title>

    <router-link to="/">
      <v-btn icon>
        <v-icon>mdi-view-list</v-icon>
      </v-btn>
    </router-link>

    <v-btn icon disabled>
      <v-icon>mdi-account-tag</v-icon>
    </v-btn>
    <v-btn icon disabled>
      <v-icon>mdi-chart-scatter-plot-hexbin</v-icon>
    </v-btn>

    <v-spacer></v-spacer>

    hogehoge
    <v-btn icon>
      <v-icon>mdi-account-circle</v-icon>
    </v-btn>

    <v-btn icon disabled>
      <v-icon>mdi-magnify</v-icon>
    </v-btn>

    <router-link to="/setting">
      <v-btn icon>
        <v-icon>mdi-cog</v-icon>
      </v-btn>
    </router-link>
  </v-app-bar>
</template>

<style scoped></style>
