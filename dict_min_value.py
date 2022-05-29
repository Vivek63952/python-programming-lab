#PROGRAM TO GET THE MINIMUM KEY FROM A DICTIONARY

dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
print(min(dict, key=dict.get))
