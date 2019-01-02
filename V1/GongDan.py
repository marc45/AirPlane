# -*- coding: utf-8 -*-
import base64
import hmac
import urllib
import time
import operator
import urllib
import requests
import json
import xlwt
import datetime
from hashlib import sha256
from datetime import datetime,timedelta
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

#获取当前时间
now_time = datetime.now().strftime('%Y-%m-%d')





#global
access_key_id = "SDOFLOAXFHXQIWBTXBYG"
secret_access_key = "z2daqTBqV1kyOM1ShHCDR28Ae1uS139anImgg0kU"
count = 1
zone = "SHA"
version = "1"
signature_version = 1
signature_method = "HmacSHA256"
stamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
api = "http://api.cmbcloud.com/iaas/"
data_list_gongdan = []
user_list_id = []
data_user_id = []
data_list = []



#function time_value   fix_time
def time_value(time):
    time_a = time
    time_b = time_a[:-1]
    date_time= datetime.strptime(time_b,"%Y-%m-%dT%H:%M:%S")
    #print(date_time)
    fix_time = date_time + timedelta(hours=8)              #type(fix_time) = datetime.datetime
    fix_time = fix_time.strftime("%Y-%m-%d %H:%M:%S")    #  type(fix_time)  =  str
    return fix_time

#excel
#file_path为excel存放绝对路径不指定则和代码一个路径，datas为下面生成的列表名
def data_write(file_path, datas):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
    data = int(len(datas))
    max_row = data
    max_column = 7
    for i in range(data):
        for j in range(max_column):
            sheet1.write(i, j, datas[i][j].decode("unicode-escape"))
    f.save(file_path)




#进行Api操作
def Get_url(action,user=None):
    #user_list_id = []
    api_value =  dict()
    api_value["access_key_id"] = access_key_id
    #api_value["action"] = "RunInstances"
    api_value["action"] = action
    api_value["count"] = count
    api_value["users"] = user
    #api_value["image_id"] = "centos64x86a"
    #api_value["instance_name"] = "demo"
    #api_value["instance_type"] = "small_b"
    #api_value["login_mode"] = "passwd"
    #api_value["login_passwd"] = "QingCloud20130721"
    api_value["signature_method"] = signature_method
    api_value["signature_version"] = signature_version
    api_value["time_stamp"] = stamp
    api_value["version"] = version
    #api_value["vxnets.1"] = "vxnet-0"
    #api_value["zone"] = "zone"
    api_value["zone"] = zone
    #a = sorted(api_value)
    #print(a)
    value_url= ""
    for i in sorted(api_value.keys()):
        value_url += i + "=" + urllib.quote(str(api_value[i])) + "&"
    value_url = value_url[:-1]
    string_to_sign = "GET\n/iaas/\n"+value_url
    #print(string_to_sign)

    h = hmac.new(secret_access_key, digestmod=sha256)
    h.update(string_to_sign)
    sign = base64.b64encode(h.digest()).strip()
    signature = urllib.quote_plus(sign)
    api_url = api + "?" + value_url + "&signature=" + signature
    print(api_url)
    result_json = requests.get(api_url).content
    #print(result_json)
    result_data = json.loads(result_json)
    #result_data = result_json
    #print(type(result_data))
    #print(result_data)
    #result_data = result_data.decode("unicode-escape")

    if api_value["action"] == "DescribeTickets":
        for i in range(100):
            guolue = result_data["ticket_set"][i]["create_time"]
            #print(type(guolue))    #unicode
            guolue = time_value(guolue)
            print(guolue)
            #user_list_id = []
            if now_time in guolue:                    #now_time为当前时间
                data_h = 'root'
                data_a = time_value(result_data["ticket_set"][i]["create_time"])
                #print(type(data_a))
                data_b = result_data["ticket_set"][i]["ticket_id"].encode("unicode-escape").decode("string_escape")
                data_c = "e"
                data_d = result_data["ticket_set"][i]["summary"].encode("unicode-escape").decode("string_escape")
                #print(type(data_d))
                #data_d = data_d1.encode("unicode-escape").decode("string_escape")
                data_e = result_data["ticket_set"][i]["status"].encode("unicode-escape").decode("string_escape")
                #data_e = data_e1.encode("unicode-escape").decode("string_escape")
                #data_e = result_data["ticket_set"][i]["summary"]
                #data_c = time_value(result_data["ticket_set"][i]["status_time"])
                data_f = result_data["ticket_set"][i]["owner"]["user_id"]
                #print(type(data_e))
                #data_a = result_data["ticket_set"][i]["status"]
                print(result_data["ticket_set"][i]["status"]),
                print(time_value(result_data["ticket_set"][i]["create_time"])),
                #print(time_value(result_data["ticket_set"][i]["status_time"])),
                print(result_data["ticket_set"][i]["ticket_id"]),
                print(result_data["ticket_set"][i]["description"]),
                print(result_data["ticket_set"][i]["owner"]["user_id"])
                #user_list_id.append(result_data["ticket_set"][i]["owner"]["user_id"])
                #list_user = user_list_id
                data_list_gongdan.append(data_a[0:10])
                data_list_gongdan.append(data_a[11:16])
                data_list_gongdan.append(data_h)
                data_list_gongdan.append(data_b)
                data_list_gongdan.append(data_c)
                data_list_gongdan.append(data_d)
                data_list_gongdan.append(data_e)
                #data_list_gongdan.append(data_f)
                user_list_id.append(data_f)
                #print(type(a))
            else:
                pass

        print(user_list_id)
        #data_list = data_list_gongdan.decode('unicode_escape')
        print(data_list_gongdan)

            #return user_list_id
    #print(list_user)
    elif api_value["action"] == "DescribeUsers":
        data_g = result_data["user_set"][0]["company_name"].encode("unicode-escape").decode("string_escape")
        #data_user_id
        data_user_id.append(data_g)
    else:
        pass


        #print(result_data["user_set"][0]["company_name"])
    #print(result_data["ticket_set"][0]["status"])
    #print(result_data["ticket_set"][0]["create_time"])
    #print(result_data["ticket_set"][0]["status_time"])
    #print(result_data["ticket_set"][0]["owner"])
    #print(result_data["ticket_set"][0]["ticket_id"])
    #print(result_data["ticket_set"][0]["description"])
    #return value_url


#print(data_list_gongdan)

Get_url('DescribeTickets')

#print(data_list_gongdan)
#print(data_f)


for i in user_list_id:                 #获取公司名称
    Get_url("DescribeUsers",i)
print(data_user_id)



len_data = len(data_list_gongdan)/7
#lendata = len_data + 1



#将data_list_gongdan里面的E换成公司名称
j = 0
for i in range(len_data):
    #print(i)
    data_list_gongdan[j+4] = data_user_id[i]
    j = j + 7
#print(data_list_gongdan)


#替换resolve和in_process为已解决和处理中
for i in range(len(data_list_gongdan)):
    change_resolved = u'已完成'
    change_in_process_open= u'处理中'
    if "resolved" == data_list_gongdan[i]:
        data_list_gongdan[i] = change_resolved.encode("unicode-escape").decode("string_escape")
    elif "in-progress" in data_list_gongdan[i]:
        data_list_gongdan[i] = change_in_process_open.encode("unicode-escape").decode("string_escape")
    elif "open" in data_list_gongdan[i]:
        data_list_gongdan[i] = change_in_process_open.encode("unicode-escape").decode("string_escape")
    else:
        pass
#for i in range(int(len(data_list_gongdan))):
    #data_list_gongdan[i] = str(data_list_gongdan[i])

#将一维列表变成二维
a = 0
while a<int(len(data_list_gongdan)):
    list_a = data_list_gongdan[a:a+7]
    a = a+7
    data_list.append(list_a)
    #print(data_list)
print(data_list)

print(data_list_gongdan)

#生成excel表格

dir = 'Z:\gongdantongji\gongdan_%s.xls'%(now_time)
data_write(dir,data_list)




    #api_value = sorted(api_value.items(), key=operator.itemgetter(0))
    #return api_value
