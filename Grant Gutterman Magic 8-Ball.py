while
welcome_name = input("Welcome to the Magic 8-Ball Code! Please enter your name: ")
print("Hello, " + welcome_name + "!")
question = input("Now what would you like to ask the Magic 8-Ball? ")
import random
answer_list = ["It is certain.","It is decidedly so.","Without a doubt.","Yes - definitely.",
                                "You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.",
                                   "Signs point to yes.","Reply hazy","Try again.","Ask again later.","Better not tell you now.",
                                       "Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.",
                                           "My sources say no.","Outlook not so good.","Very doubtful."]
print(random.choice(answer_list))







