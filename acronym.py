user_input=str(input("Enter a word:"))
text=user_input.split()
a=""
print(text)
for i in text:
    a = a+str(i[0]).upper()
print(a)
