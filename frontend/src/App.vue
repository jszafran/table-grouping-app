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
        <CreateAlertGroup v-if="filtersApplied"></CreateAlertGroup>
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
    }
  },
  methods: {
   async onProjectChosen(project) {
     this.project = project
      this.$http.get(`api/alerts?project=${project}`).then(resp => {
        this.alerts = resp.data.results
      }).catch(err => {
        console.log(err)
      })

     this.$http.get(`api/alerts/grouping_choices?project=${project}`).then(resp => {
       this.choices = resp.data
     }).catch(err => {
       console.log(err)
     })
    },
    async onProjectCleared() {
     this.alerts = []
     this.choices = emptyChoices()
      this.project = null;
    },
    async onFiltersUpdated(query) {
     this.$http.get(`api/alerts/${query}`).then(resp => {
       this.alerts = resp.data.results
     }).catch(err => {
       console.log(err)
     })
    },
    async onFiltersApplied(v) {
     this.filtersApplied = v
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
