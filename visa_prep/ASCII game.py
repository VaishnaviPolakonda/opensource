a=input()
ts=''.join([char.lower() if char.isupper() else char.upper() for char in a])
print(ts)
