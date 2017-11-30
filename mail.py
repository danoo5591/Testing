# -*- coding: utf-8 -*-

import sys
import smtplib

SERVER = "localhost"
FROM = "sender@example.com"
TO = ["danilo.amaral@montevideo.com.uy"] # must be a list
SUBJECT = "Hello!"
TEXT = "This message was sent with Python's smtplib."

message = lambda frm, to, subject, text: """\
From: %s
To: %s
Subject: %s

%s
""" % (frm, ", ".join(to), subject, text)

def send(server, frm, to, subject, text):
	try:
		if type(to) is not list:
			to = [to]
		server = smtplib.SMTP(server)
		server.sendmail(frm, to, message(frm, to, subject, text))
		server.quit()
	except smtplib.SMTPException as e:
		print e.message


def main(argv):
	send(SERVER, FROM, TO, SUBJECT, TEXT)


if __name__ == '__main__':
    try:
        sys.exit(main(sys.argv))
    except Exception as e:
        print('ERROR.init: ' + e.message, 'error')
        raise