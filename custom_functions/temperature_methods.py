#el promedio de la temperatura de cada departamento
def prom_temperature(temperature_departament_list):

    temperature_sum = 0
    temperature_quantity = len(temperature_departament_list)

    for prom in temperature_departament_list:
        temperature_sum += prom

    final_prom = temperature_sum / temperature_quantity

    return final_prom

#el mes mas caliente de cada departamento
def high_temperature(temperature_departament_list):
    high_temperature=temperature_departament_list[0]
    month=[]

    for temperature in temperature_departament_list:
        if temperature>high_temperature:
            high_temperature=temperature

    position=temperature_departament_list.index(high_temperature)

    if position==0:
        month.append("enero")
    else:
        if position==1:
            month.append("febrero")
        else:
            if position==2:
                month.append("marzo")
            else:
                if position==3:
                    month.append("abril")
                else:
                    if position ==4:
                        month.append("mayo")
                    else:
                        if position ==5:
                            month.append("junio")
                        else:
                            if position ==6:
                                month.append("julio")
                            else:
                                if position ==7:
                                    month.append("agosto")
                                else:
                                    if position ==8:
                                        month.append("septiembre")
                                    else:
                                        if position ==9:
                                            month.append("octubre")
                                        else:
                                            if position ==10:
                                                month.append("noviembre")
                                            else:
                                                if position ==11:
                                                    month.append("diciembre")
    return month


#meses mas calientes de los tres departamentos
def hot_prom(temperature_departament_list):
    hot_prom=temperature_departament_list[0]

    for temperature in temperature_departament_list:
        if temperature>hot_prom:
            hot_prom=temperature

    return hot_prom

#desviacion estandar de la temperatura en  cada departamento

def standard_deviation(temperature_departament_list):
    temperature_suma=0
    temperature_quantity=lem(temperature_departament_list)
    diferent_temperature=[]
    suma=0

    for temperature in temperature_departament_list
        temperature_suma+=temperature

    media=temperature_suma/temperature_quantity

    for i in temperature_departament_list:
        i=i-media
        diferent_temperature.append((i**2)/temperature_quantity)

    for x in diferent_temperature:
        suma+=x

    standard_deviation()=suma**(1/2)

    return standard_deviation























