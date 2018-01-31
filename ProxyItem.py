class ProxyItem:
    ip_port = ""
    country=""
    city=""
    type=""
    speed=""
    protocol=""
    
    def printSelf(self):
        return self.ip_port + ", " + self.country + ", " + self.city + ", " + self.type + ", " + self.speed + ", " + self.protocol
