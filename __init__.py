import os
from itertools import product 

def gen_ip(start_ip="0.0.0.0",end_ip="0.0.0.1"):
    start_ip = start_ip.split(".")
    end_ip = end_ip.split(".")    
    for p,q, in product(range(int(start_ip[2]),int(end_ip[2])+1),range(int(start_ip[3]),int(end_ip[3])+1)):
        x = f"{end_ip[0]}.{end_ip[1]}.{p}.{q}"
        yield x
    
def check(ip_lst):
    for ip in ip_lst:
        response = os.system("ping -c 1 " + ip)
        if response == 0:
            yield ip
        else:
            print(response)            

#check(["142.250.77.142"])