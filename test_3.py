
text=input("First player, please enter a text ")
space = " "
asterisk="*"
new_text=""

for c in text: 
        new_text += asterisk 

print(new_text)

while asterisk in new_text:
    letter=input("Second player, please enter a letter ")
   # letter="a"
    for i, c in enumerate(text): # so enumarate returns index and value
        if c == letter:
           new_text=new_text[:i]+letter+new_text[i+1:]
    print(new_text)

#NOT WORKING
print("GAME OVER")
print(new_text)