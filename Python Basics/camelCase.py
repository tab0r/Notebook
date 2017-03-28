from sys import argv
script, text = argv

def to_camel_case(text):
    #your code here
    camel_list = text.split("-")
    camelList = []
    for word in camel_list:
        print(word)
        word = word.split("_")
        print(word)
        camelList = camelList + word
    k = len(camelList)
    outputString = camelList[0]
    for i in range(1,k):
        outputString = outputString + camelList[i].capitalize()
    return outputString

print(to_camel_case(text))
