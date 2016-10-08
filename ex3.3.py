score = raw_input("Enter Score: ")
score = float(score)
if score>1 or score <0 :
    print "Enter value in range 0.0-1.0"
else :
    if score>=0.9 :
        print "A"
    elif score >=0.8 :
        print "B"
    elif score >= 0.7 :
        print "C"
    elif score >=0.6 :
        print "D"
    else :
        print "F"
