
code = """0001101011101011101"""
key = """0100111010101010010"""

code_useable = [int(i) for i in str(code)]
key_useable = [int(j) for j in str(key)]

print(code_useable)
print(key_useable)

for x in range(0, len(code_useable)):
    #if not a, and b
    if code_useable[x] == 0:
        code_useable[x] == 1
    #if a, and not b
    elif code_useable[x] == 1 and key_useable[x] == 0:
        code_useable[x] = 1
    #Otherwise: not a, and not b; a, and b
    else:
        code_useable[x] = 0

code = "".join(str(a) for a in code_useable)
print(code)