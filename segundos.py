segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

a = segundos // 86400
d = segundos % 86400
b = d // 3600
d = d % 3600
c = d // 60
d = d % 60

print(a,"dias,",b,"horas,",c,"minutos e",d,"segundos.")





