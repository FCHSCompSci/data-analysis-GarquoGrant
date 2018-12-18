#Imports

import random
import time

#Answer Inputting

answer_list = ["It is certain.","It is decidedly so.","Without a doubt.","Yes - definitely.",
                                "You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.",
                                   "Signs point to yes.","Reply hazy","Try again.","Ask again later.","Better not tell you now.",
                                       "Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.",
                                           "My sources say no.","Outlook not so good.","Very doubtful."]

reply = print(random.choice(answer_list))

#Program

name = input("Welcome to the Magic 8-Ball Code! Please enter your name: ")
print("Hello, %s!" % name)
while True
question = input("What would you like to ask the Magic 8-Ball? Type 'No' to leave. ")

if question != "No":
    print(reply)
else:
    print ("K den peace bro!")









