#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import requests
import paramiko
import time
import sys
import os
import smtplib
from email.mime.text import MIMEText

class Restart(object):


    def __init__(self,ip,port):
        self.ip=ip
        self.port=port
        time_format = "%Y-%m-%d %X"
        self.time_current = time.strftime(time_format)
        self.username="root"
    def interface_test(self):
        url = "http://%s:%s/card/cardValidate" % (self.ip, self.port)
        payload = "{\"cardNum\":\"2787504611\",\"companyId\":\"181\"}"
        headers = {
            'Content-Type': "application/json",
            'token': "2951314e0796466EE5c36ae737566128",
            'cache-control': "no-cache"
        }

        response = requests.request("POST", url, data=payload, headers=headers).text
        response=eval(response)
        if int(response['code']) ==200:
            return True
        else:
            return False

    def SSHClient(self):
        print('%s: ssh %s@%s ...'%(self.time_current,self.username,self.ip))
        try:
            private_key=paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
            self.ssh=paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            self.ssh.connect(hostname=self.ip,port=22,username=self.username,pkey=private_key)
            print('%s: ssh %s@%s success!'%(self.time_current,self.username,self.ip))
        except Exception as e:
            print('%s: ssh %s@%s failed :%s'%(self.time_current,self.username,self.ip,e))
        sys.exit(0)

    def exec_command(self,cmd):
        print('%s:command:%s'%(self.time_current,cmd))
        stdin,stdout,stderr=self.ssh.exec_command(cmd)
        res,err=stdout.read(),stderr.read()
        result=res if res else err
        print('%s: %s'%(self.time_current,result.decode()))
        return result

    def stop_tomcat(self,tomcat_home):
        print('%s : ready to stop tomcat ,path:%s...'%(self.time_current,tomcat_home))
        tomcat_pid = self.exec_command(
            'ps aux|grep ' + tomcat_home + '|grep -v grep|grep java|grep -v restart|awk \'{print $2}\'')
        self.exec_command('kill -9 '+tomcat_pid)
        print('%s : stop tomcat success...'%self.time_current)

    def start_tomcat(self,tomcat_home):
        print('%s : ready to start tomcat,path:%s...'%(self.time_current,tomcat_home))
        self.exec_command('sh '+tomcat_home+'/bin/startup.sh')


def restart_local(time_current,ip,port,tomcat_home):
    print('%s : ready to stop tomcat ,path:%s...' % (time_current, tomcat_home))
    pid = str(
        int(os.popen('ps aux|grep'+tomcat_home+'|grep -v grep|grep java|grep -v restart|awk \'{print $2}\'').read()))
    os.popen('kill -9 ' + pid)
    print('%s : stop tomcat success...' % time_current)
    print('%s : ready to start tomcat,path:%s..' % (time_current, tomcat_home[0]))
    os.popen('sh ' + tomcat_home + '/bin/startup.sh')
    test_alive(time_current,ip,port,tomcat_home)


def test_alive(time_current,ip,port,tomcat_home):
    test = Restart(ip, port)
    for i in range(100):
        result = test.interface_test()
        if result == True:
            print("%s : tomcat,path:%s is running success..." % (time_current, tomcat_home))
            break
        else:
            i += 1
            if i > 50:
                print("%s : tomcat,path:%s is starting slowly..." % (time_current, tomcat_home))
            elif i == 99:
                print("%s : warning:start tomcat(%s) overtime,the thread has closed...see email later.." % (time_current,tomcat_home))
                from_ = "562605133@qq.com"  # 你的邮箱   发件地址
                to_ = '562605133@qq.com'  # 收件地址
                subject = '重启服务器'  # 邮件标题
                text = time_current + '重启ip:%s,port:%s失败，已停止后面的重启'%(ip,port)  # 邮件内容
                SendEmail(from_, to_, subject, text)
                sys.exit()
            else:
                time.sleep(10)


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




if __name__=='__main__':
    '''全局变量'''
    time_format = "%Y-%m-%d %X"
    time_current = time.strftime(time_format)
    ip_list=['39.104.13.49','39.104.137.176']
    tomcat_home=['/root/tomcat-7.0.57_01','/root/tomcat-7.0.57_02']

    '''重启本机 39.104.13.49 7001'''
    restart_local(time_current,ip_list[0],7001,tomcat_home[0])
    '''重启本机 39.104.13.49 7002'''
    restart_local(time_current,ip_list[0],7002,tomcat_home[0])

    '''登录 39.104.137.176'''
    restart = Restart(ip_list[1], 7001)
    restart.SSHClient()

    '''重启远程主机 39.104.137.176 7001'''
    restart.stop_tomcat(tomcat_home[0])
    restart.start_tomcat(tomcat_home[0])
    test_alive(time_current,ip_list[1],7001,tomcat_home[0])
    '''重启远程主机 39.104.137.176 7002'''
    restart.start_tomcat(tomcat_home[1])
    restart.start_tomcat(tomcat_home[1])
    test_alive(time_current,ip_list[2],7002,tomcat_home[1])
    restart.ssh.close()

    from_ = "562605133@qq.com"  # 你的邮箱   发件地址
    to_ = '562605133@qq.com'  # 收件地址
    subject = '重启服务器'  # 邮件标题
    text = time_current+'重启所有成功'  # 邮件内容
    SendEmail(from_, to_, subject, text)








