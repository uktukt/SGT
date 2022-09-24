# text = input("enter sentence ")
text = "abba"
text_ed = text.lower()

i=1
for i in range(1, len(text_ed)):
    if text_ed[::i]==text_ed[::-i]:
        print(text_ed[::-1])
        break
    else:
        print("")