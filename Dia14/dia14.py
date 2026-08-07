#The map() function is a built-in function that takes a function and iterable as parameters.
#The reduce() function is defined in the functools module and we should import it from this module. Like map and filter it takes two parameters, a function and an iterable
#The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). It filters the items that satisfy the filtering criteria.

#Some of the built-in higher order functions that we cover in this part are map(), filter, and reduce. Lambda function can be passed as a parameter and the best use case of lambda functions is in functions like map, filter and reduce.
#A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.
#Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure.

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in countries:
    print(i)

print("\n")

for i in names:
    print(i)

print("\n")

for i in numbers:
    print(i)

def uppercase(name):
    return name.upper()
names_uppercase = map(uppercase,names)
print(list(names_uppercase))

def square(num):
    return num ** 2
squared_numbers = map(square,numbers)
print(list(squared_numbers))

def uppercase2(name):
    return name.upper()
pais_uppercase = map(uppercase2,countries)
print(list(pais_uppercase))

def land(name):
    if "land" in name:
        return name
    else:
        return False
land_pais = filter(land,countries)
print(list(land_pais))

def seis(nome):
    if len(nome) == 6:
        return nome
    else:
        return False
seis_caracteres = filter(seis,countries)
print(list(seis_caracteres))

def seis_ou_mais(nome):    
    if len(nome) >= 6:
        return nome
    else:
        return False
seis_caracteres2 = filter(seis_ou_mais,countries)
print(list(seis_caracteres2))

def comeco_e(nome):
    if "E" in nome:
        return nome
    else:
        return False
e_caractere = filter(comeco_e,countries)
print(list(e_caractere))

def get_string_lists(lista):
    lista_de_strings = []
    for item in lista:
        if type(item) == str:
            lista_de_strings.append(item)
    return lista_de_strings
print(get_string_lists(["Jadiel",True,1.4,3]))

from functools import reduce
def soma(x,y):
    return int(x)+ int(y)
total = reduce(soma,numbers)
print(total)

sentence = reduce(lambda x, y: x + ', ' + y if y != countries[-1] else x + ', and ' + y, countries)
final_sentence = f"{sentence} are north European countries"
print(final_sentence)

countries_2 = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

def categorize_countries_land(countries_list,pattern):
    return [country for country in countries_list if pattern in country]
print(categorize_countries_land(countries_2,"land"))
print(categorize_countries_land(countries_2,"ia"))
print(categorize_countries_land(countries_2,"island"))
print(categorize_countries_land(countries_2,"stan"))

def dict_starting(countries_list):
    letter_counts = {}
    for country in countries_list:
        first_letter = country[0].upper() 
        if first_letter in letter_counts:
            letter_counts[first_letter] += 1
        else:
            letter_counts[first_letter] = 1
    return letter_counts
result = dict_starting(countries_2)
print(result)

def get_first_ten_countries(countries_list):
    return countries_list[:10]
print(get_first_ten_countries(countries_2))

def get_last_ten_countries(countries_list):
    return countries_list[184:]
print(get_last_ten_countries(countries_2))

