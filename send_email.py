import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "nirmol882@gmail.com"
    password = "wbmdjswuriuujcun"
    reciever = "nirmol882@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)
