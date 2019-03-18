import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys, requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=1&ref_=adv_nxt"

response = requests.get(url)

content = response.content

soup = BeautifulSoup(content, "html.parser")

movieNumbers = list()
movieNames = list()
movieDates = list()

old = 1
new = 51

for f in range(5):
    for header in soup.find_all("h3", {"class": "lister-item-header"}):
        for numbers in header.find_all("span", {"class": "lister-item-index unbold text-primary"}):
            movieNumbers.append(numbers.text)
        for names in header.find_all("a"):
            movieNames.append(names.text)
        for dates in header.find_all("span", {"class": "lister-item-year text-muted unbold"}):
            movieDates.append(dates.text)

    
    url = url.replace("start=" + str(old), "start=" + str(new))
    old = new
    new += 50




message = MIMEMultipart()

message["From"] = "gloriaainn@gmail.com"
message["To"] = "okantpl@icloud.com"
message["Subject"] = "Trying to send e-mail with SMTP"

content = """## IMDb Top 250 ##

"""
start = time.time()
for f in zip(movieNumbers, movieNames, movieDates):
    infos = f[0] + f[1] + " " + f[2] + "\n"
    content = content + infos

finish = time.time()

content = content + "\n\n" + "This process has been" + float(finish - start)
content = content + "\n\n" + str(datetime.today())
print(content)


# messageBODY = MIMEText(content, "plain")
# message.attach(messageBODY)


# for f in range(10):

#     try:
#         mail = smtplib.SMTP("smtp.gmail.com", 587)

#         mail.ehlo()

#         mail.starttls()

#         mail.login("gloriaainn@gmail.com", "1q2w3e4rA")

#         mail.sendmail(message["From"], message["To"], message.as_string())

#         print("Mail sent succesfuly!")

#         mail.close()

#     except:
#         sys.stderr.write("An error occured!")
#         sys.stderr.flush()