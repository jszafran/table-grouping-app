<template>
  <v-data-table
      :headers="headers"
      :items-per-page="itemsPerPage"
      :items="alerts"
      fixed-header
      dense
      :show-select="true"
  >
  </v-data-table>
</template>

<script>
export default {
  name: "AlertTable",
  props: ["alerts"],
  data: () => ({
    headers: [
      {text: "Alert ID", value: "id"},
      {text: "Group name", value: "group_name"},
      {text: "Project", value: "project"},
      {text: "Severity", value: "severity"},
      {text: "Customer Segment", value: "customer_segment"},
      {text: "Priority", value: "priority"},
      {text: "Crime Type", value: "crime_type"},
    ],
    itemsPerPage: 20,
    dataLoaded: false,
  }),
}
</script>
