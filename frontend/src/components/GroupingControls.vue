<template>
  <div>
      <v-row align-content="left">
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
              v-model="customerSegment"
              clearable
          ></v-select>
        </v-col>
        <v-col>
          <v-select
              v-if="project"
              label="Crime Type"
              :items="choices.crime_type"
              v-model="crimeType"
              clearable
          ></v-select>
        </v-col>
        <v-col>
          <v-select
              v-if="project"
              label="Severity"
              :items="choices.severity"
              v-model="severity"
              clearable
          ></v-select>
        </v-col>
        <v-col>
          <v-select
              v-if="project"
              label="Priority"
              :items="choices.priority"
              v-model="priority"
              clearable
          ></v-select>
        </v-col>
        <v-col>
          <v-autocomplete
              v-if="project"
              label="Alert group"
              :items="choices.group_name"
              v-model="alertGroup"
              clearable
          ></v-autocomplete>
          <v-btn v-if="filtersApplied"
                 color="info"
                 small
                 @click="resetChoices"
          >
            Clear filters
          </v-btn>
        </v-col>

      </v-row>

    <v-row>
      <v-col>

      </v-col>
    </v-row>
  </div>

</template>

<script>
export default {
  name: "GroupingControls",
  emits: [
      "filtersUpdated",
      "projectChosen",
      "projectCleared",
      "filtersApplied",
  ],
  props: ["choices"],
  data: () => ({
    projects: [
        "LB_PROJ_GB",
        "BT_PROJ_AU",
        "LB_PROJ_IT",
    ],
    project: undefined,
    customerSegment: undefined,
    severity: undefined,
    priority: undefined,
    crimeType: undefined,
    alertGroup: undefined,
  }),
  computed: {
    queryParams() {
      const filters = []

      if (this.hasValue(this.project)) {
        filters.push(`project=${this.project}`)
      }

      if (this.hasValue(this.customerSegment)) {
        filters.push(`customer_segment=${this.customerSegment}`)
      }

      if (this.hasValue(this.severity)) {
        filters.push(`severity=${this.severity}`)
      }

      if (this.hasValue(this.priority)) {
        filters.push(`priority=${this.priority}`)
      }

      if (this.hasValue(this.crimeType)) {
        filters.push(`crime_type=${this.crimeType}`)
      }

      if (this.hasValue(this.alertGroup)) {
        filters.push(`group_name=${this.alertGroup}`)
      }

      if (filters.length === 0) {
        return ""
      }

      return "?" + filters.join("&")
    },
    filtersApplied() {
      return (
          this.hasValue(this.customerSegment)
          || this.hasValue(this.priority)
          || this.hasValue(this.severity)
          || this.hasValue(this.crimeType)
          || this.hasValue(this.alertGroup)
      )
    }
  },
  methods: {
    hasValue(v) {
      return v !== null
          && v !== undefined
          && v !== ""
    },
    resetChoices() {
      this.severity = null;
      this.crimeType = null;
      this.priority = null;
      this.alertGroup = null;
      this.customerSegment = null;
    }
  },
  watch: {
    project(newProj, oldProj) {
      if (newProj === undefined || newProj === null) {
        this.resetChoices()
        this.$emit("projectCleared")
        return
      }

      if (newProj !== oldProj && newProj !== undefined) {
        this.$emit("projectChosen", newProj)
      }
    },
    queryParams(newQuery, oldQuery) {
      if (newQuery !== oldQuery && newQuery.includes("project=")) {
        this.$emit("filtersUpdated", newQuery)
      }
    },
    filtersApplied(newVal, oldVal) {
      if (newVal !== oldVal) this.$emit("filtersApplied", newVal)
    }
  },
}
</script>
