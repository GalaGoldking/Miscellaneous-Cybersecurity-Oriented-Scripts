from sys import argv, exit

def change_conf_file(domain, ip_address):
    with open("test.txt", "w+") as f:
        text = f"""[libdefaults]
   default_realm = {domain.upper()}
   dns_lookup_realm = false
   dns_lookup_kdc = true
   ticket_lifetime = 24h
   forwardable = true

[realms]
   {domain.upper()} = {{
       kdc = {ip_address}
       admin_server = {ip_address}
       default_domain = {domain.upper()}
   }}

[domain_realm]
   .{domain.lower()} = {domain.upper()}
   {domain.lower()} = {domain.upper()}"""
        f.write(text)
        
def validate_input(ip_address:str) -> bool:
    ip_address = ip_address.split('.')
    try:
        if len(ip_address) != 4:
            return False
        for snippet in ip_address:
            if not snippet.isdigit() and int(snippet) < 0 and int(snippet) > 255:
                return False
        else:
            return True
    except ValueError:
        return False
        
        
        
first_input = argv[1]
second_input = argv[2]

if __name__ == "__main__":
    if len(argv) == 3:
        if validate_input(first_input) is True and validate_input(second_input) is True:
            print("No valid Domain was provided")
            exit(1)
        elif validate_input(first_input) is True:
            ip_address = first_input
            domain = second_input
        elif validate_input(second_input) is True:
            ip_address = second_input
            domain = first_input
        else:
            print("No valid IP address was provided")
            exit(1)
            
        change_conf_file(domain, ip_address)
        print(f"Configuration file created for {domain} with IP {ip_address}")
    else:
        print("Usage: python krb5.conf.py IP/Domain IP/Domain")
