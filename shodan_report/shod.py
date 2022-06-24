from importlib.resources import path
from urllib import request
import shodan,json

shodan_key = "bLlgK1CvSKC52TCNmNYhq44rMZzDDA7U"
api = shodan.Shodan(shodan_key)

xxx = input("Enter an IP adress you want to scan: ")
print(f"The IP adress is: {xxx}")
print("Please Wait ...")

host = api.host(xxx)
"""
try:

    print(host)

except shodan.APIError as e:
        print('Error: {e}')
"""
def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

path = './'
fileName = 'shodan_report'
data = {}
for report in host['data']:
    data = report


writeToJSONFile(path,fileName,data)

