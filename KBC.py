questions = [
    ["1.NetBIOS was introduced in 1983 by which company as an improvement to the standard BIOS used by Windows-based computers?","a).DELL","b).IBM","c).Compaq","d).Sytek Inc", 4],
    ["2.Which company had developed the software development process framework called \"Rational Unified Process\" or RUP?","a).Microsoft","b).IBM","c).Compaq","d).None", 2],
    ["3.A hybrid computer is the one which exhibits the features of __?","a).Analog Coumputer","b).Digital Computer","c).Both Analog and Digital Computer","d).Mainframe Computer",3],
    ["4.For which of the following, the term Knowledge Based Information processing System is being used in recent times","a).Fourth Generation Coumputers","b).Fifth Generation Coumputers","c).Sixth Generation Coumputers","d).Super Computers",2],
    ["5.Which of the following generation of computers is associated with artificial intelligence?","a).First","b).Third","c).Fifth","d).Ninth",3],
    ["6.The performance of a hard drive or other storage device, meaning how long it takes to locate a file is called ?","a).Response Time","b).Access Time","c).Quick Time","d).None of the above",2],
    ["7.A unit of data storage that equals 2 to the 70th power is called?","a).Zebibyte","b).Yottabyte","c).Yobibyte","d).None of the above",1],
    ["8.A generic name for Intel processors released after the original 8086 processor is ______?","a).Pentium","b).x86","c).Pentium 286","d).None of these",2],
    ["9.V-RAM is used for access of the following?","a).Video & Graphics","b).Text & Images","c).Programs","d).Videos only",1],
    ["10.Any piece of data can be returned in a constant time, regardless of its physical location and whether or not it is related to the previous piece of data using which of the following?","a).RAM","b).ROM","c).CPU","d).BIOS",1],
    ["11.Which among the following is not a security / privacy risk?","a).Phising","b).Spam","c).Virus","d).Hacking",2],
    ["12.Now a days Vishing has become a criminal practice of using social engineering over which of the following?","a).Social Networking Sites","b).E-Mails","c).Mobile Phones","d).Cyber Crimes",3],
    ["13.When some unidentified / unknown person / firm sends you mail in a trustworthy /lucrative way asking for sensitive banks and online payment information, this is a case of __?","a).Spam","b).Vishing","c).Hacking","d).Phising",4],
    ["14.Most of the internet banking sites provide which of the following feature to reduce the risk of keystroke logging for the password entry?","a).Finger Touching","b).Virtual Keyboard","c).ShapeWriter","d).Touch Typing",2],
    ["15.A network that is connected to the Internet, but uses encryption to scramble all the data sent through the Internet is called ?","a).Virtual Private Network","b).Social Network","c).Local Area Network","d).Internet",1],
    ["16.The terms Goodput, Throughput and Maximum throughput are most closely associated with which among the following in computers?","a).Bit Rate","b).Response Time","c).Command Line Interface","d).Random Memory",1],
    ["17.Which one of the following is a discontinued computer network operating system developed by Novell Inc.?","a).Novellware","b).Netware","c).IPX Network","d).NovnetX",2]
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000,75000000]
    
money = 0
# printing questions
for i in range(0,len(questions)):
    question = questions[i][0]
    print(f"Question for Rs. {levels[i]}:\n",question)
    
    #printing options for questions
    for j in range(1, 5):
        print(questions[i][j])
    
    #Taking input for answer and checking for correct answers
    ans = int(input("Enter correct option, Ex- 1 for a, 2 for b, 3 for c, 4 for d or 0 to quit: "))
    if (ans == 0):
        break

    if (i==4):
        money = levels[i]
    elif (i==9):
        money = levels[i]
    elif (i==14):
        money = levels[i]
    elif (i == 16):
        money = levels[i]
        
    print(f"The money is: ", money)

    if ans != questions[i][5]:
        print("You have entered a wrong answer, You are out now.")
        break
    else:
        print("Correct Answer")

if (money == 0) :
    print(f"Better luck next time. You have won nothing.")

else:
    print(f"Congratulations, Your take home money is {money}")
# print(f"Congratulations, Your take home money is {money}")