from Canvas import *
from string import *
from operator import itemgetter 

set_size(600,600)
offset=50.0
size=50.0
width=2.0
currenti=0
currentj=0

oldi=0

oldj=0

l=[[0,0,0,0,0,0,0,0,0],\
   [0,0,0,0,0,0,0,0,0],\
   [0,0,0,0,0,0,0,0,0],\
   [0,0,0,0,0,0,0,0,0],\
   [0,0,0,0,0,0,0,0,0],\
   [0,0,0,0,0,0,0,0,0],\
   [0,0,0,0,0,0,0,0,0],\
   [0,0,0,0,0,0,0,0,0],\
   [0,0,0,0,0,0,0,0,0]]
v=[[0,0,0,0,0,0,0,0,0],\
   [0,0,0,0,0,0,0,0,0],\
   [0,0,0,0,0,0,0,0,0],\
   [0,0,0,0,0,0,0,0,0],\
   [0,0,0,0,0,0,0,0,0],\
   [0,0,0,0,0,0,0,0,0],\
   [0,0,0,0,0,0,0,0,0],\
   [0,0,0,0,0,0,0,0,0],\
   [0,0,0,0,0,0,0,0,0]]

remove_square_change = True
square_remove_change = True

coords = [(2.0/7.0,2.0/7.0),(4.0/7.0,2.0/7.0),(6.0/7.0,2.0/7.0),(2.0/7.0,4.0/7.0),(4.0/7.0,4.0/7.0),(6.0/7.0,4.0/7.0),(2.0/7.0,6.0/7.0),(4.0/7.0,6.0/7.0),(6.0/7.0,6.0/7.0)]

#map(list, zip(*l))
##
##l[0][0]=[1,2,3,4,5,6,7,8,9]
##l[0][1]=[1,2,3,4,5,6,7,8,9]



#v[3][5]=6
#print v[3][5]
#print l

rectangles=[]
txt=[]
#v=[]

for i in range(9):
        #l+=[[0,0,0,0,0,0,0,0,0]]
        rectangles+=[[0,0,0,0,0,0,0,0,0]]
        txt+=[[0,0,0,0,0,0,0,0,0]]
        #v+=[[0,0,0,0,0,0,0,0,0]]
lines=[]

n=0
txtcolour="black"



def grid(currenti,currentj):
        global size, offset, width, rectangles, lines, txt, oldi, oldj
    

        for i in range(9):
                for j in range(9):
                        if i==currenti and j==currentj:
                                f="#C3C3C3"
                        else:
                                f="white"
                
                        rectangles[i][j]=create_rectangle(offset+(i*size),offset+(j*size),offset+size+(i*size),offset+size+(j*size),fill=f)
            
                        if l[i][j]!=0:
                                txt[i][j]=create_text(float(offset+(i*size))+size/2,float(offset+(j*size))+size/2,text=l[i][j])
                #txt[i][j]=create_text(float(offset+size+(i*size))+size/2,float(offset+size+(j*size))+size/2,text=l[i][j])

        #txt[1][4]=create_text(float(offset+(1*size))+size/2,float(offset+(4*size))+size/2,text=l[0][2])
            
        for i in range(10):
                                      
                if i==3 or i==6 or i==0 or i==9:
                        lines+=[create_line(offset+(i*size),offset,offset+(i*size),offset+(size*9),width=width)]
                        lines+=[create_line(offset,offset+(i*size),offset+(size*9),offset+(i*size),width=width)]
        oldi,oldj=currenti,currentj

        #create_rectangle(offset+(3*size),offset/2+(10*size),offset+size+(5*size),offset/2+size+(10*size))
        #create_text(offset+(4.5*size),offset/2+(10.5*size),text="SOLVE")

        create_rectangle(offset + (3*size),
                         offset + (10*size),
                         offset + (6*size),
                         offset + (11*size))
        create_text(offset + (4.5*size),
                    offset + (10.5*size),        
                    text="SOLVE")
        
def line():
    global lines
    for i in range(10):
        if i==3 or i==6 or i==0 or i==9:
            
            lines+=[create_line(offset+(i*size),offset,offset+(i*size),offset+(size*9),width=width)]
            lines+=[create_line(offset,offset+(i*size),offset+(size*9),offset+(i*size),width=width)]
            
def clear():
    for i in range(9):
        for j in range(9):
            delete(rectangles[i][j])

    for i in range(8):
        delete(lines[i])
            
def click(x,y,n):
        global currenti, currentj, txtcolour
        
        txtcolour = "black"

        if x>offset + (3*size) and y>offset + (10*size) and x<offset + (6*size) and y<offset + (11*size):

                solve()
        

        for i in range(9):
                for j in range(9):
                        if x > offset+(i*size) and y > offset+(j*size) and x <offset+size+(i*size) and y<offset+size+(j*size):
                                currenti=i
                                currentj=j
                                
                                
                               
                                drawBox(currenti,currentj)
                        
                                

def drawBox(currenti,currentj):
    global oldi, oldj, lines, txtcolour,l
    delete(rectangles[oldi][oldj])
    rectangles[oldi][oldj]=create_rectangle(offset+(oldi*size),offset+(oldj*size),offset+size+(oldi*size),offset+size+(oldj*size),fill="white")
    delete(txt[oldi][oldj])

    
    
    if l[oldi][oldj]!=0:
        if type(l[oldi][oldj]) is list:
            for i in range(9):
                #pass
                try:
                    txt[oldi][oldj] += create_text(float(offset+(oldi*size))+size*coords[i][0],float(offset+(oldj*size))+size*coords[i][1],text=l[oldi][oldj][i],fill=txtcolour)
                except(IndexError):
                    pass
                                
                
        else:
            txt[oldi][oldj]=create_text(float(offset+(oldi*size))+size/2,float(offset+(oldj*size))+size/2,text=l[oldi][oldj],fill=txtcolour)

        
    
    delete(rectangles[currenti][currentj])
    rectangles[currenti][currentj]=create_rectangle(offset+(currenti*size),offset+(currentj*size),offset+size+(currenti*size),offset+size+(currentj*size),fill="#C3C3C3")
    delete(txt[currenti][currentj])

    
    if l[currenti][currentj]!=0:
        if type(l[currenti][currentj]) is list:
            for i in range(9):
                try:
                    txt[currenti][currentj] += create_text(float(offset+(currenti*size))+size*coords[i][0],float(offset+(currentj*size))+size*coords[i][1],text=l[currenti][currentj][i],fill=txtcolour)
                except(IndexError):
                    pass
        else:
            txt[currenti][currentj]=create_text(float(offset+(currenti*size))+size/2,float(offset+(currentj*size))+size/2,text=l[currenti][currentj],fill=txtcolour)
            
    line()
    oldi,oldj=currenti,currentj
                

def enter(key):
        global currenti, currentj, txt, txtcolour

        #####try:
        #####        l[currenti][currentj]=int(key)
        #####except(ValueError):
        #####        pass

        try:
                if(int(key) == 0):
                        l[currenti][currentj]=int(key)
                else:
                        if l[currenti][currentj] == 0:
                                l[currenti][currentj]=int(key)
                        else:
                                if type(l[currenti][currentj]) is int:
                                        l[currenti][currentj] = list((l[currenti][currentj], int(key)))
                                elif type(l[currenti][currentj]) is list:
                                        l[currenti][currentj].append(int(key))

        except(ValueError):
                pass
                        

        
##        if key=="space":
##                new=map(list, zip(*l))
##
##                #print new
##                for i in range(9):
##                        for j in range(9):
##                                print new[i][j],
##                        print
##        else:
        txtcolour = "black"
        drawBox(currenti,currentj)


def solve():
        
        global v,n,l
        
        numbers=[1,2,3,4,5,6,7,8,9]

        #for i in range(9):
            #for j in range(9):
                #if type(l[i][j]) is list:
                    #l[i][j] = 0
        
        #v=[]
        n=map(list, zip(*l))
        
        for i in range(9):
                for j in range(9):
                    print n[i][j],
                print
        print
        
        for i in range(9):
                for j in range(9):
                        v[i][j]=[1,2,3,4,5,6,7,8,9]

##        for i in range(9):
##                for j in range(9):
##                        v[i][j]=[1,2,3,4,5,6,7,8,9]
##                        print v[i][j]


##        for i in range(9):
##                for j in range(9):
##                        print v[i][j],
##                print

        #print v[0][0]

        for i in range(9):
                for j in range(9):
                        if n[i][j] != 0:  # n contains no zeros so those will be skipped

                                v[i][j]=n[i][j]

                                print v[i][j],
                        else:
                                print "0",
                print

        print
        

        remove()
        
def remove():
        global square_remove_change,remove_square_change

        
        count = 0
        for i in range(9):
                for j in range(9):
                        try:
                                if len(v[i][j]) == 1:
                                        v[i][j] = v[i][j][0]
                                        count = count + 1

                        except(AttributeError,ValueError,TypeError):
                                pass
                                
                        if type(v[i][j]) is int:
                                for k in range(9):
                                        try:
                                                v[i][k].remove(v[i][j])

                                                count = count + 1
                                                #print str(i) + " " + str(k),
                                                #print v[i][k]
                                        except(AttributeError,ValueError):
                                                pass
                                        #print
                                for k in range(9):
                                        try:
                                                v[k][j].remove(v[i][j])

                                                count = count + 1
                                                #print str(k) + " " + str(j),
                                                #print v[k][j]
                                        except(AttributeError,ValueError):
                                                pass
        for i in range(9):
                for j in range(9):
                        print v[i][j],
                print
                
                
        if count != 0:
                print "###REMOVE###"
                print
                print "count: " + str(count)
                print
                
                remove_square_change = True
                square_remove_change = True
                
                print "remove to square: " + str(remove_square_change)
                print "square to remove: " + str(square_remove_change)
                
                remove()
        else:
                print "###REMOVE###"
                
                remove_square_change = False
                print
                print "count: 0"
                print

                print "remove to square: " + str(remove_square_change)
                print "square to remove: " + str(square_remove_change)

                if remove_square_change == False and square_remove_change == False:
                        #guess()
                        display()
                elif remove_square_change == True or square_remove_change == True:
                        squares()



def squares():
        global square_remove_change,remove_square_change
        

        
        count = 0


        
        #square 1
        #rangex = 3
        #rangey = 3

        squarelist = [[(0,3),(0,3)],[(3,6),(0,3)],[(6,9),(0,3)]],\
                      [[(0,3),(3,6)],[(3,6),(3,6)],[(6,9),(3,6)]],\
                      [[(0,3),(6,9)],[(3,6),(6,9)],[(6,9),(6,9)]],\
                      
        for a in range(3):
                for b in range(3):
                        
                        rangex = squarelist[a][b][0]
                        rangey = squarelist[a][b][1]

                        #print rangex
                        #print rangey
                       # print
                        
                        for i in range(*rangex):
                                for j in range(*rangey):
                                        try:
                                                if len(v[i][j]) == 1:
                                                        v[i][j] = v[i][j][0]
                                                        count = count + 1
                                                        
                                        except(AttributeError,ValueError,TypeError):
                                                pass
                                        
                                        if type(v[i][j]) is int:
                                                for x in range(*rangex):
                                                        for y in range(*rangey):
                                                                try:
                                                                        v[x][y].remove(v[i][j])
                                                                        count = count + 1
                                                                        
                                                                except(AttributeError,ValueError):
                                                                        pass  



        for i in range(9):
                for j in range(9):
                        print v[i][j],
                print

                
        if count != 0:
                print "###SQUARE###"
                print
                print "count: " + str(count)
                print

                square_remove_change = True
                remove_square_change = True
                
                print "remove to square: " + str(remove_square_change)
                print "square to remove: " + str(square_remove_change)
                
                squares()
        else:
                print "###SQUARE###"
                square_remove_change = False
                print
                print "count: 0"
                print

                print "remove to square: " + str(remove_square_change)
                print "square to remove: " + str(square_remove_change)
                
                if remove_square_change == False and square_remove_change == False:
                        #guess()
                        display()
                elif remove_square_change == True or square_remove_change == True:
                        remove()
                
def guess():
        global square_remove_change,remove_square_change

        print check()
        
       ## temp = v[0][0]

        
        
        ##square_remove_change = True
        ##remove_square_change = True
        
        ##remove()

def check():
        #checks for sudoku rules

        
        
        square = [0,0,0,0,0,0,0,0,0]

        for i in range(9):
                x = [0,0,0,0,0,0,0,0,0]
                y = [0,0,0,0,0,0,0,0,0]
                
                column = map(itemgetter(i), v)
                
                for j in range(9):
                        x[j] = v[i].count(j+1)
                        y[j] = column.count(j+1)

                print "x" + str(i) + ": ",
                print x
                print "y" + str(i) + ": ",
                print y
                
                for k in range(9):
                        if x[k] > 1:
                                return False
                        if y[k] > 1:
                                return False


##        for i in range(9):
##                for j in range(9):
##                        
##                       print v[j][i],
##                print





#       1. set known numbers in the array DONE
#       2. for each empty rectangle check for known numbers horisontally, vertically and in the same square and delete them from the array
        #DONE
#       3. try to solve the rest...


def display():
        global txtcolour
        

        for i in range(9):
                for j in range(9):

                        #if v[j][i] != l[i][j]:
                        l[i][j] = v[j][i]

                        currenti=i
                        currentj=j

                        txtcolour = "red"

                                
                        drawBox(currenti,currentj)
                                
                        
                                #print l[i][j],
                #print
        

grid(currenti=0,currentj=0)

set_mousedown_handler(click)

set_keydown_handler(enter)


run()
