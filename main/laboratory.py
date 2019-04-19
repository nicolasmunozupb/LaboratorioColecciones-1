"""
Solución del laboratorio
"""

from custom_functions import temperature_methods




#departamento de santander

santander_temperature_list=[]
print("please enter the temperature of santander")
for month in range(0,12):

    temperature=int(input("enter enter the temperature of the month {}".format(month+1)))

    santander_temperature.append(temperature)

santander_prom=temperature_methods.prom_temperature(santander_temperature_list)
santander_high_temperature=temperature_methods.high_temperature(santander_temperature_list)
print("the prom temperature of the depártment of santander is:{} ".format(santander_prom))
print("the hot temperature was".format(santander_high_temperature))

temp_mayor_santander=temperature_methods.mayor(santander_temperature_list)
sum_temp_santander=temperature_methods.sum_lista(santander_temperature_list)
standard_deviation_santander=temperature_methods.standard_deviation(santander_temperature_list)




#departamento de guajira

guajira_temperature_list=[]
print("please enter the temperature of guajira")
for month in range(0,12):

    temperature=int(input("enter enter the temperature of the month {}".format(month+1)))

    guajira_temperature.append(temperature)

guajira_prom=temperature_methods.prom_temperature(guajira_temperature_list)
guajira_high_temperature=temperature_methods.high_temperature(guajira_temperature_list)
print("the prom temperature of the depártment of guajira is:{} ".format(guajira_prom))
print("the hot temperature was".format(guajira_high_temperature))

temp_mayor_guajira=temperature_methods.mayor(guajira_temperature_list)
sum_temp_guajira=temperature_methods.sum_lista(guajira_temperature_list)
standard_deviation_guajira=temperature_methods.standard_deviation(guajira_temperature_list)





#departamento de nariño

nariño_temperature_list=[]
print("please enter the temperature of nariño")
for month in range(0,12):

    temperature=int(input("enter enter the temperature of the month {}".format(month+1)))

    nariño_temperature.append(temperature)

nariño_prom=temperature_methods.prom_temperature(nariño_temperature_list)
nariño_high_temperature=temperature_methods.high_temperature(nariño_temperature_list)
print("the prom temperature of the depártment of nariño is:{} ".format(nariño_prom))
print("the hot temperature was".format(nariño_high_temperature))

temp_mayor_nariño=temperature_methods.mayor(nariño_temperature_list)
sum_temp_nariño=temperature_methods.sum_lista(nariño_temperature_list)
standard_deviation_nariño=temperature_methods.standard_deviation(nariño_temperature_list)




#Promedio de la temperatura a nivel nacional

prom_nacional=int((sum_temp_santander+sum_temp_guajira+sum_temp_nariño)/36)
print("The average of the temperatures at the national level is {}°C".format(prom_nacional))

#Promedio de las temperaturas de los meses mas calientes de los tres departamentos

prom_temp_three_depart=int((temp_mayor_santander+temp_mayor_guajira+temp_mayor_nariño)/3)
print("The average of the temperatures of the hottest months of the three departments is {}°C".format(prom_temp_three_depart))



#cual promedio de los tres departamentos fue mayor

if santander_prom>guajira_prom and santander_prom>nariño_prom:
	print("The largest of the three departments was the department of Santander with {}°C".format(santander_prom))
else:
	if guajira_prom>santander_prom and guajira_prom>nariño_prom:
		print("The largest of the three departments was the department of guajira with {}°C".format(guajira_prom))
	else:
		if nariño_prom>santander_prom and nariño_prom>guajira_prom:
			print("The largest of the three departments was the department of nariño with {}°C".format(nariño_prom))

#cual fue la temperatura mas caliente en todo el año, en que mes se prensento y en que departamento

if temp_mayor_santander>temp_mayor_guajira and temp_mayor_santander>temp_mayor_nariño:
	print("The warmest temperature that occurred throughout the year was {} ° C, was presented in the month of {} in the department of Santander".format(temp_mayor_santander,santander_high_temperature))
else:
	if temp_mayor_guajira>temp_mayor_santander and temp_mayor_guajira>temp_mayor_nariño:
		print("The warmest temperature that occurred throughout the year was {} ° C, was presented in the month of {} in the department of guajira".format(temp_mayor_narinno,guajira_high_temperature))
	else:
		if temp_mayor_nariño>temp_mayor_santander and temp_mayor_nariño>temp_mayor_guajira:
			print("The warmest temperature that occurred throughout the year was {} ° C, was presented in the month of {} in the department of nariño".format(temp_mayor_guajira,nariño_high_temperature))



#Desviacion estandar de los tres departamentos

print("The standard deviation of the department of Santander is:", standard_deviation_santander)

print("The standard deviation of the department of guajira is:", standard_deviation_guajira)

print("The standard deviation of the department of nariño is:", standard_deviation_nariño)

