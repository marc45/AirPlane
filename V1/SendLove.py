import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def plove():
    sentence = "Dear,LoveYouForever!️"
    for char in sentence.split():
       allChar = []
       for y in range(12, -12, -1):
           lst = []
           lst_con = ''
           for x in range(-30, 30):
                formula = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
                if formula <= 0:
                    lst_con += char[(x) % len(char)]
                else:
                    lst_con += ' '
           lst.append(lst_con)
           allChar += lst
    return '\n'.join(allChar)


fromAddr = '714735333@qq.com'
myPass = 'heuxaxqlkmacbfhg'
toAddr = 'pandongzi@mbcloud.com'

msg = MIMEMultipart()
msg['From'] = fromAddr
msg['To'] = toAddr
msg['Subject'] = 'Dear Miao~!'

body = plove()
msg.attach(MIMEText(body))

# with open('/Users/winterson/Desktop/abc.xlsx', 'rb') as f:
#     # 设置附件的MIME和文件名，这里是xlsx类型:
#     mime = MIMEBase('excel', 'xlsx', filename='abc.xlsx')
#     # 加上必要的头信息:
#     mime.add_header('Content-Disposition', 'attachment', filename='abc.xlsx')
#     mime.add_header('Content-ID', '<0>')
#     mime.add_header('X-Attachment-Id', '0')
#     # 把附件的内容读进来:
#     mime.set_payload(f.read())
#     # 用Base64编码:
#     encoders.encode_base64(mime)
#     # 添加到MIMEMultipart:
#     msg.attach(mime)

server = smtplib.SMTP('smtp.qq.com',587)
server.starttls()
server.login(fromAddr,myPass)


server.send_message(msg)
server.quit()
