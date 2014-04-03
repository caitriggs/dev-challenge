# Exercises for chapter 3:

# Name: Cait

#Exercise 3.1:
'''
NameError: name 'repeat_lyrics' is not defined
'''

#Exercise 3.2:
'''
ABC
ABC
ABC
ABC
'''

#Exercise 3.3:
print "Exercise 3.3"

def right_justify(s):
	print '{:>70}'.format(s)
	length = "(The length of the text above is %s characters including spaces)" %len(s)
	print '{:>70}'.format(length)

right_justify('This is right justified to column 70')
print '' #break line between exerciese
#source: https://docs.python.org/2/library/string.html#formatspec

#Exercise 3.4:
#Exercise 3.4.2
def do_twice(f, printString):
    f(printString)
    f(printString)

#Exercise 3.4.3
def print_twice(printString):
    print printString
    print printString

print "Exercise 3.4.4"
do_twice(print_twice, 'spam')
print '' #break between next function print

print "Exercise 3.4.5"
def do_four(f, printString):
    do_twice(f, printString)
    do_twice(f, printString)

do_four(print_twice, 'spam')
print '' #break line between exerciese



