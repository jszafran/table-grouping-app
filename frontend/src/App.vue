<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-app-bar-title>Alert Grouping POC</v-app-bar-title>
      </div>
      <v-spacer></v-spacer>
      <v-btn v-if="project"
          text
          @click="onRemoveAllGroups"
      >
        <span class="mr-2">Remove all groups</span>
      </v-btn>
    </v-app-bar>
    <v-main>
      <v-container>
        <GroupCreatedSnackbar v-if="showSnackbar"
            :show="showSnackbar"
            :group-name="snackbarGroupName"
            :alerts-count="alerts.length"
            @closeSnackbar="showSnackbar = false"
        ></GroupCreatedSnackbar>

        <GroupingControls
            @projectChosen="onProjectChosen"
            @projectCleared="onProjectCleared"
            @filtersUpdated="onFiltersUpdated"
            @filtersApplied="onFiltersApplied"
            :choices="choices"
            :waiting-for-alerts="waitingForAlerts"
        ></GroupingControls>
        <CreateAlertGroup
            v-if="filtersApplied"
            @alertGroupCreate="onAlertGroupCreate"
        >
        </CreateAlertGroup>
      </v-container>
      <AlertTable
        :alerts="alerts"
        :table-loading="tableLoading"
      />
    </v-main>
  </v-app>
</template>

<script>
import AlertTable from "@/components/AlertTable";
import GroupingControls from "@/components/GroupingControls";
import CreateAlertGroup from "@/components/CreateAlertGroup";
import {emptyChoices} from "@/utils";
import GroupCreatedSnackbar from "@/components/GroupCreatedSnackbar";

export default {
  name: 'App',
  components: {
    GroupCreatedSnackbar,
    AlertTable,
    GroupingControls,
    CreateAlertGroup,
  },

  data: function() {
    return {
      alerts: [],
      choices: emptyChoices(),
      project: null,
      filtersApplied: false,
      query: "",
      showSnackbar: false,
      snackbarGroupName: "",
      tableLoading: false,
      waitingForAlerts: false,
    }
  },
  methods: {
    turnOnLoader() {
      this.tableLoading = true
      this.waitingForAlerts = true
    },
    turnOffLoader() {
      this.tableLoading = false
      this.waitingForAlerts = false
    },
   async fetchAlerts(url) {
    this.turnOnLoader()
     this.$http.get(url).then(resp => {
       this.alerts = resp.data.results
       this.turnOffLoader()
     }).catch(err => {
       console.log(err)
       this.turnOffLoader()
     })
   },
    async fetchChoices(project) {
     this.$http.get(`api/alerts/grouping_choices?project=${project}`).then(
         resp => {
           this.choices = resp.data
         }
     ).catch(err => {
       console.log(err)
     })
    },
    async createAlertGroup(groupName) {
      this.tableLoading = true
      this.$http.post(
          `api/alerts/create_group`,
          {
            group_name: groupName,
            alert_ids: this.alerts.map(x => x.id),
          }
      ).then(() => {
        this.fetchAlerts(`api/alerts/${this.query}`)
        this.fetchChoices(this.project)
      }).catch(err => {
        console.log(err)
      })
    },
   async onProjectChosen(project) {
     this.project = project
     this.alerts = await this.fetchAlerts(`api/alerts?project=${project}`)
     this.choices = await this.fetchChoices(project)
    },
    async onProjectCleared() {
     this.alerts = []
     this.choices = emptyChoices()
      this.project = null;
    },
    async onFiltersUpdated(query) {
     this.query = query
     this.alerts = await this.fetchAlerts(`api/alerts/${query}`)
    },
    async onFiltersApplied(v) {
     this.filtersApplied = v
    },
    async onAlertGroupCreate(groupName) {
      await this.createAlertGroup(groupName)
      this.snackbarGroupName = groupName
      this.showSnackbar = true;
    },
    async onRemoveAllGroups() {
     this.tableLoading = true
     this.$http.post(
         `/api/alerts/remove_all_groups`
     ).then(() => {
       this.fetchAlerts(`api/alerts/${this.query}`)
       this.fetchChoices(this.project)
     }).catch(err => console.log(err))
    }
  }
};
</script>

<style>
  .controls {
    margin-left: 10px;
    margin-right: 10px;
  }
</style>
