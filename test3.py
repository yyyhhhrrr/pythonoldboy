#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import smtplib
from email.mime.text import MIMEText


import time

time_format = "%Y-%m-%d %X"
time_current = time.strftime(time_format)


def SendEmail(fromAdd, toAdd, subject, text):
    _pwd = "lobhxvlvxnadbfeb"  # 授权码

    msg = MIMEText(text)
    msg["Subject"] = subject
    msg["From"] = fromAdd
    msg["To"] = toAdd
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(fromAdd, _pwd)
        s.sendmail(fromAdd, toAdd, msg.as_string())
        s.quit()
        print("Success!")
    except smtplib.SMTPException:
        print('Falied!')


if __name__ == '__main__':
    from_ = "562605133@qq.com"  # 你的邮箱   发件地址
    to_ = '562605133@qq.com'  # 收件地址
    subject = '重启服务器'  # 邮件标题
    text =time_current+'成功'  # 邮件内容
    SendEmail(from_, to_, subject, text)
