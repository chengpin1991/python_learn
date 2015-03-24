#-*- coding: utf-8 -*-
'''
	发送带附件的邮件，首先要创建MIMEMultipart()实例，然后构造附件，如果有多个附件，可依次构造
	send email with attachments
'''
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage 
from smtplib import SMTP

msg = MIMEMultipart()

#构造附件1和附件2
att1 = MIMEText(open('C:\\Users\\chengpin.FUNSHION\\Desktop\\mac.txt', 'rb').read(), 'base64', 'utf-8')
att1['Content-Type'] = 'application/octet-stream'
att1['Content-Disposition'] = 'attachment; filename="mac.txt"' #filename可以任意写，写什么，邮件就显示什么名字
msg.attach(att1)

att2 = MIMEText(open(u'C:\\Users\\chengpin.FUNSHION\\Desktop\\OTT\\亿播盒子测试用例.xlsx', 'rb').read(), 'base64', 'utf-8')
att2['Content-Type'] = 'application/octet-stream'
att2['Content-Disposition'] = 'attachment; filename="亿播盒子测试用例.xlsx"'
msg.attach(att2)



#以附件的形式加入图片
image = MIMEText(open(u'C:\\Users\\chengpin.FUNSHION\\Desktop\\QQ图片20150316143524.png', 'rb').read(), 'base64', 'utf-8')
image['Content-Type'] = 'application/octet-stream'
image['Content-Disposition'] = 'attachment; filename="QQ图片20150316143524.png"'
msg.attach(image)

image2 = MIMEImage(open(u'C:\\Users\\chengpin.FUNSHION\\Desktop\\QQ图片20150316143524.png', 'rb').read())
image2.add_header('Content-ID', '<image1>')
msg.attach(image2)

#用户名后缀，要与smtp_host保持一致，才能登陆成功
from_user = "***@***"
from_password = "******"
smtp_host = "*******"
mailto_list = ['****@****']

content_html = '''
<a href="http://www.baidu.com">hehe</a>
'''
content_text = 'please open file with mode, otherwise you will can not open the file in email'

def send_email(mailto_list, subject, content, html):
	content = MIMEText(content, _subtype='plain', _charset='utf-8')
	msg.attach(content)
	content_html = MIMEText(html, _subtype='html', _charset='utf-8')
	msg.attach(content_html)
	#加邮件头
	msg['To'] = ";".join(mailto_list)
	msg['From'] = from_user
	msg['Subject'] = subject
	connection = SMTP()
	connection.connect(smtp_host, 25)
	connection.login(from_user, from_password)
	connection.sendmail(from_user, msg['To'], msg.as_string())
	connection.close()

if __name__ == '__main__':
	send_email(mailto_list, 'email with attachments', content_text, content_html)

