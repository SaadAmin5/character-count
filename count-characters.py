string=input('enter word: ').lower()
character=input('enter character to be counted: ').lower()
count=0

for i in string:
    if i==character:
        count=count+1
        
print(character, 'appears', count, 'times')