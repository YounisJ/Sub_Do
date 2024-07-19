import requests


print("                          \n",                                                   
" ad88888ba                88                     88888888ba,   \n",              
"d8       8b               88                     88      `'8b     \n",           
"Y8,                       88                     88        `8b          \n",     
"`Y8aaaaa,    88       88  88,dPPYba,             88         88   ,adPPYba,   \n",
"  `'''''8b,  88       88  88P'    '8a            88         88  a8'     '8a  \n",
"        `8b  88       88  88       d8            88         8P  8b       d8  \n",
"Y8a     a8P  '8a,   ,a88  88b,   ,a8'            88      .a8P   '8a,   ,a8'  \n",
 " Y88888P'    `'YbbdP'Y8  8Y'Ybbd8''              88888888Y''     `'YbbdP''   \n",
"                                                                            \n")
def find_subdomain(domain_name, sub_domnames):
    print("Sub_finder is working...")
    print("Scanning : ", domain_name)
    print("\n")

 
    for sub_domain in sub_domnames:
        url = f"http://{sub_domain}.{domain_name}"
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            print("[+] Discovered subdomain: ", url)
            
if __name__ == "__main__":
    print("\n")
    domain = input("Enter the domain name: ")
    print("\n")
    print("\n")
    with open("sub_list.txt") as file:
        name=file.read()
        sub_dom = name.splitlines()
    find_subdomain(domain, sub_dom)


   
