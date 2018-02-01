import urllib.request
from bs4 import BeautifulSoup
from ProxyItem import ProxyItem
import re
import base64

class ProxyInfoContainer:
    def __init__(self):
        self.countries = []
        self.proxyItems = []
        pass
    
    def fetchCountryInfo(self):
        url = "http://proxy-list.org/english/"
        #data = {'sid':'result', 'keyword': horseName.encode('Shift_JIS'),  'x':'9',  'y':'9'}
        #url_values=urllib.parse.urlencode(data)
        #GET
        #full_url=url+url_values 
        for i in range(10):
            try:
                data=urllib.request.urlopen(url,  timeout=30).read() 
                break
            except Exception as e:
                print('Error: ' + str(e))
                print('[retry %d]'%(i+1))
        else:
            return None
        
        soup = BeautifulSoup(data, "html.parser")
        tag_country = soup.find_all(name='select',  attrs={"name":"country"})
        tag_option = tag_country[0].find_all(name="option")
        self.countries = [(x.text,  x["value"]) for x in tag_option]
        
        #self.proxyItems.extend(self._getPageItems(soup))
        pass
        
    def fetchInfoForCountryByPage(self, country, page):
        url = "http://proxy-list.org/english/search.php?search=&country=%s&type=any&port=any&ssl=any&p=%s"%(country, page)
        for i in range(10):
            try:
                data=urllib.request.urlopen(url,  timeout=30).read() 
                break
            except Exception as e:
                print('Error: ' + str(e))
                print('[retry %d]'%(i+1))
        else:
            return False
        
        soup = BeautifulSoup(data, "html.parser")
        pageItems = self._getPageItems(soup)
        if pageItems:
            self.proxyItems.extend(pageItems)
        else:
            return False
        
        return True
    
    #
    # Get items for the current page
    #
    def _getPageItems(self,  soup):
        pageItems = []
        items_ul = soup.find(name="div",  class_="table").find_all("ul")
        for item in items_ul:
            item_ins = ProxyItem()
            ip_port_encoded = item.find("li", class_="proxy").get_text()
            item_ins.ip_port = self._getIPPort(ip_port_encoded)
            if not item_ins.ip_port:
                return None
            item_ins.protocol = item.find("li", class_="https").get_text()
            item_ins.speed = item.find("li", class_="speed").get_text()
            item_ins.type = item.find("li", class_="type").get_text()
            item_ins.country, item_ins.city = self._getCountryCity(item.find("li", class_="country-city"))
            
            #add to list
            pageItems.append(item_ins)
            #print(item_ins.printSelf())
        return None if len(pageItems) == 0 else pageItems
        
    def _getIPPort(self, encodedText):
        matchObj = re.match( r'Proxy\(\'(.*)?\'\)', encodedText)
        if matchObj:
            return base64.b64decode(matchObj.group(1)).decode()
        else:
            return ""
        pass
        
    def _getCountryCity(self, node):
        return (node.find(name="span", class_="country").find(name="span", class_="name").get_text(), node.find(name="span", class_="city").get_text())
        pass
        
#ProxyInfoContainer().fetchInfo()
