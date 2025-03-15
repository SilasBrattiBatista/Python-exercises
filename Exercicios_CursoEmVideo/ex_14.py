#Escreva um programa que converta uma temperatura digitada em °C e converta para °F

celcius = float(input('Digite a temperatura em °C: '))
fahrenheit =  ((9 * celcius) / 5) + 32 
print(f'A temperatura de {celcius}°C corresponde a {fahrenheit}°F')