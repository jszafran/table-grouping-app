<template>
  <div>
      <v-row>
        <v-col>
          <v-select
              label="Project"
              :items="projects"
              v-model="project"
              clearable
              chips
              :disabled="waitingForAlerts"
          ></v-select>
        </v-col>
        <v-col>
          <v-select
              v-if="project && choices"
              label="Customer Segment"
              :items="choices.customer_segment"
              v-model="customerSegment"
              multiple
              deletable-chips
              chips
              :disabled="waitingForAlerts"
          ></v-select>
        </v-col>
        <v-col>
          <v-select
              v-if="project  && choices"
              label="Crime Type"
              :items="choices.crime_type"
              v-model="crimeType"
              clearable
              multiple
              deletable-chips
              chips
              :disabled="waitingForAlerts"
          ></v-select>
        </v-col>
        <v-col>
          <v-select
              v-if="project && choices"
              label="Severity"
              :items="choices.severity"
              v-model="severity"
              clearable
              multiple
              deletable-chips
              chips
              :disabled="waitingForAlerts"
          ></v-select>
        </v-col>
        <v-col>
          <v-select
              v-if="project && choices"
              label="Priority"
              :items="choices.priority"
              v-model="priority"
              clearable
              multiple
              deletable-chips
              chips
              :disabled="waitingForAlerts"
          ></v-select>
        </v-col>
        <v-col>
          <v-autocomplete
              v-if="project && choices"
              label="Alert group"
              :items="choices.group_name"
              v-model="alertGroup"
              clearable
              multiple
              deletable-chips
              chips
              :disabled="waitingForAlerts"
          ></v-autocomplete>

        </v-col>

      </v-row>

    <v-row style="margin-top: 0;">
      <v-col>
        <v-btn v-if="filtersApplied"
               color="red lighten-1"
               @click="resetChoices"
        >
          Clear filters
        </v-btn>
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
  props: ["choices", "waitingForAlerts"],
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
        filters.push(this.getQueryUrl("customer_segment", this.customerSegment))
      }

      if (this.hasValue(this.severity)) {
        filters.push(this.getQueryUrl("severity", this.severity))
      }

      if (this.hasValue(this.priority)) {
        filters.push(this.getQueryUrl("priority", this.priority))
      }

      if (this.hasValue(this.crimeType)) {
        filters.push(this.getQueryUrl("crime_type", this.crimeType))
      }

      if (this.hasValue(this.alertGroup)) {
        filters.push(this.getQueryUrl("group_name", this.alertGroup))
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
    getQueryUrl(key, val) {
      const suffix = Object.values(val).length > 1 ? "__in" : ""
      return `${key}${suffix}=${val}`
    },
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
