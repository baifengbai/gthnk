# (c) 2013 Ian Dennis Miller
# -*- coding: utf-8 -*-

from poodledo.apiclient import ApiClient, PoodledoError, ToodledoError
import json, os
from GT.dashboard import DashboardWidget

class TodoWidget(DashboardWidget):
    filename = "~/.gt/dashboard.json"

    def do_login(self):
        client = ApiClient()
        with open(os.path.expanduser(filename), "r") as f:
            auth = json.load(f)

        try:
            client.application_id = "dash"
            client.application_token = auth['app_token'].encode('rot13')
        except KeyError:
            raise PoodledoError("Application ID or token not specified in configuration")

        try:
            client._key = auth['session_key']
            client.getAccountInfo()
        except (ToodledoError, KeyError):
            # cached session key either wasn't there or wasn't good; get a new one and cache it
            client._key = None

            try:
                client.authenticate(auth['username'], auth['password'].encode('rot13'))
            except ToodledoError as e:
                print("No login credentials were successful; please try again.")
                raise e

            auth['session_key'] = client.key
            with open(os.path.expanduser(filename), "w") as f:
                json.dump(auth, f, indent=4)

        return client

    def render(self):
        c = self.do_login()
        todos = c.getTasks()
        todos.reverse()
        todos_list = list(dict(i) for i in todos)
        return json.dumps(todos_list, indent=4)
