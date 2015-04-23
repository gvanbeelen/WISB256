print('What is your name?')
yourName=input()
print('How many greetings?')
number=int(input())
for i in range(number):
    print ('Hello, ' + yourName + '!')