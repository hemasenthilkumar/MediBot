import smtplib
def send_mail(message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("hemapriya.2019@vitstudent.ac.in", "--")
    s.sendmail("hemapriya.2019@vitstudent.ac.in", "hemapriya.2019@vitstudent.ac.in",
    message)
    s.quit()
