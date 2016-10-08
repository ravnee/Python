def computepay(h,r):
    if(h>40):
        return h*r
    else:
        t = h*(3*r)/2
        return t


hrs = raw_input("Enter Hours:")
hrs = float(hrs)
rph = raw_input("Enter rate per hour:")
rph = float(rph)
p = computepay(hrs,rph)
print "Pay",p
