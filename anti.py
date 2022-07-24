import os
import subprocess
import time
import random

blacklisted_ip = []

def block_ip(ip):
    blacklisted_ip.append(ip)
    os.system(f"iptables -I INPUT -s {ip} -j DROP")
    return f"[X] Blocked IP: {ip}"

def samp():
    while True:
        incoming_ips = subprocess.getoutput("timeout 1 tcpdump | grep UDP")
        current = incoming_ips.split("\n")[random.randrange(0, len(incoming_ips.split("\n")))]

        if len(incoming_ips) > 0:
            if "IP" in current:
                ip = current.split(" ")[2].split(".")
                full_ip = f"{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}"
                if full_ip in blacklisted_ip:
                    pass
                else:
                    resp = block_ip(full_ip)
                    print(resp)
            else:
                pass
        
        time.sleep(3)

samp()
