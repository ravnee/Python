inp = None
total =0;
count = 0;
avg = 0;
min = -1;
max = 0;
while True:
  try:
    inp = raw_input('> ');
    if inp=='done':
      break;
    inp = float(inp);
    total = total+inp;
    count=count+1;
    if(min > inp):
      min = inp;
    if(max<inp):
      max = inp;
  except Exception as e:
    print "Bad data"
if count>0:
  print str(total)+ " "+ str(count) +" "+ str(total/count);
  print "min "+str(min)+" max "+str(max);

