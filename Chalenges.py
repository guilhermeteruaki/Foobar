from fractions import Fraction
def chalenge1( x, y):
    '''
    Prison Labor Dodgers
    ====================

    Commander Lambda is all about efficiency, including using her bunny prisoners for manual labor. But no one's been properly monitoring the labor shifts for a while, and they've gotten quite mixed up. You've been given the task of fixing them, but after you wrote up new shifts, you realized that some prisoners had been transferred to a different block and aren't available for their assigned shifts. And manually sorting through each shift list to compare against prisoner block lists will take forever - remember, Commander Lambda loves efficiency!

    Given two almost identical lists of prisoner IDs x and y where one of the lists contains an additional ID, write a function solution(x, y) that compares the lists and returns the additional ID.

    For example, given the lists x = [13, 5, 6, 2, 5] and y = [5, 2, 5, 13], the function solution(x, y) would return 6 because the list x contains the integer 6 and the list y doesn't. Given the lists x = [14, 27, 1, 4, 2, 50, 3, 1] and y = [2, 4, -4, 3, 1, 1, 14, 27, 50], the function solution(x, y) would return -4 because the list y contains the integer -4 and the list x doesn't.

    In each test case, the lists x and y will always contain nFibbo non-unique integers where nFibbo is at least 1 but never more than 99, and one of the lists will contain an additional unique integer which should be returned by the function.  The same nFibbo non-unique integers will be present on both lists, but they might appear in a different order, like in the examples above. Commander Lambda likes to keep her numbers short, so every prisoner ID will be between -1000 and 1000.

    Languages
    =========

    To provide a Python solution, edit solution.py
    To provide a Java solution, edit Solution.java

    Test cases
    ==========
    Your code should pass the following test cases.
    Note that it may also be run against hidden test cases not shown here.

    -- Python cases --
    Input:
    solution.solution([13, 5, 6, 2, 5], [5, 2, 5, 13])
    Output:
        6

    Input:
    solution.solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50])
    Output:
        -4

    -- Java cases --
    Input:
    Solution.solution({13, 5, 6, 2, 5}, {5, 2, 5, 13})
    Output:
        6

    Input:
    Solution.solution({14, 27, 1, 4, 2, 50, 3, 1}, {2, 4, -4, 3, 1, 1, 14, 27, 50})
    Output:
        -4

    '''

    
    set1 = set(x)
    set2 = set(y)
    if len(set1) > len(set2):
        
        dif = set1.difference(set2)
    
    else:
        
        dif = set2.difference(set1)
  
    for s in dif: 
        return s 

def chalenge2_1(pegs):
    '''Gearing Up for Destruction
    ==========================

    As Commander Lambda's personal assistant, you've been assigned the task of configuring the LAMBCHOP doomsday device's axial orientation gears. It should be pretty simple - just add gears to create the appropriate rotation ratio. But the problem is, due to the layout of the LAMBCHOP and the complicated system of beams and pipes supporting it, the pegs that will support the gears are fixed in place.

    The LAMBCHOP's engineers have given you lists identifying the placement of groups of pegs along various support beams. You need to place a gear on each peg (otherwise the gears will collide with unoccupied pegs). The engineers have plenty of gears in all different sizes stocked up, so you can choose gears of any size, from a radius of 1 on up. Your goal is to build a system where the last gear rotates at twice the rate (in revolutions per minute, or rpm) of the first gear, no matter the direction. Each gear (except the last) touches and turns the gear on the next peg to the right.

    Given a list of distinct positive integers named pegs representing the location of each peg along the support beam, write a function solution(pegs) which, if there is a solution, returns a list of two positive integers a and b representing the numerator and denominator of the first gear's radius in its simplest form in order to achieve the goal above, such that radius = a/b. The ratio a/b should be greater than or equal to 1. Not all support configurations will necessarily be capable of creating the proper rotation ratio, so if the task is impossible, the function solution(pegs) should return the list [-1, -1].

    For example, if the pegs are placed at [4, 30, 50], then the first gear could have a radius of 12, the second gear could have a radius of 14, and the last one a radius of 6. Thus, the last gear would rotate twice as fast as the first one. In this case, pegs would be [4, 30, 50] and solution(pegs) should return [12, 1].

    The list pegs will be given sorted in ascending order and will contain at least 2 and no more than 20 distinct positive integers, all between 1 and 10000 inclusive.

    Languages
    =========

    To provide a Java solution, edit Solution.java
    To provide a Python solution, edit solution.py

    Test cases
    ==========
    Your code should pass the following test cases.
    Note that it may also be run against hidden test cases not shown here.

    -- Java cases --
    Input:
    Solution.solution({4, 17, 50})
    Output:
        -1,-1

    Input:
    Solution.solution({4, 30, 50})
    Output:
        12,1

    -- Python cases --
    Input:
    solution.solution([4, 30, 50])
    Output:
        12,1

    Input:
    solution.solution([4, 17, 50])
    Output:
        -1,-1
    '''
    # used this solution to understand the chalenge, altough very similar, maybe even equals,  I tried to ajust the code to my liking
    # https://stackoverflow.com/questions/40465866/google-foobar-gearing-up-for-destruction
    pegsLength = len(pegs)
    if pegsLength % 2 == 0:
        pegsSum = -pegs[0] + pegs[pegsLength-1]
        isEven = True
    else:
        pegsSum = -pegs[0] - pegs[pegsLength-1]
        isEven = False

    if pegsLength>2:
        for i in range(1,pegsLength-1):
                pegsSum += 2*( pegs[i] * (-1)**(i+1) )
    

    if isEven == True:
        Answer  = Fraction(2*(float(pegsSum)/3)).limit_denominator()

    else:
        Answer  = Fraction(2*(float(pegsSum))).limit_denominator()

    if Answer < 2:
        return [-1,-1]

    R1 = Answer

    for i in range (0, pegsLength-2):
        R2 = (pegs[i+1] - pegs[i]) - R1
    
        if R1 < 1 or R2 < 1:
            return[-1,-1]
        else:
            R1 = R2

    return [Answer.numerator, Answer.denominator]
 
def Chalenge2_2(total_lambs):
    '''
    Lovely Lucky LAMBs
    ==================

    Being a henchman isn't all drudgery. Occasionally, when Commander Lambda is feeling generous, she'll hand out Lucky LAMBs (Lambda's All-purpose Money Bucks). Henchmen can use Lucky LAMBs to buy things like a second pair of socks, a pillow for their bunks, or even a third daily meal!

    However, actually passing out LAMBs isn't easy. Each henchman squad has a strict seniority ranking which must be respected - or else the henchmen will revolt and you'll all get demoted back to minions again! 

    There are 4 key rules which you must follow in order to avoid a revolt:
        1. The most junior henchman (with the least seniority) gets exactly 1 LAMB.  (There will always be at least 1 henchman on a team.)
        2. A henchman will revolt if the person who ranks immediately above them gets more than double the number of LAMBs they do.
        3. A henchman will revolt if the amount of LAMBs given to their next two subordinates combined is more than the number of LAMBs they get.  (Note that the two most junior henchmen won't have two subordinates, so this rule doesn't apply to them.  The 2nd most junior henchman would require at least as many LAMBs as the most junior henchman.)
        4. You can always find more henchmen to pay - the Commander has plenty of employees.  If there are enough LAMBs left over such that another henchman could be added as the most senior while obeying the other rules, you must always add and pay that henchman.

    Note that you may not be able to hand out all the LAMBs. A single LAMB cannot be subdivided. That is, all henchmen must get a positive integer number of LAMBs.

    Write a function called solution(total_lambs), where total_lambs is the integer number of LAMBs in the handout you are trying to divide. It should return an integer which represents the difference between the minimum and maximum number of henchmen who can share the LAMBs (that is, being as generous as possible to those you pay and as stingy as possible, respectively) while still obeying all of the above rules to avoid a revolt.  For instance, if you had 10 LAMBs and were as generous as possible, you could only pay 3 henchmen (1, 2, and 4 LAMBs, in order of ascending seniority), whereas if you were as stingy as possible, you could pay 4 henchmen (1, 1, 2, and 3 LAMBs). Therefore, solution(10) should return 4-3 = 1.

    To keep things interesting, Commander Lambda varies the sizes of the Lucky LAMB payouts. You can expect total_lambs to always be a positive integer less than 1 billion (10 ^ 9).

    Languages
    =========

    To provide a Python solution, edit solution.py
    To provide a Java solution, edit Solution.java

    Test cases
    ==========
    Your code should pass the following test cases.
    Note that it may also be run against hidden test cases not shown here.

    -- Python cases --
    Input:
    solution.solution(143)
    Output:
        3

    Input:
    solution.solution(10)
    Output:
        1

    -- Java cases --
    Input:
    Solution.solution(143)
    Output:
        3

    Input:
    Solution.solution(10)
    Output:
        1

    Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
    '''
    #generous follows a 2**n sequence, and stingy follows a fibbonachi sequence
    # fibboCache = {} 
    sumFibbo = 0
    nFibbo = 1
    fibboCache = {}
    def fibbonachi(n): #calculate fibbo of n
       
        if n in fibboCache: # look in fibbo cache
             return fibboCache[n] # get fibbo return
        else: #if fibbo was not computed previusly 
            if n == 1:
                value =  1                    
            elif n == 2:
                value =  1
            else:
                value = (fibbonachi(n -1) + fibbonachi(n-2))

        fibboCache[n] = value
        return value
    
    while sumFibbo <= total_lambs: # adds fibbo[n] to sum
       sumFibbo += fibbonachi(nFibbo) 
       
       nFibbo += 1
       
    
    
    sumTwoN =0
    nTwoN = 1
    while sumTwoN < total_lambs:
        if nTwoN == 1: 
            sumTwoN += 1
            nTwoN += 1
        else:
            sumTwoN += 2**(nTwoN-1)
            nTwoN += 1
        
        #through the comment of vnuno here (https://stackoverflow.com/questions/43429328/google-foobar-python-failure-on-two-tests-lovely-lucky-lambs-counting-of-seq)
        # I was able to understand that the test 9 that I had problems was due to having extra money left
        # so I was able to veryfy if the money left was enought to pay a extra henchan not the min nor the maximun salary
    leftOver = total_lambs - 2**(nTwoN-2) +1 #left over money
    lastTwohench = 2**(nTwoN-3)+2**(nTwoN-4) #minumiun amount of rule #3

    if leftOver > lastTwohench: #check money left 
        nTwoN +=1 #hire one more henchman
    
    #needs to be -2 since my code adds 1 at the end and the while counter only stops after the sum goes over total_lambs
    answer = int((nFibbo-2)- (nTwoN-2)) 
    return answer


def Chalenge3_1(x,y):
   
    def readMeFooBar():

        '''
        Bomb, Baby!
        ===========

        You're so close to destroying the LAMBCHOP doomsday device you can taste it! But in order to do so, you need to
        deploy special self-replicating bombs designed for you by the brightest scientists on Bunny Planet. There are 
        two types: Mach bombs (M) and Facula bombs (F). The bombs, once released into the LAMBCHOP's inner workings, 
        will automatically deploy to all the strategic points you've identified and destroy them at the same time. 

        But there's a few catches. First, the bombs self-replicate via one of two distinct processes: 
        Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
        Every Facula bomb spontaneously creates a Mach bomb.

        For example, if you had 3 Mach bombs and 2 Facula bombs, they could either produce 3 Mach bombs and 5 Facula bombs, 
        or 5 Mach bombs and 2 Facula bombs. The replication process can be changed each cycle. 

        Second, you need to ensure that you have exactly the right number of Mach and Facula bombs to destroy the 
        LAMBCHOP device. Too few, and the device might survive. Too many, and you might overload the mass capacitors
        and create a singularity at the heart of the space station - not good! 

        And finally, you were only able to smuggle one of each type of bomb - one Mach, one Facula - 
        aboard the ship when you arrived, so that's all you have to start with. (Thus it may be impossible to deploy 
        the bombs to destroy the LAMBCHOP, but that's not going to stop you from trying!) 

        You need to know how many replication cycles (generations) it will take to generate the correct amount of bombs
        to destroy the LAMBCHOP. Write a function solution(M, F) where M and F are the number of Mach and Facula bombs
        needed. Return the fewest number of generations (as a string) that need to pass before you'll have the exact 
        number of bombs necessary to destroy the LAMBCHOP, or the string "impossible" if this can't be done! M and F 
        will be string representations of positive integers no larger than 10^50. For example, if M = "2" and F = "1",
        one generation would need to pass, so the solution would be "1". However, if M = "2" and F = "4", it would not 
        be possible.

        Languages
        =========

        To provide a Java solution, edit Solution.java
        To provide a Python solution, edit solution.py

        Test cases
        ==========
        Your code should pass the following test cases.
        Note that it may also be run against hidden test cases not shown here.

        -- Java cases --
        Input:
        Solution.solution('2', '1')
        Output:
            1

        Input:
        Solution.solution('4', '7')
        Output:
            4

        -- Python cases --
        Input:
        solution.solution('4', '7')
        Output:
            4

        Input:
        solution.solution('2', '1')
        Output:
            1

        Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
        '''
    def tentativa1(): #do not pass some cases. need rework
        '''from collections import deque
        import math
        bombM = int(total_bombs[0]) 
        bombF = int(total_bombs[1])
        factor = [0]
        transf = [0]
        MFList= deque()
        answer = [None]
        def MbiggerThanF(M,F):
            factor[0] = math.floor(M/F)
            X1 = M-factor[0]*F
                
            return [X1,F]
            
        def FbiggerThanM(M,F):
            factor[0] = math.floor(F/M)
            X1 = F-factor[0]*M
            return [M,X1]

        def subtraction(A,B):
            if A>B:
                transf[0] += 1
                return (A-B,B)
                
            elif A<B:
                transf[0] += 1
                return (A, B-A)
                
            else:
                answer[0] = "impossible"
                return (0,0)     

        if bombM==1 and bombF==1:
            answer[0] = "impossible"
            

        elif bombM == 1 and bombM>0 and bombF>0:
            answer[0] = bombF - 1

        elif bombF == 1 and bombM>0 and bombF>0:
            answer[0] = bombM - 1

        elif bombM<1 or bombF<1:
            answer[0] = "impossible"
        else:
            
            if bombM>bombF:
                i = 1
            
                dataA = MbiggerThanF(bombM,bombF)[0]
                dataB = MbiggerThanF(bombM,bombF)[1] 
                MFList.append((dataA,dataB))
                while i!=0:
                    dataA = (MFList[0])[0]
                    dataB = (MFList[0])[1]
                    MFList.popleft()
                    if dataA>=1 and dataB>=1:
                        temp1 = subtraction(dataA,dataB)[0]
                        temp2 = subtraction(dataA,dataB)[1]
                        transf[0] -= 1
                        if temp1==1 and temp2 == 1:
                            #answer[0]= transf[0] + factor[0]
                            i=0
                        else:
                            MFList.append((temp1,temp2))
                    else:
                        i=0
                        
            elif bombM<bombF:
                
                i = 1
            
                dataA = FbiggerThanM(bombM,bombF)[0]
                dataB = FbiggerThanM(bombM,bombF)[1] 
                MFList.append((dataA,dataB))
                while i!=0:
                    dataA = (MFList[0])[0]
                    dataB = (MFList[0])[1]
                    MFList.popleft()
                    if dataA>=1 and dataB>=1:
                        temp1 = subtraction(dataA,dataB)[0]
                        temp2 = subtraction(dataA,dataB)[1]
                        transf[0] -= 1
                        if temp1==1 and temp2 == 1:
                            #answer[0]= transf[0] + factor[0]
                            i=0
                        else:
                            MFList.append((temp1,temp2))
                    else:
                        i=0

        if answer[0] == "impossible":
            print( str(answer[0]))
            #print(type(str(answer[0])))
        elif answer[0] == None:            
            answer[0] = transf[0] + factor[0]
            print ( str(answer[0]))
        # print(type(str(answer[0])))
        else:
        print( str(answer[0]))
        # print(type(str(answer[0])))
        '''
    
        

def answer(x, y):
    answer = 0
    m, f = int(x), int(y)
    i=0

    if m == 1 and f == 1:
        return str(answer)

    elif m<1 or f<1 or m==f:
        i=1
        return "impossible"

    elif m ==1:
        return str(f-1)

    elif f==1:
        return str(m-1)

    elif m>f:
        temp = int(m/f)
        answer += temp

        m = m - (temp*f)

    elif m<f:
        temp = int(m/f)
        answer += temp

        f = f - (temp*m)
    
    while i!=1:
        if m == 1 and f == 1:
            i=1
            return str(answer)
        elif m<1 or f<1 or m==f:
            i=1
            return "impossible"
        else:
            if m > f:
               
                m-=f
                answer += 1
            else:
               
                f-=m
                answer += 1       