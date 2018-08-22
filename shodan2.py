import shodan
from subprocess import check_output as call
 
api_key = 'eKCp0zyOeoTlnNP1GQ98oAJmxKj49XC3'
 
api = shodan.shodan(api_key)
 
ip = bytes.decode(
    call(
        'dig +short myip.opendns.com @resolver1.opendns.com',
        shell=True
    )
).strip()
 
print(api.search(ip))