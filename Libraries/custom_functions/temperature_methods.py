def average_temperature(temperature_list):
    temperature_sum = 0
    temperature_count = len(temperature_list)


    for average in temperature_list:
        temperature_sum += average

    final_average = temperature_sum / temperature_count

    return final_average


def higher_temperature(temperatuere_list):
    higher_temperature=temperatuere_list[0]

    for temperature in temperatuere_list:
        if temperature > higher_temperature:
            higher_temperature=temperature
    return higher_temperature

def hottest_average (hottest_list):
    hottest_average=hottest_list[0]
    for hottest in hottest_list:
        if hottest > hottest_average:
            hottest_average=hottest

    return hottest_average
