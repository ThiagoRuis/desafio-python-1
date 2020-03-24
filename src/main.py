import sys, os
from server.instance import server

# Need to import all resources
# so that they register with the server 
from controller import *

if __name__ == '__main__':
    server.run()