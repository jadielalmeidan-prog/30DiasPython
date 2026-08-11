import re
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

print(re.findall("teaching",paragraph))
clean_paragraph = paragraph.replace('.', '').lower()
words = clean_paragraph.split()

frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
frequency_dict = {}        
for word in words:
    frequency_dict[word] = frequency_dict.get(word, 0) + 1
formatted_list = [(count, word) for word, count in frequency_dict.items()]
formatted_list.sort(reverse=True)
most_frequent = max(frequency, key=frequency.get)
print(f'A palavra mais frequente é: "{most_frequent}" com {frequency[most_frequent]} ocorrências.')
print(formatted_list)

def is_valid_variable(nome):
    caracteres_invalidos = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '!', '@', '#', '$', '%', '&', '*')
    if nome.startswith(caracteres_invalidos):
        return False
    else:
        return True

print(is_valid_variable('first_name'))
print(is_valid_variable('first-name'))
print(is_valid_variable('1first_name')) 
print(is_valid_variable('firstname'))

def clean_text(sentence):
    caracteres = ('-', '!', '@', '#', '$', '%', '&', '*', ";")
    for caractere in caracteres:
        sentence = sentence.replace(caractere, '')
    return sentence
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
print(clean_text(sentence))

def most_frequent_words(sentence):
    clean_sentence =sentence.replace('.', '').lower()
    words = clean_sentence.split()

    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    frequency_dict2 = {}        
    for word in words:
        frequency_dict2[word] = frequency_dict2.get(word, 0) + 1
    formatted_list2 = [(count, word) for word, count in frequency_dict2.items()]
    formatted_list2.sort(reverse=True)
    return formatted_list2[:3]
clean_sentence = clean_text(sentence)
print(most_frequent_words(clean_sentence))