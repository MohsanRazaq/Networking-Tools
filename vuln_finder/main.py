import socket
import os

file = "common_vuln.txt"

# Create file if it doesn't exist
if not os.path.exists(file):
    open(file, 'w').close()

# ------------------ load patterns  ------------------
def load_patterns():
    patterns = []
    with open(file, 'r') as f:
        for line in f:  
            line = line.strip() 
            if line:
                patterns.append(line.lower())  
    return patterns


# ------------------ get banner ------------------
def get_banner(ip, port):
    try:
        socket.setdefaulttimeout(2)

        s = socket.socket()
        s.connect((ip, port))

        # Sending http request so we receieve some response
        if port == 80:
            s.send(b"GET / HTTP/1.1\r\nHost: test\r\n\r\n")

        result = s.recv(1024)
        s.close()

        response = result.decode(errors="ignore")

        headers = response.split("\r\n\r\n")[0]

        return headers

    except Exception:
        return None


# ------------------ check patterns ------------------
def vuln_check(headers, patterns):
    if not headers:
        return
 
    for pattern in patterns:
        if pattern in headers.lower():
            print(f"[+] Match Found --> {pattern}")


# ------------------ main ------------------
def menu():
    ports = [21, 22,23, 80, 443, 110]

    patterns = load_patterns() 

    for sub in range(1, 20): 
        ip = "192.168.100." + str(sub)

        for port in ports:
            headers = get_banner(ip, port)

            if headers:
                print(f"{ip}:{port}\n{headers}\n")
                vuln_check(headers, patterns)


if __name__ == "__main__":
    menu()
