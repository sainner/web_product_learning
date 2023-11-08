from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 返回状态码200 OK
        self.send_response(200)
        # 设置头部信息为text/html类型
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # 向客户端写入响应内容
        self.wfile.write(b"Hellolxy")

# 设置服务器的端口
server_address = ('', 8000)
httpd = HTTPServer(server_address, HelloHandler)

print("Server running on port 8000...")
# 启动服务器
httpd.serve_forever()
