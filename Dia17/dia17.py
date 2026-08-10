try:
    countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland',"Estonia","Russia"]
    fin,sw,nor,den,ice,e,rus,*res = countries
    nordic_countries = fin + " " + sw + " " + nor + " " + " " + den + " " + ice
    print(nordic_countries)
    print(e)
    print(rus)
    print(res)
except Exception as e:
    print(e)
## Extra
#1.Tratamento de Divisão por Zero

try:
    num1 = int(input("Digite o 1° número inteiro: "))
    num2 = int(input("Digite o 2° número inteiro: "))
    operação = input("Diga a operação(+,-,/,*): ")
    match operação: 
        case "+":
            print(f"Resultado: {num1+num2}")
        case "-":
            print(f"Resultado: {num1-num2}")        
        case "/":
            print(f"Resultado: {num1/num2}")
        case "*":
            print(f"Resultado: {num1*num2}")
except ZeroDivisionError as erro:
    print(erro) 