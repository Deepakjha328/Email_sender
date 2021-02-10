import smtplib
from email.message import  EmailMessage
from string import Template #html template show to you program
from pathlib import Path #access you template

html =Template(Path('index.html').read_text())
email=EmailMessage()
email['from'] = '#your emailname'
email['to']  = '#use receiver password'
email['subject'] ='send something'


email.set_content(html.substitute({'name':'html subtitute'}),'html') #add ing subtitue to add text in html file


with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('#use your sender email','sender password')
    smtp.send_message(email)
    print('Done!')

