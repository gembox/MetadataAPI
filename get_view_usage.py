import csv
import os
import tableauserverclient as TSC


def view_usage(viewid,tableau_auth,server):

    with server.auth.sign_in(tableau_auth):
        vmatch = server.views.get_by_id(viewid)
        workbookid = vmatch._workbook_id
        match = server.workbooks.get_by_id(workbookid)
        server.workbooks.populate_views(match,usage=True)
        output = [view for view in match.views if vmatch.id == view.id]
        return output[0]