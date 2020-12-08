#!/usr/bin/env python3

import shutil
import psutil
import emails
import socket


CPU_THRESHOLD = 80.0 # 80%
MEM_THRESHOLD = 500 * 1024 * 1024  # 500MB (available)
DISK_USAGE_THRESHOLD = 80 # 80% (percent)

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = ''
body = 'Please check your system and resolve the issue as soon as possible.'

cpu = psutil.cpu_percent(interval=1)
mem = psutil.virtual_memory()
disk = psutil.disk_usage('/')
try:
    lh = socket.gethostbyname('localhost')
except Exception:
    #no hay localhost
    subject='Error - localhost cannot be resolved to 127.0.0.1'

if mem.available <= THRESHOLD:
    subject = 'Error - Available memory is less than 500MB'
if cpu >= CPU_THRESHOLD:
    subject = 'Error - CPU usage is over 80%'
if disk.percent >= DISK_USAGE_THRESHOLD:
    subject = 'Error - Available disk space is less than 20%'

if subject is not '':
    em=emails.generate_email_error_report(sender, receiver, subject, body)
    send_email(em)



