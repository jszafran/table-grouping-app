<template>
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
            color="success"
            class="mr-4"
            :disabled="!valid || !groupName"
        >
          Create Group
        </v-btn>
      </v-col>
    </v-row>
  </v-form>

</template>

<script>
export default {
  name: "CreateAlertGroup",
  data: () => ({
    groupName: null,
    valid: false,
    groupNameRules: [
        v => !(v === "" || v === null) || "Group name cannot be an empty string",
        v => !v.includes(" ") || "Group name cannot contain white space.",
    ]
})
}
</script>
