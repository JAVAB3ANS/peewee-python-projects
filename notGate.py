code = """0001101011101011101"""

code_useable = [int(i) for i in str(code)]

print(code_useable)

for x in range(0, len(code_useable)):
    if code_useable[x] == 0:
        code_useable[x] == 1
    else:
        code_useable[x] == 0

code = "".join(str(a) for a in code_useable)
print(code)