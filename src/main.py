import flet as ft
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler


def main(page: ft.Page):
    def run_server(host: str = "localhost", port: int = 2012):
        server = HTTPServer((host, port), SimpleHTTPRequestHandler)
        print(f"Server started at http://{host}:{port}")
        server.serve_forever()

    def render_latex():
        wv.run_javascript('renderLatex("Hello, World!")')
        wv.update()

    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    wv = ft.WebView(
        url="http://localhost:2012/",
        expand=True,
    )
    page.add(wv)
    wv.on_page_ended = lambda _: render_latex()


ft.app(main)
