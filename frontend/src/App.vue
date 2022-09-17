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

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <GroupingControls
          @projectChosen="onProjectChosen"
          @projectCleared="onProjectCleared"
          @filtersUpdated="onFiltersUpdated"
          :choices="choices"
      ></GroupingControls>
      <AlertTable
        :alerts="alerts"
      />
    </v-main>
  </v-app>
</template>

<script>
import AlertTable from "@/components/AlertTable";
import GroupingControls from "@/components/GroupingControls";
import {emptyChoices} from "@/utils";

export default {
  name: 'App',

  components: {
    AlertTable,
    GroupingControls,
  },

  data: function() {
    return {
      alerts: [],
      choices: emptyChoices(),
    }
  },
  methods: {
   async onProjectChosen(project) {
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
    },
    async onFiltersUpdated(query) {
     this.$http.get(`api/alerts/${query}`).then(resp => {
       this.alerts = resp.data.results
     }).catch(err => {
       console.log(err)
     })
    }
  }
};
</script>
