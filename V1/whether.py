import urllib, urllib2, sys
import ssl


host = 'https://saweather.market.alicloudapi.com'
path = '/spot-to-weather'
method = 'GET'
appcode = '21c3196600644b92ae0b70707736cd3d'
querys = 'area=%E6%B3%B0%E5%B1%B1&need3HourForcast=0&needAlarm=0&needHourData=0&needIndex=0&needMoreDay=0'
bodys = {}
url = host + path + '?' + querys

request = urllib2.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib2.urlopen(request, context=ctx)
content = response.read()
if (content):
    print(content)