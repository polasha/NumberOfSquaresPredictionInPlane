
# import sys> access the fuction and defined the module
import sys
print("how many test do you want>")
t = int(input())  # test case, how many time we test

print("how many points do you want to put>")
while (t):
    n = int(input())  # define how many pairs (x, y) input
    s = set()   # iterable element(tuple , list)
    for i in range(n):
        line = input().split()  #split input by seperator
        s.add((int(line[0]), int(line[1])))
    count = 0

    a = list(s)  #create list
    for i in range(n - 1):
        for j in range(i + 1, n):
            x1, y1 = a[i][0], a[i][1]  # make nested list, first element of first nested list
            x2, y2 = a[j][0], a[j][1]
            if (x1 > x2):
                tmp = x1
                x1 = x2
                x2 = tmp
                tmp = y1
                y1 = y2
                y2 = tmp
            x3, y3 = x2 + (y1 - y2), y2 + (x2 - x1)  # x2= x1, square aligned with axes, found potential point, side = y1-y2, x3= x2 + side, similarly y3
            x4, y4 = x1 + (y1 - y2), y1 + (x2 - x1)  #  similiarly x4 and y4
            if ((x3, y3) in s and (x4, y4) in s):
                count += 1
            print((x1,y1))
            print((x2,y2))
            print((x3,y3))
            print((x4,y4))
            print()
            x3, y3 = x2 - (y1 - y2), y2 - (x2 - x1)   # for non aligned squares, x3= x2- side , same for other parametes
            x4, y4 = x1 - (y1 - y2), y1 - (x2 - x1)
            if ((x3, y3) in s and (x4, y4) in s):
                count += 1
        print((x1,y1))
        print((x2,y2))
        print((x3,y3))
        print((x4,y4))
        print()

    sys.stdout.write(str(int(count / 4)) + "\n")    #print command but add new line



    t -= 1   #subtraction