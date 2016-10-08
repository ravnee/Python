'''
Write a program which prompts the user for a Celsius temperature,
convert the temperature to Fahrenheit
and print out the converted temperature.
'''
inp = raw_input("Enter temperature in Celsius: ")
cTemp = float(inp)
fTemp = (cTemp*9/5)+32
print "Temp in Fahrenheit: "+str(fTemp)
