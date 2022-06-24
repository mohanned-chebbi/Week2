import shodan,fpdf

shodan_key = "bLlgK1CvSKC52TCNmNYhq44rMZzDDA7U"
api = shodan.Shodan(shodan_key)

xxx = input("Enter an IP adress you want to scan: ")
print(f"The IP adress is: {xxx}")
print("Please Wait ...")

host = api.host(xxx)

try:

    print("""
            IP: {}
            Organization: {}
            Operating System: {}
        """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

except shodan.APIError as e:
        print('Error: {e}')

for item in host['data']:
        print("""
                Port: {}
                Banner: {}

        """.format(item['port'], item['data']))

