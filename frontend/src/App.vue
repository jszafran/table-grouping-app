<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
      </div>

      <v-spacer></v-spacer>


    </v-app-bar>

    <v-main>
      <v-container>
        <GroupingControls
            @projectChosen="onProjectChosen"
            @projectCleared="onProjectCleared"
            @filtersUpdated="onFiltersUpdated"
            @filtersApplied="onFiltersApplied"
            :choices="choices"
        ></GroupingControls>
        <CreateAlertGroup
            v-if="filtersApplied"
            @alertGroupCreate="onAlertGroupCreate"
        >
        </CreateAlertGroup>
      </v-container>
      <AlertTable
        :alerts="alerts"
      />
    </v-main>
  </v-app>
</template>

<script>
import AlertTable from "@/components/AlertTable";
import GroupingControls from "@/components/GroupingControls";
import CreateAlertGroup from "@/components/CreateAlertGroup";
import {emptyChoices} from "@/utils";

export default {
  name: 'App',
  components: {
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
    }
  },
  methods: {
   async fetchAlerts(url) {
     this.$http.get(url).then(resp => {
       this.alerts = resp.data.results
     }).catch(err => {
       console.log(err)
     })
   },
    async fetchChoices(project) {
     this.$http.get(`api/alerts/grouping_choices?project=${project}`).then(
         resp => {
           console.log(resp.data)
           this.choices = resp.data
         }
     ).catch(err => {
       console.log(err)
     })
    },
    async createAlertGroup(groupName) {
      this.$http.post(
          `api/alerts/create_group`,
          {
            group_name: groupName,
            alert_ids: this.alerts.map(x => x.id),
          }
      ).then(resp => {
        console.log(resp)
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
