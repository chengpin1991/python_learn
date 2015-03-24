#-*- coding: utf-8 -*-
'''
send text or html email
'''
from smtplib import SMTP
from email.mime.text import MIMEText
mailto_list = ['chengpin@fun.tv', 'zhengxc@fun.tv']
mail_host = "mail.funshion.com:25"
mail_user = "chengpin"
mail_password = "1q2w3e4r!"
mail_suffix = "@funshion.com"

#subject:主题
#邮件组成：发件人，收件人，主题，邮件内容，附件等
def send_mail(to_list, subject, content):
	from_user = mail_user + mail_suffix
	# msg = MIMEText(content, _subtype='plain', _charset='utf-8') #text邮件
	msg = MIMEText(content, _subtype='html', _charset='utf-8') #html邮件
	msg['From'] = from_user
	msg['To'] = ";".join(mailto_list)
	msg['Subject'] = subject
	connection = SMTP() #需要实例化一个SMTP的对象
	connection.connect(mail_host)
	connection.login(from_user, mail_password)
	connection.sendmail(from_user, mailto_list, msg.as_string())
	connection.close()

if __name__ == '__main__':
	# send_mail(mailto_list, 'test', 'just for testing')#text邮件
	send_mail(mailto_list, 'test_html', '<a href="http://www.baidu.com">hehe</a>') #html邮件