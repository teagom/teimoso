# Teimoso
python script - sendmail when internet ip change adsl

# Install
$ cd /usr/local

$ git clone https://github.com/teagom/teimoso.git

$ cd teimoso

$ cp settings.py.DIST settings.py

$ chmod 700 teimosoIP.py settings.py

# change settings, smtp,user,subject and others.
$ vim settings.py

# crontab / Check for each 00 minutes
$ vim /etc/crontab

00 *    * * *   root     /usr/local/teimoso/teimosoIP.py

# Test first time
$ cd /usr/local/teimoso

$ ./teimosoIP.py

# Test change IP
$ echo "LIXO" > /tmp/out.log

# Test reset
$ rm /tmp/out.log
