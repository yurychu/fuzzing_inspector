from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

from datetime import datetime


class HttpGetHandler(BaseHTTPRequestHandler):

    def _get_current_datetime_str(self):
        result = datetime.now().ctime()
        return result

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        curr_time = self._get_current_datetime_str()
        to_send = '{ "name": "fuzz_target_1", "time": "' + curr_time + '" }'
        self.wfile.write(to_send.encode())


def run(server_class=HTTPServer, handler_class=HttpGetHandler):
  server_address = ('localhost', 8100)
  httpd = server_class(server_address, handler_class)
  try:
      httpd.serve_forever()
  except KeyboardInterrupt:
      httpd.server_close()


if __name__ == "__main__": run()
