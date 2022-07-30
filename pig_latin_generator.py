text = input("Type what you want to translate into pig latin: ")

vowels = "aeiou"
text_split = text.split()
translated_text = ""
includes_period = False

for word in text_split:
    lower_word = word.lower()
    
    if lower_word[0] in vowels:
        new_word = word + "yay "
    else:
        for idx, char in enumerate(word):
            if char not in vowels:
                word_constant = lower_word[0:idx+1]
            else:
                rest_of_word = lower_word[idx:None]
                break
            
        if "." in word_constant or "." in rest_of_word:
            includes_period = True
    
        word_constant = word_constant.replace(".", "")
        rest_of_word = rest_of_word.replace(".", "")
        
        new_word = rest_of_word + word_constant + "ay "
        
        if includes_period is True:
            new_word += ". "
            
    translated_text += new_word
    includes_period = False
    
print(translated_text)