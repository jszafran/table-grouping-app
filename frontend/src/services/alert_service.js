import axios from "axios";

async function fetchChoicesForProject(project) {
    axios.get(`api/alerts/grouping_choices?project=${project}`).then(
        resp => {
            const choices = {
                crimeTypes: resp.data.crime_type,
                customerSegments: resp.data.customer_segment,
                priorities: resp.data.priority,
                severities: resp.data.severity
            }
            return choices
        }
    ).catch(
        err => {
            console.log("Error when fetching choices", err)
        }
    )
}

async function  fetchDataForProject(project) {
    axios.get(`api/alerts?project=${project}`).then(
        resp => {
            return resp.data
        }
    ).catch(
        err => {
            console.log(err)
        }
    )
}

export { fetchChoicesForProject, fetchDataForProject }
