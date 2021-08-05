from __init__ import *
import time

start_ip = input("Enter start ip: ").strip()
end_ip = input("Enter end ip: ").strip()
print("start scaning...".title())
start_time = time.time()
ip_lst = list(gen_ip(start_ip,end_ip))
valid_ip_lst = list(check(ip_lst))

if valid_ip_lst != []:
    with open("saveip.txt", "r+") as f:
        f.truncate(0)
        f.close()
    print("IP List")
    for i in range(1,len(valid_ip_lst)+1):
        fvalid= f"{i} {valid_ip_lst[i-1]}"
        with open("saveip.txt", "a") as f:
            f.write(fvalid+"\n")
            f.close()
        print(fvalid)
else:
    print("No valid ip foun".title())

end_time = time.time()
passt = end_time-start_time
if (end_time - start_time) >= 60:
    print(f"Time takes {passt/60} miniutes")
else:
    print(f"Time takes {passt} seconds")

