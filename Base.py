#!/home/mattias/anaconda3/envs/tutorial/bin/python
# Shebang for conda envirionment

######
### Variable
x = 1
x, y = 1, 2
x, *y = 1, 2, 3, 4 # Packs rest into a list y

######
# Flow and logic
A, B, C, D = 0, 1, 2, 0
A or B 
C or B 
E = A or D or 4 # E becomes 4

data = 1
#True and data = data + 2 # Does not work
True and not exec("data = data + 2") or exec("data = data + 3") #Executes first if True else if False second
False and not exec("data = data + 2") or exec("data = data + 3")

## if
if (A == 1 or B == 1):
    print("Yes")
    
if not(A != 4 and B <= 10):
    print("This")
elif not(A != 4 and C <= 10):
    print("That")
else:
    print("Those")
    
### match
match A:
    case 1:
        print("A is 1")
    case 2:
        print("A is 2")
    case _:
        print("A is Something else")

"Yes" if True else "No"
"Yes" if False else "No"
False and "Yes" or "No"
True and "Yes" or "No"

### while
A = 1
while(A < 100):
    A = A + 1
    if (A == 10):
        continue #Skips back to while
    if (A == 20):
        break # Breaks out of while
    print(A)
else:
    print("Loop complete") # Does not get printed since the loop break before completion

### for
aList = ["a","b","c"]
bList = ["d","e","f"]
for A in aList:
    if A == "b":
        continue # Skips back to for
    print(A)
else:
    print("Done")

for A in aList:
    if A == "b":
        continue # Skips back to for
    print(A)
else:
    print("Done")

### List comprehension
[A+B for A in aList for B in bList if not "bd" in A+B]
[A+B if A+B != "ae" else "change" for A in aList for B in bList]

###### Functions
### Normal function
def diff_numbers(numberone, numbertwo):
    return(numberone - numbertwo)

Differance = diff_numbers(10, 2)
print("Differance is ", Differance)

Newdiff = diff_numbers # Copy offunction
Newdiff(8,3)

### Use global variable in new function
def add():
    def inner(b):
        return(In+b)
    return(inner)
In = 5
addIn = add()
addIn(5)
# Equals 10
In = 10
addIn(5)
# Equals 15

### Bind/lock global varible value in new function called "closure"
def add(In):
    def inner(b):
        return(In+b)
    return(inner)

In = 5
addIn = add(In)
addIn(5)
# Equals 10
In = 10
addIn(5)
# Still equals 10, not 15 15

### Anonymous lambda function. Use "or" to chain multiple expressions that return none. exec() returns none
newfunc = lambda x,y: x+y
newfunc(2,3)
(lambda x,y: x*y)(2,3)

# Multiline multicommand lambda
(lambda x,y:\
exec("\
x+y\n\
x*y\
"))(2,3)

### Decoration
def printKing():
    print("King is here")

def addGreeting(func):
    def wrapp():
        print("Be greeted eveyone!")
        func()
    return(wrapp)

printKing()
printKing = addGreeting(printKing) # Transforms/decorates the function

@addGreeting # Shorthand for decoration of function
def printQueen():
    print("Queen is here")

printQueen()

###### Class, object/instance 

data1 = 2 # global
class calcdata():
    data1 = 5
    data2 = 7
    
    def __init__(self, data1=10): # 10 is default value
        self.data1 = data1
    
    def add_numSelf(self):
        return(data1 + self.data1)
    
    @classmethod # Can only access class data and global
    def add_numClass(cls):
        return(data1 + cls.data1)
    
    def add_numSelfClass(self):
        return(self.__class__.data1 + self.data1)
    def add_numTwoSelfClass(self):
        return(self.__class__.data2 + self.data2)


mycalcdata = calcdata() # Creates an instance of the class with default parameter 10
mycalcdata = calcdata(13) # Creates an instance of the class
mycalcdata.add_numSelf() # 15 = 2 + 13
mycalcdata.add_numClass() # 7 = 2 + 5
mycalcdata.add_numSelfClass() # 18 = 5 + 13
calcdata.data1 = 3 # Change class data1 
mycalcdata.add_numSelf() # Same 15 does not use class data1
mycalcdata.add_numClass() # 5 = 2 + 3
mycalcdata.add_numSelfClass() # 16 = 3 + 13
mycalcdata.add_numTwoSelfClass() # 14 = 7 + 7
calcdata.data2 = 8 # Seems to change both class and instance data2 from 7 to 8. self.data2
mycalcdata.add_numTwoSelfClass() # 16 = 8 + 8. self.data2 is the same as calcdata.data2 until it has been set in method e.g. __init__

### Inheritance. Make an new derived/child class using another base/parent class

class calcmoredata(calcdata):
    def diff_num(self):
        return(self.data1 - self.data2)
    def add_numSelf(self): # Overwrites since same name
        return(data1 + self.data2)
    def base_add_numSelf(self):
        return(super().add_numSelf())

mycalcmoredata = calcmoredata(12)
mycalcmoredata.diff_num() # 4 = 12 - 8 class data2 was changed to 8
mycalcmoredata.add_numSelf() # 10 = 2 + 8
mycalcmoredata.base_add_numSelf() # 14 = 2 +12


###### Iterables 
### String
In = 5
Text = "Jag är {} år {}". format(In,2023)
# f-string
Insert = 5
Text = f"All {Insert} people ran {round(4.5)} km."

#Substring index
Text[0:3]
Text[slice(0,3)]
Text[range(0,3)] #Range works with unpacking and inner list creation
r = [*range(0,3)] #Does not even converting range to list
Text[r] #Does not work
[Text[i] for i in r] # List comprehension is not practic

#Test if "är is in Text, True
"är" in Text
#Find text optional substring
Text.find("är",0,3) # -1 no find
Text.find("är") # 4
Text.find("är",2,6) # 4
#Remove
Text="ababbababa"
Text.replace("b","",2) # Rplace first two "b"s with nothing
Text[slice(2,4)]
#Insert
Text = "Alla kan vara med."
Text.replace("an va","an inte va") 
#Join
Text + Text
#Join list of strings
" ".join(["Text1", "Text2"]) #Space string between words of list
#Split
Text = "Alla kan vara med."
Text.split(" ")
#length of string
len(Text)


### List, tupple and set
aList = ["a","b","c"]
bList = ["d","e","f"]
aList + bList


MyList = ["Jag", "Kan", "Skriva"]
#Add to end
MyList.append("Text")
# Substring
MyList[slice(0,2)]
MyList[0:2]
# Make a list to index a list
index = [0,1,2]
MyList[index] #Does not work
SubList = [MyList[ind] for ind in index] #Works

Mytupple = ("Jag","Kan","skriva") #Cannot be changed
Mytupple[1]

MySet = {"Jag","kan","skriva", "A"} #Elements do not have an order or duplication
MySet[1] # Does not work since no order/index
sorted(MySet) #Outputs a sorted list

MyNewSet = {"Jag","kan","Läsa", "B"}
MySet | MyNewSet #Union
MySet & MyNewSet #Intersetion
MySet - MyNewSet #Differance
MySet ^ MyNewSet #Not in both

# Multidimensional list
multilist = [[1,5,9], [2, 4, 9], [1,1, 2]]
#[1,5,9]
#[2,4,9]
#[1,1,2]
#Whole rows can be accessed
multilist[1]
# But column access does not work
multilist[0:2][1]
# Only single values can be accessed e.g. row 1 column 2
multilist[1][2] # 9
# List comprehension can be used to pick out a column
Column = 1
[multilist[i][Column] for i in range(0,3)]

# Dictionary like a named set/list
Dict = {"Name":"Mattias","Age":"43","Home":"Skyttorp"}
Dict["Name"] # Mattias
