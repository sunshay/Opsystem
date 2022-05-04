#read input from the cmd or pass the argument to the python interpreter sysarg
#X = input('please enter hit ')
import sys
#print(sys.argv) #returns a list of command line arguments passed to a Python script
#rint(type(sys.argv))
print("You entered: ",sys.argv[1], sys.argv[2], sys.argv[3])
#print("Number of elements excluding the name of the program:",sys.argv[0])
#print("Number of elements excluding the name of the program:",len(sys.argv)-1)
#print("Argument List:",str(sys.argv))