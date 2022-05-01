import sys
#print(sys.argv[0])
#print(len(sys.argv))
def convert_distance(miles):
    	return miles * 0.62137119  #conversion_factor = 0.6213...
kilometers = convert_distance(int(sys.argv[1]))

#y = int(sys.argv[2])
 #miles = x + y
print('the distance in miles is ', kilometers)