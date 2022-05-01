import csv
import tableauserverclient as TSC
import get_view_usage


with open('C:\\creds\\pat.txt', 'r') as file :
    token = file.read()

with open('C:\\creds\\name.txt', 'r') as file :
    user = file.read()

with open('C:\\creds\\site.txt', 'r') as file :
    site = file.read()

tableau_auth = TSC.PersonalAccessTokenAuth(user,token,site)
server = TSC.Server('https://10ax.online.tableau.com', use_server_version=True)

with server.auth.sign_in(tableau_auth):
    with open("luid_output.csv", "r") as viewids:
        wreader = csv.reader(viewids, delimiter=',')
        
        for row in wreader:
            view = get_view_usage.view_usage(row[0],tableau_auth,server)
            print("Viewid:{} - Viewname: {} has {} total views.".format(view.id, view.name, view._total_views))