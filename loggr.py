import urllib
import urllib2

class Config(object):
    logKey = ""
    apiKey = ""

class DataType(object):
    html = 0
    plaintext = 1
    json = 2
    
class Event(object):
    text = ''
    link = ''
    source = ''
    user = ''
    tags = ''
    value = ''
    data = ''
    dataType = DataType.plaintext
    geo = ''
    
class Events(object):
    @staticmethod
    def Create():
        return FluentEvent()
    
class Users(object):
    @staticmethod
    def TrackUser(username, email, page):
        values = {}
        values['apikey'] = Config.apiKey
        values['user'] = username
        if email:
            values['email'] = email
        if page:
            values['page'] = page
        url = 'http://post.loggr.net/1/logs/' + Config.logKey + '/users'
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
    
class FluentEvent(object):
    e = Event()
    def Text(self, t):
        self.e.text = t
        return self
    def Link(self, t):
        self.e.link = t
        return self
    def Source(self, t):
        self.e.source = t
        return self
    def User(self, t):
        self.e.user = t
        return self
    def Tags(self, t):
        self.e.tags = t
        return self
    def Value(self, t):
        self.e.value = t
        return self
    def Data(self, t):
        self.e.data = t
        return self
    def DataType(self, t):
        self.e.dataType = t
        return self
    def Geo(self, lat, lon):
        self.e.geo = str(lat) + "," + str(lon)
        return self
    def GeoIP(self, ip):
        self.e.geo = "ip:" + ip
        return self
    def Post(self):
        values = {}
        values['apikey'] = Config.apiKey
        values['text'] = self.e.text
        if self.e.link:
            values['link'] = self.e.link
        if self.e.source:
            values['source'] = self.e.source
        if self.e.user:
            values['user'] = self.e.user
        if self.e.tags:
            values['tags'] = self.e.tags
        if self.e.value:
            values['value'] = self.e.value
        if self.e.data:
            if self.e.dataType == DataType.html:
                values['data'] = '@html\n' + str(self.e.data)
            elif self.e.dataType == DataType.json:
                values['data'] = '@json\n' + str(self.e.data)
            else:
                values['data'] = str(self.e.data)
        if self.e.geo:
            values['geo'] = self.e.geo
        url = 'http://post.loggr.net/1/logs/' + Config.logKey + '/events'
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        
