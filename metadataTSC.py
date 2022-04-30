import csv
import os
import json
import tableauserverclient as TSC
import extract_json_values

with open('C:\\creds\\pat.txt', 'r') as file :
    token = file.read()

with open('C:\\creds\\name.txt', 'r') as file :
    user = file.read()

with open('C:\\creds\\site.txt', 'r') as file :
    site = file.read()

tableau_auth = TSC.PersonalAccessTokenAuth(user,token,site)
server = TSC.Server('https://10ax.online.tableau.com', use_server_version=True)

with server.auth.sign_in(tableau_auth):
    result = server.metadata.query("""
    query tables {
  tables (filter:{name:"Orders"}){
    name
    id
    columns (filter:{name:"Segment"}){
      id
      name
      downstreamDashboards{
        name
        luid
        path
      }
    }
  }
}
    """)
    if result.get("errors"):
        print('### Errors/Warnings')
        print(result['errors'])
    
    if result.get("data"):
        with open('query_result.json',"w") as jsonfile:
            json.dump(result['data'], jsonfile, indent =4)

        extract_json_values.get_json_values('query_result.json','luid')
