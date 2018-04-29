import time
import json
import random
import os

class ExportUtil:
    def _getRandomStr(self, n):
        rslt = ""
        for i in range(n):
            rslt += hex(random.randint(0, 15))[2:]
        return rslt.upper()

    def _getRandomUUID(self, ):
        return self._getRandomStr(8) + "-" + self._getRandomStr(4) + "-" + self._getRandomStr(4) + "-" + self._getRandomStr(4) + "-" + self._getRandomStr(12)

    def _getCfgItem(self, ip, port, country, type):
        timestamp = time.time()
        item = {
                "obfsParam" : "",
                "weight" : int(timestamp),
                "title" : "",
                "host" : ip,
                "ota" : False,
                "file" : "",
                "uuid" : self._getRandomUUID(),
                "method" : "aes-256-cfb",
                "flag" : country,
                "updated" : timestamp,
                "obfs" : "",
                "type" : type,
                "user" : "",
                "protoParam" : "",
                "tls" : False,
                "port" : port,
                "selected" : False,
                "proto" : "",
                "password" : "",
                "data" : "",
                "ping" : "",
                "created" : timestamp
        }
        return item
    
    def exportShadowrocketJSON(self, proxyTable):
        output = []

        for i in range(proxyTable.rowCount()):
            ip_port = proxyTable.item(i, 0).text()
            ip = ip_port.split(":")[0]
            port = ip_port.split(":")[1]
            country = proxyTable.item(i, 1).text()[:2]
            type = proxyTable.item(i, 5).text()
            output.append(self._getCfgItem(ip, port, country, type))

        if not os.path.exists("outputs"): 
            os.makedirs("outputs") 
        fo = open("outputs/Shadowrocket.json", "w")
        fo.write(json.dumps(output,indent=2))
        fo.close()