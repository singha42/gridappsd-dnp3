import json
with open("/home/git/gridappsd-dnp3/service/port.json", 'r') as f:
    port_config = json.load(f)
    print(port_config)
    for m in port_config:
        print(m['port'])
    #     # if "port" in m.keys():
    #     print(port1)



