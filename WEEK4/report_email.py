#!/usr/bin/env python3

import os
import datetime
import emails
import reports
import sys

def main(argv):
    attachment='tmp/processed.pdf'
    descr_dir = "supplier-data/descriptions/"
    paragraph=''
    title = 'Processed Update on '+  datetime.date.today().strftime("%B %d, %Y")
    files_txt = [fn for fn in os.listdir(descr_dir) if fn.endswith('.txt')]
    for file in files_txt:
        file_name, file_ext = file.split('.')
        with open(descr_dir+file, 'r') as fl:
            paragraph += 'name: ' + fl.readline() + '<br/>'
            paragraph += 'weight: ' + fl.readline() + '<br/>'
            paragraph +='<br/><br/>'
    print(paragraph)
    reports.generate_report(attachment, title, paragraph)

    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    em = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(em)
    

        


if __name__ == "__main__":
  main(sys.argv)