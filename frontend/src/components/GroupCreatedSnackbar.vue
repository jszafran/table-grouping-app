<template>
  <div class="text-center ma-2">
    <v-snackbar
        :value="show"
        text
        top
        color="primary"
    >
      {{ text }}

      <template v-slot:action="{ attrs }">
        <v-btn
            color="black"
            text
            v-bind="attrs"
            @click="onClose"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script>
export default {
  name: "GroupCreatedSnackbar",
  emits: ["closeSnackbar"],
  props: ["alertsCount", "groupName", "show"],
  data: function() {
    return {
      text: `Group '${this.groupName}' (${this.alertsCount} alerts) created!`,
    }
  },
  methods: {
    onClose() {
      this.$emit("closeSnackbar")
    }
  }
}
</script>
