'''

Question41:
Write a program which accepts a string as input to print "Yes" 
if the string is "yes" or "YES" or "Yes", otherwise print "No". 

'''

while True:
    s = input("enter string ->")
    if s:
        if s in [ 'yes','YES','Yes']:
            print("Yes")
        else:
            print('No')
    else:
        break
