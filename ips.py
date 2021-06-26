import ipaddress

ip = '192.168.0.1'

endereco = ipaddress.ip_address(ip)

print(endereco + 257)


ip2 = '192.168.0.0/24'

rede = ipaddress.ip_network(ip2, strict = false)

for ip2 in rede:

    print(rede)
