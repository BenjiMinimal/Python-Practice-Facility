#Hello!Welcome to File 1

#Function Coding Facilities.

def mymin(anyarray):

    min = anyarray[0]

    for value in anyarray:
        if value < min:
            min = value
    return min

def mymax(anyarray):

    max = anyarray[0]

    for value in anyarray:
        if value > max:
            max = value
    return max

def mysum(anyarray):

    sum=0
    for x in range(0,len(anyarray)):

        sum += anyarray[x]
    return sum


def myaverage(anyarray):

    average=mysum(anyarray)/len(anyarray)

    return average




def mymed (anyarray):

    sorts = sorted(my_array)
    length = len(sorts)
    if not length % 2:
        return (sorts[length / 2] + sorts[length / 2 - 1]) / 2.0
    return sorts[length / 2]


def mymode (anyarray):
    mydict = {}
    for value in anyarray:
        if value in mydict:
            mydict[value]+=1
        else:
            mydict[value]=1
    return mydict



#Data Entry Area.Enter numbers here.
my_array=[2,2,6,8,10,1,60,90,90,11,10,2,11,1]






   #Data entry complete.Loading Info Results

 #Info Result Tab
print "Info Results"
print "\/\/\/\/\/\/\/\/\/"
print"------------------"
print"Mode\t\t  = " +str(mymode(my_array))
print"Sum\t\t\t  = "+str(mysum(my_array))
print'Average\t\t  = '+str(myaverage(my_array))
print'Maximum Value = '+str(mymin(my_array))
print'Minimum Value = '+str(mymax(my_array))
print 'Median\t\t  = '+str(mymed(my_array))
print "------------------"
print "/\/\/\/\/\/\/\/\/"

#Loading complete.



#Minimum and Maximum Example Code

#count = 24
#temperatures = [3 * x for x in range(count)]
#max = -9999
#min = 9999
#total = 0.0

#for value in temperatures:
    #total = total + value
    #if value > max:
        #max = value
    #if value < min:
        #min = value

#print("Minimum: ", min)
#print("Maximum: ", max)
#print("Average: ", total / count)











#Experiment Division closed due to lack of funding.














