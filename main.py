import sipfullproxy
import socketserver
import logging
import time
import socket

def setupLogger():
    logging.basicConfig(format='%(asctime)s - %(message)s', filename='call_logs.log', level=logging.INFO,
                       datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))

# Main
def main():

    # Setup logger
    setupLogger()

    # Get IP address
    ipaddress = socket.gethostbyname(socket.gethostname())
    logging.info("Server starting at %s" % ipaddress)
    print("Server starting at %s" % ipaddress)

    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, sipfullproxy.PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, sipfullproxy.PORT)

    # Set up the server
    server = socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
    # Start the server
    server.serve_forever()


if __name__ == "__main__":
    main()
