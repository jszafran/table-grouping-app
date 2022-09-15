<template>
  <div v-if="dataLoaded">
    <v-data-table
        :headers="headers"
        :items-per-page="itemsPerPage"
        :items="items"
    >
    </v-data-table>
  </div>
</template>

<script>
export default {
  name: "AlertTable",
  data: () => ({
    headers: [
      {text: "Alert ID", value: "id"},
      {text: "Group name", value: "group"},
      {text: "Project", value: "project"},
      {text: "Severity", value: "severity"},
      {text: "Customer Segment", value: "customer_segment"},
      {text: "Priority", value: "priority"},
      {text: "Crime Type", value: "crime_type"},
    ],
    items: null,
    itemsPerPage: 20,
    dataLoaded: false,
  }),
  mounted() {
    console.log("Alert table was mounted!")
    this.$http.get("api/alerts").then((resp) => {
      this.items = resp.data.results
      this.dataLoaded = true
    }).catch((err) => {
      console.log(err)
      console.log("Failed to fetch alerts")
    })
  }
}
</script>
