import clipboard
stringToChange = clipboard.paste()
newString = ""
LowerOrUpper = 0
for letter in stringToChange:
    if(LowerOrUpper == 0):
        newString = newString + letter.lower()
        LowerOrUpper = 1
    elif(LowerOrUpper == 1):
        newString = newString + letter.upper()
        LowerOrUpper = 0
    else:
        newString = newString + letter

clipboard.copy(newString)
