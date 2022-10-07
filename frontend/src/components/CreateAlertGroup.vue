<template>
  <div>
    <v-form v-model="valid">
      <v-row>
        <v-col>
          <v-text-field
              :counter="100"
              label="Group name"
              :rules="groupNameRules"
              v-model="groupName"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-btn
              color="info"
              class="mr-4"
              :disabled="!valid || !groupName"
              @click="emitAlertGroupCreate"
          >
            Create Group
          </v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: "CreateAlertGroup",
  emits: ["alertGroupCreate"],
  data: () => ({
    groupName: "",
    valid: false,
    groupNameRules: [
        v => !v.includes(" ") || "Group name cannot contain white space.",
        v => !v.includes(",") || "group name cannot contain a comma."
    ],

}),
  methods: {
    emitAlertGroupCreate() {
      this.$emit("alertGroupCreate", this.groupName)
      this.groupName = "";
    }
  }
}
</script>
