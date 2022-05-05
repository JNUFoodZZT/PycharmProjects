import smtplib
from email.mime.text import MIMEText
from email.header import Header
smtp_obj = smtplib.SMTP_SSL("smtp.exmail.qq.com",465)
smtp_obj.login("6210113257@stu.jiangnan.edu.cn","Zzt20140224")

mail_body ='''
1
'''


msg = MIMEText(mail_body,"html","utf-8")
msg["From"] = Header("from jiangnan","utf-8")
msg["To"] = Header("hfut","utf-8")
msg["Subject"] = Header("testify",'utf-8')

smtp_obj.sendmail("6210113257@stu.jiangnan.edu.cn",["imaphz.qiye.163.com","2017214435@mail.hfut.edu.cn"],msg.as_string())