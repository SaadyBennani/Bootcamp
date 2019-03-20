#unit_convert.py

#which operation will we be doing
distance = int(input('What is your initial distance?:'))
initial_unit= input('What is your starting unit?:')
final_unit = input('What unit would you like to convert to?:')

#conversion functions
def to_m(distance, unit):
    if unit == 'm':
        return distance *1
    if unit == 'ft':
        return distance*0.3048
    if unit == 'yd':
        return distance*0.9144
    if unit == 'mi':
        return distance*1609.34
    if unit == 'km':
        return (distance*1000)
    if unit == 'in':
        return (distance*0.0254)


def from_m(distance, unit):
    if unit == 'm':
        return str(distance*1)+ 'm'
    if unit == 'ft':
        return str(distance*3.28084)+'ft'
    if unit == 'km':
        return str(distance*0.001)+'km'
    if unit == 'mi':
        return str(distance*0.000621371)+'mi'
    if unit == 'in':
        return str(distance*39.3701)+'in'
    if unit == 'yd':
        return str(distance*1.09361)+'yd'

meters = to_m(distance, initial_unit)

print(from_m(meters, final_unit))
