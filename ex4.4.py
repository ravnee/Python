def computepay(hrs,rph):
    try:
        h = float(hrs)
        rph = float(rph)
        pay = 0
        if(h>40):
            pay = 40*rph + (h-40)*1.5*rph
        else:
        	pay = h*rph
        return pay
    except Exception as e:
        print "Error, Please enter numeric value"

hours = raw_input("Enter Hours:")
rph = raw_input("Enter rate:")
retVal = computepay(hours,rph)
if type(retVal) != type(None):
    print retVal
