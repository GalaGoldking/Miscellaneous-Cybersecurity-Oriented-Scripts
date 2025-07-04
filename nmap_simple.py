from sys import argv

def run_nmap_port_scan(host:str) -> None:
    """
    Run Nmap port scan on the given host
    """
    from os import system
    
    cmd = f"nmap --min-rate=5000 -Pn -n -p- {host} | grep '^ *[0-9]\\+/tcp' | grep open | awk -F '/' '{{print $1}}' > ports.txt"
    system(cmd)
    
    cut_results()
    
def cut_results() -> None:
    """
    Format ports.txt file for correct port format for nmap
    """
    with open("ports.txt", "r+") as f:
        placeholder = f.read()
        spliter = placeholder.split("\n")
        filter_ports = [x for x in spliter if x is not None and x != ""]
        combined_ports = ",".join(filter_ports)
        f.seek(0)
        f.write(combined_ports)
        f.truncate()

def run_service_scan(host:str) -> None:
    """
    Run service port scan on found and filtered ports
    """
    from os import system
    
    cmd = f"nmap -sC -sV -p$(cat ports.txt) {host} -oN {host}_nmap.txt"
    system(cmd)
    
host = argv[1]
run_nmap_port_scan(host)
run_service_scan(host)
