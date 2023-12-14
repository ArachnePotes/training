'''
Question 24
Level 1

Question:
    Python has many built-in functions, and if you do not know how to use it, 
    you can read document online or find some books. 
    But Python has a built-in document function for every built-in functions.
    Please write a program to print some Python built-in functions documents,
    such as abs(), int(), raw_input()
    And add document for your own function
    
Hints:
    The built-in document method is __doc__
'''

pyf = {
    "abs":abs.__doc__,
    "aiter":aiter.__doc__,
    "all":all.__doc__,
    "anext":anext.__doc__,
    "any":any.__doc__,
    "ascii":ascii.__doc__,
    "bin":bin.__doc__,
    "bool":bool.__doc__,
    "breakpoint":breakpoint.__doc__,
    "bytearray":bytearray.__doc__,
    "bytes":bytes.__doc__,
    "callable":callable.__doc__,
    "chr":chr.__doc__,
    "classmethod":classmethod.__doc__,
    "compile":compile.__doc__,
    "complex":complex.__doc__,
    "delattr":delattr.__doc__,
    "dict":dict.__doc__,
    "dir":dir.__doc__,
    "divmod":divmod.__doc__,
    "enumerate":enumerate.__doc__,
    "eval":eval.__doc__,
    "exec":exec.__doc__,
    "filter":filter.__doc__,
    "float":float.__doc__,
    "format":format.__doc__,
    "frozenset":frozenset.__doc__,
    "getattr":getattr.__doc__,
    "globals":globals.__doc__,
    "hasattr":hasattr.__doc__,
    "hash":hash.__doc__,
    "help":help.__doc__,
    "hex":hex.__doc__,
    "id":id.__doc__,
    "input":input.__doc__,
    "int":int.__doc__,
    "isinstance":isinstance.__doc__,
    "issubclass":issubclass.__doc__,
    "iter":iter.__doc__,
    "len":len.__doc__,
    "list":list.__doc__,
    "locals":locals.__doc__,
    "map":map.__doc__,
    "max":max.__doc__,
    "memoryview":memoryview.__doc__,
    "min":min.__doc__,
    "next":next.__doc__,
    "object":object.__doc__,
    "oct":oct.__doc__,
    "open":open.__doc__,
    "ord":ord.__doc__,
    "pow":pow.__doc__,
    "print":print.__doc__,
    "property":property.__doc__,
    "range":range.__doc__,
    "repr":repr.__doc__,
    "reversed":reversed.__doc__,
    "round":round.__doc__,
    "set":set.__doc__,
    "setattr":setattr.__doc__,
    "slice":slice.__doc__,
    "sorted":sorted.__doc__,
    "staticmethod":staticmethod.__doc__,
    "str":str.__doc__,
    "sum":sum.__doc__,
    "super":super.__doc__,
    "tuple":tuple.__doc__,
    "type":type.__doc__,
    "vars":vars.__doc__,
    "zip":zip.__doc__,
    "import":__import__.__doc__,
}

print(f'''Function documents''')
for i in pyf:
    print(f'''{i}()  \t {pyf[i]}\n''')






