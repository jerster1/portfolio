import shodan
import sys
from subprocess import check_output as call
 
api_key = 'HOgh3aguR75vIevPDYZQS8RGYQoDba9V'
 
api = shodan.Shodan(api_key)
 
ip = input('enter a desired ip or ip range: ')
 
results = api.scan(ip)
 
print("Total results {}".format(results['total']))
print(results['matches']['ip_str'])
 
# Create a tool that takes an ip range from the user
# search Shodan database for each IP
# present "some kind of useful data" to the user