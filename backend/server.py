
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from db import insert_invoice
from blockchain import record_invoice_on_chain

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        if self.path == '/add_invoice':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                invoice_id = insert_invoice(data)
                tx_hash = record_invoice_on_chain(data)
                self._set_headers()
                self.wfile.write(json.dumps({'message': 'Invoice submitted successfully', 'tx_hash': tx_hash}).encode())
            except Exception as e:
                self._set_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())

if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Server running on port 8000")
    httpd.serve_forever()
