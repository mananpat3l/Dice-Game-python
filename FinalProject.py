
import random
#I,Manan Patel, 000826892, certify that this material is my original work. No other person's work has been used without due acknowledgment and I have not made my work available to anyone else.
def rollDie( faces,dices ):
    # module to roll a single die with a variable number of faces
    # ASSUME faces is a valid positive integer, greater than 1
    percentage=0
    studentpoints=0
    fact=0
    import random

    myList = []

    loop = 0
    while loop < dices:
          myList.append( random.randint( 0, faces ) )
          loop += 1

    print( myList )
    avg= average(myList)
    finaltotal=total(myList)
    fact=pattern1(myList)
    fact=pattern2(finaltotal)
    fact=pattern3(myList,avg)
    fact=pattern4(myList)
    
    
    maxtotal=faces*dices
    precentage=finaltotal/maxtotal
    studentnumber=int(input("enter your student number:"))
    studentpoints=studentnumber%2020
    points=maxtotal+percentage+studentpoints+fact
    print("your total points is ",points)

    return myList

def validateInt( min, max, prompt ):
    # ASSUME min and max are valid positive integers, and that min < max
    return 0

def validateStr( prompt, listOfChoices ):
    # assume prompt is a String and listOfChoices is a list of Strings.
    return ""

def average( myList ):
     total = 0
     for i in myList:
                total += i

     
     avg=total/dices
     print( "The average of the list is",avg )
     return avg
    
def total( myList ):
     sum = 0
     for i in myList:
                sum += i

     print( "The sum of this list is",sum )
     
     return sum  
    
    
    
          
    # ASSUME inList is a list of numbers and the length of inList is > 0
    

def calculatePercentage( sides, dice, diceRolls ):
    # ASSUME sides*dice != 0, sides, dice are numbers
    # ASSUME diceRolls is a list of numbers
    return 0

def isPrime( number ):
    # ASSUME number is an integer
    return False

def pattern1(myList ):
    # ASSUME sides > 0 and dice is a list of integers
    fact=0
    n=len(myList)
    for n in myList:
       if myList[n-1]==myList[n]:
           print("pattern matches")
           n=n-1
           fact=bonusFactor(10)
           break
       else:
           print("pattern does not match")
           break
       
    return fact

def pattern2(finaltotal):
    # ASSUME sides, count are integers
    # ASSUME dice is a list of integers
    fact=0
    for i in range(2,finaltotal):
           if(finaltotal%i)==0:
               print("sum is not a prime number")
               break
               
           else:
               print("sum is an prime number pattern matches 2")
               fact=bonusFactor(15)
               break
    return fact

def pattern3( myList,avg):
    # ASSUME dice is a list of integers
    fact=0
    lo = 0
    hi = len( myList ) - 1
    mid = (lo + hi) // 2
    for mid in myList:
        
          if myList[1]>avg:
              print("pattern matchs 3")
              fact=bonusFactor(5)
              lo=lo+1
              break
    return fact

def pattern4(myList):
    # ASSUME dice is a list of integers
    fact=0
    n=len(myList)
    for n in myList:
       if myList[n]!=myList[n-1]and myList[0]!=myList[1] :
           n=n-1
           print("pattern 4 mathes as all the index have the same value " )
           fact=bonusFactor(8)
           break
           
       else:
           print("pattern 4 does not matched! some of the values are matched not all")
           break
       
       
       
    
    return fact
    
    
    
def bonusFactor( factor ):
    # ASSUME dice is a list of numbers
    # ASSUME sides, count are integers
    print("your bonus factor is",factor)
    
    return factor

def score( maxSides, totalDice, diceRolled ):
    # ASSUME maxSides and totalDice are integers > 0
    # ASSUME diceRolled is a list of integers
    return 0
    

    


# main
faces=int(input("enter the number of faces:"))
dices=int(input("enter the number of dices:"))
rollDie(faces,dices)







# Don't forget a statement of authorship at the top of the file!
