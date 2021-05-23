import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def trans(w):
    w = w.lower()
    if w in data:

       return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]       
    elif len(get_close_matches(w, data.keys()))>0 :
        letter= input("Did you mean %s instead ? Enter Y if YES,or N for NO? " %get_close_matches(w,data.keys(), n=3))
        if letter == "Y":
              letter2=input ("Enter the index of the Word ")
              letter2=int(letter2)
              if letter2 <= 5:
                 return data[get_close_matches(w, data.keys())[(letter2-1)]]
              else :
                     return "Out of Range,Please Check. "
        elif letter == "N":
            return " The word does not exist."
        else :
            return "Did not understand your entry."   

    else:
        return "Check your word."


word = input("Enter the Word: ") 

output = trans(word)

if type(output) == list:

    for item in output:
     print(item)
else:
    print(output) 
