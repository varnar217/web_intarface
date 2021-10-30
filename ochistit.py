
#app.secret_key = 'mysecret'

#socket_io = SocketIO(app)

tert= '{\n  "stats": {\n    "graph": {\n      "eb_id": 1,\n      "time": "2021-10-06T04:345:21.1436",\n      "period": 1000,\n      "size": 3521058,\n      "vpercent": 50,\n      "avrpktsz": 791,\n      "pktcount": 2574,\n      R"(\n    }\n  }\n}'
def func_ochist(tert):
    tert=tert.split('{')
    tert=''.join(tert[3:])
    tert=tert.split('}')

    tert=''.join(tert[:-3])
    tert=tert.strip()
    tert=tert.split(',')
    tert=''.join(tert[:-1])
    tert=tert.split('\n')
    bufer_out=[]
    for i in tert:
        bufer=[]
        tt=i.split(':')
        for ii in tt:
            bufer.append(ii)
        bufer_out.append(bufer)
    return bufer_out
