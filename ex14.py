#Prompting and passing
from sys import argv

script, username = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (username, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % username
likes = raw_input(prompt)

print "Where do you live %s?" % username
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me. You live in %r. Not sure where that is. And you have an %r computer. Nice. """ % (likes, lives, computer)