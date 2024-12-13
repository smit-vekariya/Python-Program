
"""
from requests import get
ip=get("https://www.javatpoint.com/javascript-interview-questions").text
print(f"Your ip address is {ip}")
"""

import socket 
host="pcb.sparrowerp.com"
print(f"ip adderss of {host} is {socket.gethostbyname(host)}")