hrs = raw_input("Enter Hours:")
h = float(hrs)
rph = raw_input("Enter rate:")
rph = float(rph)
pay = 0
if(h>40):
    pay = 40*rph + (h-40)*1.5*rph
else:
	pay = h*rph
print pay
