#A Simple Drawing Program
#Daniel Kasprowicz

from Canvas import *
set_size(1200,800)

colour1="#FFFFFF" #initial white colour1
colour2="#000000" #initial black colour2

thicknessHighlight=[]

colours=["#000000","#808080","#800040","#FF0000","#FF7F27","#FFF200","#22B14C",\
         "#00A2E8","#3F48CC","#A349A4","#FFFFFF","#C3C3C3","#B97A57","#FFAEC9",\
         "#FFC90E","#EFE4B0","#B5E61D","#99D9EA","#7092BE","#C8BFE7"] #hex values for colours

def colourPicker():     #draws the colour picker
    a,b=0,0
    for i in range(20):
        if i==10:
            b=20
            a=0
        create_rectangle(370+a,20+b,390+a,40+b,fill=colours[i],outline="white")
        a+=20


def color():                        #draws the initial preview
    global p
    create_rectangle(580,20,620,60)
    p=create_rectangle(590,32,610,48,fill=colour1,outline=colour2,width=w)
    
def color2():                       #updates the preview, need a different function because have to delete the old preview first,
    global p                        #otherwise if thickness is changed from a bigger value to smaller the thinner updated
    delete(p)                       #version would be drawn on top of the old one and the thicker one would be still visible.
    p=create_rectangle(590,32,610,48,fill=colour1,outline=colour2,width=w)
    
def toolbar(r,o,p,l):
    create_rectangle(20,20,60,60,fill=r) #rectangle tool icon
    create_rectangle(30,32,50,48) 

    create_rectangle(60,20,100,60,fill=o) #oval tool icon
    create_oval(70,30,90,50)

    create_rectangle(100,20,140,60,fill=p) #pen tool icon
    
    create_line(115,25,110,50)
    create_line(115,25,120,25.5)
    create_line(120,25.5,115,50.5)
    create_line(110,50,115,50.5)

    create_line(110,50,111,55)
    create_line(111,55,115,50.5)

    create_rectangle(140,20,180,60,fill=l) #line tool icon
    create_line(150,30,170,50)

    create_text(100,10,text="Tools")
    create_text(230,10,text="Thickness")
    create_text(320,10,text="Colour mode")
    create_text(467,10,text="Colours")
    create_text(600,10,text="Preview")

    
def colourMode(f,o):

    create_rectangle(320,20,360,60,fill=f) #fill colour mode
    create_text(340,40,text="Fill")

    create_rectangle(280,20,320,60,fill=o) #outline colour mode
    create_text(300,40,text="Outline")
def thickness(thicknessHighlight):
    a,b=0,0
    for i in range(8):
        if i==4:
            b=20
            a=0
        create_rectangle(190+a,20+b,210+a,40+b,fill=thicknessHighlight[i])
        create_text(190+a+10,20+b+10,text=i+1)
        a+=20
    

colourPicker()
w=1
color()
thicknessHighlight=["grey","","","","","","",""]
thickness(thicknessHighlight)

toolbar("grey","","","") #initial tool being hilighted
colourMode("grey","white") #initial colour mode highlighter



tool=1 #initial tool selected
mode=1 #you guessed it.. this is also an initial value
def click(x,y,num):
    global tool,colour1,colour2,mode,thicknessHighlight,w,p
    a,b=0,0
    if x > 370 and y > 20 and x < 20*20+390 and y < 40+20:
        for i in range(20):
                if i==10:
                    b=20
                    a=0
                if x > 370+a and y > 20+b and x < 390+a and y < 40+b: #implementation of changing a colour
                    if mode ==1:
                        colour1=colours[i]
                    elif mode==2:
                        colour2=colours[i]
                    color2() #after a fill or outline colour has been changed the colour preview thingy gets updated

                a+=20
        a=0
        b=0
    if x>280 and y >20 and x <320 and y <60:    #outline colour
        mode=2
        colourMode("white","grey")
    if x>320 and y>20 and x < 360 and y <60:    #fill colour
        mode=1
        colourMode("grey","white")
    if x > 20 and y > 20 and x < 60 and y < 60: #select rectangle tool
        toolbar("grey","white","white","white") #highlight rectangle tool
        tool = 1
    if x > 60 and y > 20 and x < 100 and y < 60: #select oval tool
        toolbar("white","grey","white","white") #highlight oval tool
        tool = 2
    if x > 100 and y > 20 and x <140 and y < 60: #select pen tool
        toolbar("white","white","grey","white") #highlight pen tool
        tool = 3
    if x > 140 and y > 20 and x < 180 and y < 60: #select line tool
        toolbar("white","white","white","grey") #highlight ine tool
        tool=4
    if x > 20 and y > 60:
        global xx,yy,rectangle,oval,pen,line,w
        xx=x
        yy=y
        if tool ==1:
            rectangle=create_rectangle(xx,yy,x,y,fill=colour1,outline=colour2,width=w)
        elif tool ==2:
            oval = create_oval(xx,yy,x,y,fill=colour1,outline=colour2,width=w)
        elif tool==4:
            line=create_line(xx,yy,x,y,fill=colour2,width=w)
            
        set_mousemotion_handler( onMotion )
    for i in range(8):
        if i==4:
            b=20
            a=0
        if x > 190+a and y > 20+b and x < 210+a and y < 40+b:
            w=i+1
            thicknessHighlight=["white","white","white","white","white","white","white","white",] #clear all boxes
            thicknessHighlight[i]=["grey"] #highlight a button corresponding to that thickness
            thickness(thicknessHighlight)
            color2()    #update preview
        a+=20

def onMotion(x,y):
    global xx,yy,rectangle,tool,oval,pen,colour1,colour2,line,w

    if x<20 or y<100:    #prevent covering the toolbar with drawings, if mouse is moved fast enough it will pass that point anyways..
        unset_mousemotion_handler()
    
    if tool ==1:
        delete(rectangle)
        rectangle=create_rectangle(xx,yy,x,y,fill=colour1,outline=colour2,width=w)
    elif tool == 2:
        delete(oval)
        oval = create_oval(xx,yy,x,y,fill=colour1,outline=colour2,width=w)
    elif tool ==3:
        create_line(xx,yy,x,y,fill=colour2,width=w)
        xx=x
        yy=y
    elif tool==4:
        delete(line)
        line=create_line(xx,yy,x,y,fill=colour2,width=w)
        
def onMouseUp(x,y,n):
    unset_mousemotion_handler()
        


set_mousedown_handler( click )

set_mouseup_handler( onMouseUp )

run()
