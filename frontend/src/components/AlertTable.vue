<template>
  <v-data-table
      :headers="headers"
      :items-per-page="itemsPerPage"
      :items="alerts"
      fixed-header
      dense
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
      {text: "Project", value: "project"},
      {text: "Customer Segment", value: "customer_segment"},
      {text: "Crime Type", value: "crime_type"},
      {text: "Severity", value: "severity"},
      {text: "Priority", value: "priority"},
      {text: "Group name", value: "group_name"},
    ],
    itemsPerPage: 20,
    dataLoaded: false,
  }),
}
</script>
