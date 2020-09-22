import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("malliksiddharth@gmail.com", "password")
server.sendmail("souravmohanty0077@gmail.com", "priyankamahaku31@gmail.com", "dreed31@gmail.com", "Hello,whatup!")
server.quit()