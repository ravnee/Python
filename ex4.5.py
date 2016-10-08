def computegrade(score):
    if score>1 or score <0 :
        return "Enter value in range 0.0-1.0"
    else :
        if score>=0.9 :
            return "A"
        elif score >=0.8 :
            return "B"
        elif score >= 0.7 :
            return "C"
        elif score >=0.6 :
            return "D"
        elif score <0.6 :
            return "F"
        else :
            return "Bad Score"
grade = raw_input("Enter Score: ")
grade = float(grade)
retVal = computegrade(grade)
print retVal
