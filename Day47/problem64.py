'''
Question:
Please write assert statements to verify that every number in the list [2,4,6,8] is even.
Hints:
Use "assert expression" to make assertion.

'''

linput = input("enter a  list of numbers -->").split(',') 
li= [ int(i) for i in  linput]
#li = [2,4,6,8] ##ouput #is even. #no input requiered
filtred = list(filter(lambda x: (x%2==0) or (x<=2),li))
##ouput
a = [str(i) for i in filtred]
if a:
    print(f"{ ','.join(a) } is even.")
else: 
    print(f"list is odd.")