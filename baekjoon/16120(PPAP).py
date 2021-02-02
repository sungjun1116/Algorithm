string = input()

stack = []

for s in string:
    stack.append(s)
    if len(stack) >= 4:
        if "".join(stack[-4:]) == "PPAP":
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append("P")

if ''.join(stack) == "P":
    print("PPAP")
else:
    print("NP")
