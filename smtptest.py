import smtplib
from email.mime.text import MIMEText
smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
smtpobj.set_debuglevel(True)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.ehlo()
smtpobj.login("new.conference.2020@gmail.com", "uecnewconf")

# 送受信先
to_email = "interior5471@gmail.com"

# MIMEの作成
subject = "テストメール"
message = "テストメール"
msg = MIMEText(message, "html")
msg["Subject"] = subject
msg["To"] = to_email
msg["From"] = "new.conference.2020@gmail.com"

smtpobj.send_message(msg)
smtpobj.quit()
