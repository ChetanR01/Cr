import socket
import subprocess
import os
from ipaddress import IPv4Network,IPv4Address


def active_ips_in_network(ip):
    # ip_range = IPv4Address(ip)
    active_ip_list=[]
    inactive_ip_list=[]
    if "/" in ip:
        net= IPv4Network(ip)
        for i in net:
            print(i)
        no_of_adds= net.num_addresses
        print("IP",ip_range)
        print("Subnet Mask",net)
        print("No of hosts",no_of_adds)

        import ipaddress
        net_ips = ipaddress.ip_network(net)
        print("Net IP", net_ips)
        # loop through all IP addresses in the range and check if they're reachable
        for host in net_ips.hosts():
            temp= str(host)
            # ping the IP address to see if it's reachable
            response = subprocess.Popen(['ping', '-n', '1', '-w', '500', temp], stdout=subprocess.PIPE).stdout.read()
            if 'Reply' in str(response):
                active_ip_list.append(temp)
            else:
                inactive_ip_list.append(temp)
            print("Host",temp)
    else:
        response = subprocess.Popen(['ping', '-n', '1', '-w', '500', ip], stdout=subprocess.PIPE).stdout.read()
        if 'Reply' in str(response):
            active_ip_list.append(ip)
        else:
            inactive_ip_list.append(ip)
        print("Host",ip)
    return active_ip_list, inactive_ip_list
ip_range="192.168.162.140"
active_ip_list, inactive_ip_list = active_ips_in_network(ip_range)
print(active_ip_list)
print(inactive_ip_list)
