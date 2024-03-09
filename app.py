import socket
from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
# Define user credentials and directory
user = "user"
password = "12345"
directory = "./server"

authorizer = DummyAuthorizer()
authorizer.add_user(user, password, directory, perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = servers.FTPServer((ip, 21), handler)
server.serve_forever()