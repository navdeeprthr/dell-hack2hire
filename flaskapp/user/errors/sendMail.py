import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail():

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
                connection.login(
                        user='your email',
                        password='password generate it from settings and then app password'
                )

                connection.sendmail(
                        from_addr='your email',
                        to_addrs='receiver address',
                        msg=f"Subject:Database error\n\n"
                        f"DataBase is showing 500"
                )