import math
list_of_degrees=[30.0,45.0,90.0,180.0,270.0,360.0]
for deg in list_of_degrees:
    rad=math.radians(deg)
    print ("This is a table of trig values")
    print (("sin of ") + str(deg) + (" is ") +  str(math.sin(rad))  )
    print (("cos of ") + str(deg) + (" is ") +  str(math.cos(rad))  )
    print (("tan of ") + str(deg) + (" is ") +  str(math.tan(rad))  )
