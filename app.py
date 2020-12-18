import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data: 
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys()))>0:
        li = get_close_matches(w,data.keys(), n = 4, cutoff=0.6)
        print("Suggestions ")
        for i in range(len(li)):
            print("Press " ,i, "For this Keyword " , li[i] )
      
        take_in = int(input("Press Keyword please...: "))
        if take_in == 0:
            return(data[li[0]])
        elif take_in == 1:
            return(data[li[1]])
        elif take_in == 2:
            return(data[li[2]])
        elif take_in == 3:
            return(data[li[3]])
        else:
            return("Invalid Input . Please Check Again")
   

    else:
        return"The word does'nt exist. Please Double check it."

word = input("Enter word for finding its meaning....: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)


print("Stay Connected for more Information")