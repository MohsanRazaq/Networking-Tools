import ipaddress
## How many targets are in range of given IP
ip='192.168.100.0/30'
network=ipaddress.ip_network(ip)
print(f'The network is : {network}\n')

for ip in network:
    print(f'Target ip is : {ip}') 