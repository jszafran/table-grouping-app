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
          :items="customer_segments"
      ></v-select>
    </v-col>
    <v-col>
      <v-select
          v-if="project"
          label="Crime Type"
          :items="crime_types"
      ></v-select>
    </v-col>
    <v-col>
      <v-select
          v-if="project"
          label="Severity"
          :items="severities"
      ></v-select>
    </v-col>
    <v-col>
      <v-select
          v-if="project"
          label="Priority"
          :items="priorities"
      ></v-select>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: "GroupingControls",
  emits: ["controlsUpdated"],
  data: () => ({
    projects: [
        "LB_PROJ_GB",
        "BT_PROJ_AU",
        "LB_PROJ_IT",
    ],
    customer_segments: undefined,
    crime_types: undefined,
    priorities: undefined,
    severities: undefined,
    project: undefined,
  }),
  methods: {
    fetchChoicesForProject(project) {
      console.log(`Fetching choices for ${project} project`)
      this.$http.get(`api/alerts/grouping_choices?project=${project}`).then(
          resp => {
            this.crime_types = resp.data.crime_type
            this.customer_segments = resp.data.customer_segment
            this.priorities = resp.data.priority
            this.severities = resp.data.severity
          }
      ).catch(
          err => {
            console.log("Error when fetching choices", err)
          }
      )
    },
  },
  watch: {
    project(newProj, oldProj) {
      if (newProj === undefined || newProj === null) {
        return
      }
      if (newProj !== oldProj && newProj !== undefined) {
        this.fetchChoicesForProject(newProj)
      }
    }
  }

}
</script>
