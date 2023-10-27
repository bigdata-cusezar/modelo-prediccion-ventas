from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
hostPort = 8000

class ServidorPredicionVentas(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write(bytes("<b> Hello World !</b>", 'utf-8'))

    paths = dict(
        GET={
            'macroproyectos'
        },
        POST={
            'macroproyectos'
        }
    )

    def resolve_path(self, path: str) -> callable:
        """
        Función básica para controlar acceso a recursos
        :param path:
        :return:
        """
        pass


servidor = HTTPServer((hostName, hostPort), ServidorPredicionVentas)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    servidor.serve_forever()
except KeyboardInterrupt:
    pass

servidor.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
