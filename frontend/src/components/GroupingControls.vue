<template>
  <v-row>
    <v-col>
      <v-select
        label="Project"
        :items="projects"
        v-model="project"
        clearable
      ></v-select>
    </v-col>
    <v-col>
      <v-select
          v-if="project"
          label="Customer Segment"
          :items="choices.customer_segment"
      ></v-select>
    </v-col>
    <v-col>
      <v-select
          v-if="project"
          label="Crime Type"
          :items="choices.crime_type"
      ></v-select>
    </v-col>
    <v-col>
      <v-select
          v-if="project"
          label="Severity"
          :items="choices.severity"
      ></v-select>
    </v-col>
    <v-col>
      <v-select
          v-if="project"
          label="Priority"
          :items="choices.priority"
      ></v-select>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: "GroupingControls",
  emits: ["controlsUpdated", "projectChosen", "projectCleared"],
  props: ["choices"],
  data: () => ({
    projects: [
        "LB_PROJ_GB",
        "BT_PROJ_AU",
        "LB_PROJ_IT",
    ],
    project: undefined,

  }),
  methods: {},
  watch: {
    project(newProj, oldProj) {
      if (newProj === undefined || newProj === null) {
        this.$emit("projectCleared")
        return
      }

      if (newProj !== oldProj && newProj !== undefined) {
        this.$emit("projectChosen", newProj)
      }
    }
  }

}
</script>
