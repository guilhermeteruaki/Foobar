from fractions import Fraction
def chalenge1( x, y):
    '''
    Prison Labor Dodgers
    ====================

    Commander Lambda is all about efficiency, including using her bunny prisoners for manual labor. But no one's been properly monitoring the labor shifts for a while, and they've gotten quite mixed up. You've been given the task of fixing them, but after you wrote up new shifts, you realized that some prisoners had been transferred to a different block and aren't available for their assigned shifts. And manually sorting through each shift list to compare against prisoner block lists will take forever - remember, Commander Lambda loves efficiency!

    Given two almost identical lists of prisoner IDs x and y where one of the lists contains an additional ID, write a function solution(x, y) that compares the lists and returns the additional ID.

    For example, given the lists x = [13, 5, 6, 2, 5] and y = [5, 2, 5, 13], the function solution(x, y) would return 6 because the list x contains the integer 6 and the list y doesn't. Given the lists x = [14, 27, 1, 4, 2, 50, 3, 1] and y = [2, 4, -4, 3, 1, 1, 14, 27, 50], the function solution(x, y) would return -4 because the list y contains the integer -4 and the list x doesn't.

    In each test case, the lists x and y will always contain n non-unique integers where n is at least 1 but never more than 99, and one of the lists will contain an additional unique integer which should be returned by the function.  The same n non-unique integers will be present on both lists, but they might appear in a different order, like in the examples above. Commander Lambda likes to keep her numbers short, so every prisoner ID will be between -1000 and 1000.

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

def chalenge2_2(total_lambs):   # def​ ​solution(total_lambs):
        '''Lovely Lucky LAMBs
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


    nGenerous
    nStingy
    sumGenerous
    sumStingy

    fibo
    twoNPower
    