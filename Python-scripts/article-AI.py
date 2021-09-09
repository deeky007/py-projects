Get started
Open in app


Open in app


You have 2 free member-only stories left this month. Sign up for Medium and get an extra one

10 Python mini-projects that everyone should build (with codes)
Best mini projects for python that you can find on the internet today
Abhay Parashar
Abhay Parashar

Sep 28, 2020·5 min read



Photo by David Clode on Unsplash
Hi there, I am Abhay
We are in 2020. we all know that the industry is growing day by day. if you see from 2013 to 2019 the growth of python in the industry is around 40% and it is said that it will grow up to 20% more in the next few years. the increased rate of python developers is increased by 30% in the past few years.so there is no better time for learning python and to learn python there is no better way than doing projects.
In this blog, we will create 10 python mini-projects.
Dice roll simulator
Guess the number game
Random password generator
Binary search
Sending emails using python
Medium Article Reader
Alarm clock
URL shortener
Weather app
Key logger

Photo by Riz Mooney on Unsplash
Dice roll simulator
The goal is to create a program that will simulate the roll of dice.
Topics: random module, looping, and if-else
Hint: Using a random module generate a random number between the range from 1 to 6 when the user wants.
GIVE A TRY ON YOUR OWN
import random 
while True:     
     print(''' 1. roll the dice             2. exit     ''')    
     user = int(input("what you want to do\n"))     
     if user==1:         
        number = random.randint(1,6)         
        print(number)     
     else:         
        break
Guess the number game
The main goal of the project is to create a program that randomly select a number in a range then the user has to guess the number. user has three chances to guess the number if he guess correct then a message print saying “you guess right “otherwise a negative message prints.
Topics: random module, for loop, f strings
GIVE A TRY ON YOUR OWN
import random
number = random.randint(1,10)
for i in range(0,3):
    user = int(input("guess the number"))
    if user == number:
        print("Hurray!!")
        print(f"you guessed the number right it's {number}")
        break
if user != number:
    print(f"Your guess is incorrect the number is {number}")
Random password generator
To create a program that takes a number and generate a random password length of that number.
Topics: random module, joining strings, taking input
Hint: Create a string with all characters, then take random characters from it and concatenate each char to make a big string.
GIVE A TRY ON YOUR OWN
import random
passlen = int(input("enter the length of password"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p =  "".join(random.sample(s,passlen ))
print (p)
Binary search
The goal of binary search is to search whether a given number is present in the string or not.
Topics: list,sorting,searching
Hint: First Check whether it is present in the middle or not then check for front and rear.
GIVE A TRY ON YOUR OWN
lst = [1,3,2,4,5,6,9,8,7,10]
lst.sort()
first=0
last=len(lst)-1
mid = (first+last)//2
item = int(input("enter the number to be search"))
found = False
while( first<=last and not found):
    mid = (first + last)//2
    if lst[mid] == item :
         print(f"found at location {mid}")
         found= True
    else:
        if item < lst[mid]:
            last = mid - 1
        else:
            first = mid + 1 
   
if found == False:
    print("Number not found")
Sending emails using python
To create a python script that can send emails
Topics: import packages, SMTP lib, sending a request to the server
GIVE A TRY ON YOUR OWN
import smtplib 
from email.message import EmailMessage
email = EmailMessage() ## Creating a object for EmailMessage
email['from'] = 'xyz name'   ## Person who is sending
email['to'] = 'xyz id'       ## Whom we are sending
email['subject'] = 'xyz subject'  ## Subject of email
email.set_content("Xyz content of email") ## content of email
with smtlib.SMTP(host='smtp.gmail.com',port=587)as smtp:     
## sending request to server 
    
    smtp.ehlo()          ## server object
smtp.starttls()      ## used to send data between server and client
smtop.login("email_id","Password") ## login id and password of gmail
smtp.send_message(email)   ## Sending email
print("email send")    ## Printing success message

Photo by Fab Lentz on Unsplash
Medium Article Reader
The task is to create a script that can read articles from a link.
Topics: web scraping, text to speech
Hint: Take the URL of the article as input, scrape the text from the link and then pass it to text to speech.
GIVE A TRY ON YOUR OWN
import pyttsx3
import requests
from bs4 import BeautifulSoup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
  engine.say(audio)
  engine.runAndWait()
text = str(input("Paste article\n"))
res = requests.get(text)
soup = BeautifulSoup(res.text,'html.parser')
articles = []
for i in range(len(soup.select('.p'))):
    article = soup.select('.p')[i].getText().strip()
    articles.append(article)
text = " ".join(articles)
speak(text)
# engine.save_to_file(text, 'test.mp3') ## If you want to save the speech as a audio file
engine.runAndWait()