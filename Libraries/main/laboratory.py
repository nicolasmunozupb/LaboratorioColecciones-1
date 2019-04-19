"""
Solución del laboratorio
"""

from custom_functions import temperature_methods

import statistics as stats

santanderstemperature_list=[]
print("please enter the temperatures of the department of santander")
for i in range(0, 12):

    temperature = int(input("give me the temperature of month  {}  ".format(i+1)))


    santanderstemperature.append(temperature)

santanders_average=temperature_methods.average_temperature(santanderstemperature_list)
santander_higher_temperature=temperature_methods.higher_temperature(santanderstemperature_list)
print("the average temperature of the depártment of santander is: ", santanders_average "\n and its client temperature was: "guajira_higher_temperature))

#departamento de la guajira



guajirasstemperature_list=[]
print("please enter the temperatures of the department of guajira")
for i in range(0, 12):

    temperature = int(input("give me the temperature of month  {}  ".format(i+1)))


    guajirastemperature.append(temperature)

guajiras_average=temperature_methods.average_temperature(guajirasstemperature_list)
guajira_higher_temperature=temperature_methods.higher_temperature(guajirasstemperature_list)
print("the average temperature of the depártment of guajira is: ", guajiras_average "\n and its client temperature was: "guajira_higher_temperature)

#departamento de nariño



nariñosstemperature_list=[]
print("please enter the temperatures of the department of nariño")
for i in range(0, 12):

    temperature = int(input("give me the temperature of month  {}  ".format(i+1)))


    nariñosstemperature.append(temperature)

nariño_average=temperature_methods.average_temperature(nariñostemperature_list)

nariño_higher_temperature=temperature_methods.higher_temperature(nariñosstemperature_list)
print("the average temperature of the depártment of nariño is: ", nariño_average "\n and its client temperature was: ", nariño_higher_temperature)

national_average=(santanders_average+nariño_average+guajiras_average)/3
national_higher_temperature=(santander_higher_temperature+guajira_higher_temperature+nariño_higher_temperature)/3

print("The average of the highest temperatures is: ",national_higher_temperature)
print("the average national temperature is: ",national_average)

highertemperature_list=[santanders_average,guajiras_average,nariño_average]

hottest=temperature_methods.hottest_average(highertemperature_list)

print("the hottest average is: ",hottest)




