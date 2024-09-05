from socket import *

# Function to perform a connection scan on a specific port of the target host
def conScan(tgtHost, tgtPort):
    try:
        # Create a new socket using IPv4 and TCP connection
        connskt = socket(AF_INET, SOCK_STREAM)
        
        # Try to establish a connection to the target host and port
        connskt.connect((tgtHost, tgtPort))
        
        # If successful, print that the port is open
        print('[+] %d/tcp open' % tgtPort)
        
        # Close the connection after checking the port
        connskt.close()
    except:
        # If the connection fails, print that the port is closed
        print('[-] %d/tcp closed' % tgtPort)

# Function to scan multiple ports on the target host
def portScan(tgtHost, tgtPorts):
    try:
        # Resolve the target host's name to an IP address
        tgtIP = gethostbyname(tgtHost)
    except:
        # If the hostname cannot be resolved, print an error and exit the function
        print('[-] Cannot resolve %s' % tgtHost)
        return
    
    try:
        # Attempt to get the full name of the target host using its IP address
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan results for: %s' % tgtName[0])
    except:
        # If the host name is unavailable, print the target IP instead
        print('\n[+] Scan results for: %s' % tgtIP)
    
    # Set a default timeout for socket connections (1 second in this case)
    setdefaulttimeout(1)
    
    # Loop through each port in the list of target ports and scan them
    for tgtPort in tgtPorts:
        print('Scanning Port: %d' % tgtPort)
        
        # Call the connection scan function to check the port status
        conScan(tgtHost, int(tgtPort))

# If the script is executed directly (not imported), perform a scan on 'google.com' for ports 80 (HTTP) and 22 (SSH)
if __name__ == '__main__':
    portScan('google.com', [80, 22])