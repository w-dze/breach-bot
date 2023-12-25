#Breach Bot Starter Code
breachYear = 2019

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) +
      " years since the Facebook data breach.")

#Introduces breach
print("Would you like to learn about the Facebook data breach in 2019?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
    print(
        "What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, (c) I would like to hear your reflection."
    )
    topic = input()

    if topic.lower() == "a":
        print("Malicious actors scraped personal information from around 533 million Facebook users from 106 countries by exploiting a vulnerability in the feature that allows users to find each by phone number. This personal information includes phone numbers, full names, locations, email addresses, and other details provided in the user profile.")

    elif topic.lower() == "b":
        print("Facebook’s spokesperson claims they found and fixed the issue in August 2019 and do not plan to notify the users individually. In July 2019, Facebook reached a five billion settlement with the US Federal Trade Commission for violating an agreement about protecting user privacy.")

    elif topic.lower() == "c":
        break
      
    else:
        print("Sorry, I didn't catch that. Choose one of the options listed.")

    input("Press enter to continue\n")


#Introduces my take
print("\nI am excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
    print(
        "What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to the CIA Triad, (b) my reaction, (c) my advice, or (d) none."
    )
    topic = input()

    if topic.lower() == "a":
        print("This data leak connects to confidentiality because personal information was leaked from the user profile, which damages the confidentiality of private information.")

    elif topic.lower() == "b":
        print("We disagree with the organization's response because Facebook could have notified the users whose information was leaked immediately after the breach.")

    elif topic.lower() == "c":
        print("I would convince victims to take action by informing them that even the smallest personal information can threaten our privacy. I advise monitoring for any suspicious activity on online platforms connecting with phone numbers and email addresses.")

    elif topic.lower() == "d":
        break
      
    else:
        print("Sorry, I didn't catch that. Choose one of the options listed.")

    input("Press enter to continue\n")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")
