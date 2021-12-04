#!/usr/bin/python3
specialchardict = {"!":"exc", "@": "ate", "#": "num", "$": "dol", "%": "prc", "^": "crt", "&": "and", "*": "str", "(": "opn", ")": "cpn", "[": "obr", "]": "cbr", "{": "ocl", "}": "ccl", "<": "lft", ">": "rgt", "?": "qst", ",": "com", "/": "slh", "'": "sqt", "\"": "dqt", ".": "prd", "\\": "bsl", "~": "tld", "`": "btk", "-": "min", "_": "und", "\n": "new", "+": "pls", "=": "eql", "|": "pip", ":": "cln", ";": "scn", " ": "spc", "	": "tab"}
newdict = {}
for key, value in specialchardict.items:
	newdict[value] = key
print(newdict)