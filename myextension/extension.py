from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.utils import url_path_join

class MyExtensionHandler(JupyterHandler):

    def get(self):
        self.write("Hello, world")


def load_jupyter_server_extension(serverapp):

    webapp = serverapp.web_app

    route_pattern = url_path_join(webapp.settings['base_url'], '/myextension')

    webapp.add_handlers('.*$', 
        [
            (route_pattern, MyExtensionHandler)
        ]
    )