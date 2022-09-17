<template>
  <v-row>
    <v-col>
      <v-text-field
          :counter="100"
          label="Group name"
      ></v-text-field>
      <v-btn
          color="success"
          class="mr-4"
      >
        Validate
      </v-btn>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: "CreateAlertGroup",
}
</script>
