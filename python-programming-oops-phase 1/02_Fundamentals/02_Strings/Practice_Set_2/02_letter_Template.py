letter = '''Dear <|NAME|>,\nYou are selected!\n<|DATE|>'''

print(letter)


l2 ='''Dear <|NAME|>,\nYou are selected!\n<|DATE|>'''

print(l2.replace("<|NAME|>","Alexa").replace("<|DATE|>","1st Jan 2024"))
