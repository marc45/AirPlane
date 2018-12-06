import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromAddr = '714735333@qq.com'
myPass = 'heuxaxqlkmacbfhg'
toAddr = 'pandongzi@mbcloud.com'

msg = MIMEMultipart()
msg['From'] = fromAddr
msg['To'] = toAddr
msg['Subject'] = 'Hello World!'

body = 'Hello world!'
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


i = 3
while i >0:
    server.send_message(msg)
    i = i-1
server.quit()