#!/usr/bin/python
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # 
# auto: Tiago de Souza Moraes
# http://teago.futuria.com.br
#
# Teimoso IP - Sendmail to admin when Internet IP change
# https://github.com/teagom/teimoso
# 
# Python 2.7 and urlllib2
# # # # # # # # # # # # # # # # # # # # #

import urllib2
import time
from os import path
from settings import sender, to, subject, smtpserver, username, password, log, again

from smtplib import SMTP_SSL as SMTP
from email.MIMEText import MIMEText


def sendmail(ipc):
    print "--- Sendmail" 

    msg = MIMEText(ipc, 'plain')
    msg['Subject'] = subject
    msg['From'] = sender

    r = False

    while r == False:
        """
            Why while?

            IP change but:
                smtp server error
                internet error
                others
        """

        try:
            conn = SMTP(smtpserver)
            conn.set_debuglevel(False)
            conn.login(username, password)
            conn.sendmail(sender, to, msg.as_string())
            conn.close()
            r = True # success
            print '- Success! A e-mail was sent'
        except:
            print '- Error sending e-mail...'
            time.sleep(again) # try again in seconds


def write_log(fl,ip):
    print "- Store new Internet IP"
    fl = open(log,"w")
    fl.write(ip)
    fl.close()
    return fl


def read_log(fl):
    print "- Get last Internet IP"
    fl = open(log,"r")
    content = fl.read()
    fl.close()
    return content


def get_current_ip():
    print "- Get current Internet IP"
    url = urllib2.urlopen("http://api.ipify.org") # return internet IP plain text
    r = url.read()
    url.close()
    return r


# # # # # # # # #
# main code 
# # # # # # # # #

print '--- Checking internet IP'
ipc = get_current_ip()

# check IP change
if path.isfile(log): # file log exit? first time no exist.
    ipl = read_log(log) # ipl = last ip stored

    if not ipl == ipc :
        sendmail(ipc)
        write_log(log,ipc) # store new IP in log tile.
        print '- Internet IP change'
    else:
        print '- Internet IP not change'

else: # not last log, sendmail and store ip.
    print "- Non exist last IP"
    write_log(log,ipc)
    sendmail(ipc)
