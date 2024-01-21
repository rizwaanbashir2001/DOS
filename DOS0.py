import whois

def get_nameserver_whois(domain_name):
    try:
        w = whois.whois(domain_name)
        return w.name_servers
    except Exception as e:
        return str(e)

domain_name = input("Enter a website URL: ")
print("Name servers:", get_nameserver_whois(domain_name))
