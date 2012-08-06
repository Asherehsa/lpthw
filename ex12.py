#Asking Questions #11
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

#Prompting People #12
y = raw_input("Name? ") #This prompts the user with "Name?" and puts the result into the variable y. This is how you ask someone a question and get their answer.
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input ("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)