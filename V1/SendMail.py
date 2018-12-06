import smtplib
server = smtplib.SMTP('smtp.qq.com',587)
server.starttls()
server.login('714735333@qq.com','heuxaxqlkmacbfhg')

msg = 'Hello world'
server.sendmail('714735333@qq.com','pandongzi@mbcloud.com', msg)
server.quit()