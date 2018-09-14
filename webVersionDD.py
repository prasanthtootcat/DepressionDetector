import ddFunction as dd
import sys, random
userInput = sys.argv[1]
prediction = dd.depresssion_detect(userInput)

if prediction == 'Suicidal':
    print('<h4><i>You are not alone!<br>There are lot\'s of people who face the same troubles<br>You\'ll feel lot better if you speak to them<br>visit </i><a href="https://www.7cups.com">Anonymous chat group</a></h4>')
elif prediction == 'Not depressed':
    print('<h4><i>Have a great day!</i></h4>')
else:
    quotes = ['Keep going...<br>everything will come to you at the perfect time','You are deserving of the most pure,<br>wholesome, and authentic love.<br>I hope you know that','When you can\'t find the sunshine,<br>be the sunshine','You\'ve been through the worst<br>You are the best!','Hey little fighter<br>Soon things will be brighter!','Do not believe the things you tell yourself<br>when you are sad','You go through the worst<br>Only to hit the best!']
    print('<h2 class="text-muted"><i>"'+quotes[random.randrange(7)]+'"</i></h2>')