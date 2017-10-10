# f = open('helloworld.txt','w')
# f.write('hello world')
# f.close()


ip="000.000.000.000"

def ip_validator(to_validate):
    if len(to_validate) >15:
        print "ip no valida"
        exit(0)
    splited_ip = to_validate.split('.')
    for item in splited_ip:
        print item, len(item)
        if len(item) > 3 and len(item) < 0:
            print "ip no valida"
            break
        if not item.isdigit():
            print "ip no valida"
            break
    print splited_ip

ip_validator(ip)