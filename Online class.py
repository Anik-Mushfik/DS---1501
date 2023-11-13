#We pass argument or parameter to a function
#Python functions - print(),input(),max(),min(),sum(),len(),int(),float(),type()


#Make your own function-

# First define your function
def function_name():
    # inside the function
    print("I am a function")

# Call the functiuon-
function_name() #signature of the function(functioner namer pashe parentheses)


# Parameter of a funcion-
def paraFunc(X): # x is a parameter
    print(X)

paraFunc("Bangladesh will win World Cup") # this string is called argument


#** Returning value-
def multFunc(x):
    return x*2
val = multFunc(20)
print(val)


# Multiple parameter-
def multiFunc(x,y):
    if x>y:
        return x
    else:
        return y
print(multiFunc(14,5))

def powerof(num,pow):
    return num**pow
print(powerof(pow=2,num=5)) #Keyword argument

# Practice 1:
def word(x,y):
    if x>y:
        return y
    else:
        return x
print(word("apple","bat"))


# Default value-
def poerof(num,pow=1):
    return num**pow
print(poerof(10,2))
print(poerof(10))


# List as a parameter-


# Practice 2:
def lists(L1,L2):
    L1sum = sum(L1)
    L2sum = sum(L2)
    if L1sum > L2sum:
        return L1sum - L2sum
    else:
        return L2sum - L1sum
print(lists([12,12,13],[40,50,60]))
#Or,
def lists(L1,L2):
    L1sum = sum(L1)
    L2sum = sum(L2)
    x = L1sum - L2sum
    if x>0:
        return x
    else:
        return -x
print(lists([12,12,13],[40,50,60]))



# Local variables-

x = 20 # Global variable

def muFunc(s): # s is also a local variable
    n = 50 # n is a Local variable(Shudhu function er modhe chinbe)
# Local k shudhu functioner vitore chine but Global k vitore baire shobkhane chine.
print(x)


x = 20
def funcX():
    global x # Global variable k function er vitore chancge kora jaye
    x = 10

print(funcX())
print(x)


#BC section class- 
def vowel_count(x):
    count = 0
    for i in x:
        if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            count += 1
    return count

def mult_str_vow_count(*s):
    count2 = 0
    for j in s:
        count2 += vowel_count
    return count2
print(mult_str_vow_count("apple", "Banana"))




def is_prime(num):
    for i in range(2, num):
        if num%i == 0:
            return False
            return True

print(is_prime(2))