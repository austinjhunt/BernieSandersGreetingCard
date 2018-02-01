# Austin Hunt
# valentineGreeting.py
# Purpose: Create a valentine's day card with moving arrow and heart
# Certification of Authenticity:
# I certify that this lab is entirely my own work.

from graphics import *
import time

def valentineGreeting () :

    # use for loop to return x and y values of click points to basically
    # "draw" portrait, as there is no "Bernie Sanders" class

    #create a square window with height and width of 500
    #set coordinates to allow for easier mapping of design elements
    winWidth = 500
    winHeight = 500
    win = GraphWin("Bernie Valentine", winWidth, winHeight)
    win.setCoords(0.0,0.0, 10.0,10.0)

    #create triangle for bottom of heart
    ptA = Point(5,2.5)
    ptB = Point(1.75,7.5)
    ptC = Point(8.25,7.5)
    heartBottom = Polygon (ptA,ptB,ptC)

    #assign variable heart color, set bottom of heart to color
    hotPink = color_rgb(255,0,100)
    heartBottom.setFill(hotPink)
    heartBottom.setOutline(hotPink)
    heartBottom.draw(win)

    #create two circles for top of heart
    cir1 = Circle(Point(3.75,7.5),2.05)
   
    cir2 = Circle(Point(6.25,7.5),2.05)

    #make circles blend with rest of heart
    cir1.setFill(hotPink)
    cir1.setOutline(hotPink)
    cir1.draw(win)
    
    cir2.setFill(hotPink)
    cir2.setOutline(hotPink)
    cir2.draw(win)

    
 
    #use these points to widen up the bottom of the heart, make it 
    #line up better with top of heart
    ptD = Point(1.9,6.6)
    ptE = Point(8.1, 6.6)

    #second, wider heartbottom to make it blend together more

    bottomHeart2 = Polygon(ptA, ptD, ptE)
    bottomHeart2.setFill(hotPink)
    bottomHeart2.setOutline(hotPink)
    bottomHeart2.draw(win)

    #points for coat polygon, left side
    ptF= Point(3.45, 4.65)
    ptG= Point(3.89, 4.95)
    ptH= Point(4, 5.15)
    ptI= Point(4.26, 5.29)

    #points for coat polygon, right side
    ptJ= Point(4.3,5.35)
    ptK= Point( 5.7, 5.35)
    ptK2= Point(5.74, 5.29)
    ptL = Point(6, 5.15)
    ptM= Point(6.11, 4.95)
    ptN= Point(6.55,4.65)

    #easiest part, back layer, create black coat with polygon class          
    coat = Polygon(ptA,ptF,ptG,ptH,ptI,ptJ,ptK,ptL,ptM,ptN)
    coat.setFill("black")
    coat.draw(win)

    

    #points on the left side of shirt, to be used in shirt polygon
    ptO = Point(4.47, 4.77)
    ptP = Point(4.41, 4.23)
    ptQ = Point(4.5, 4.1)
    ptR = Point(4.39, 4.55)
    ptS = Point(4.37, 3.43)

    #points on top/center of shirt, to be used in shirt polygon
    ptT = Point(ptA.getX()-.15, 4.3)
    ptU = Point(ptA.getX()+.15, 4.3)
    
    #points on right side of shirt, to be used in shirt polygon
    ptV = Point (5.53, 4.77)
    ptW = Point(5.59, 4.23)
    ptX = Point(5.5, 4.1)
    ptY = Point(5.61, 4.55)
    ptZ = Point(5.63, 3.43)
    
    #use polygon to create light colored shirt, layer above coat
    shirt = Polygon(ptO, ptP, ptQ, ptR, ptS, ptA, ptZ, ptY, ptX, ptW,
                    ptV, ptU, ptT)
    shirt.setFill(color_rgb(214,203, 242))
    shirt.draw(win)

    #create points for shadow polygon
    ptA1 = Point(ptT.getX()-.07,4.15)
    ptA2 = Point(ptU.getX()+.07,4.15)
    ptA3 = Point(ptA1.getX(),4)
    ptA4 = Point(ptA2.getX(), 4)
    ptA5 = Point(ptA.getX(),4.15)

    #shadow above just above the tie, use above points
    shadow = Polygon(ptT,ptU,ptA2,ptA4,ptA5, ptA3,ptA1)
    shadow.setFill(color_rgb(76,62,112))
    shadow.draw(win)

    #assign variables these X values for convenience
    #when creating left/right collar sections
    A1X = ptA1.getX()
    A4X = ptA4.getX()

    #left section of collar
    leftFlip = Line(ptA1, Point(A1X,3.75))
    leftFlip.draw(win)
    leftFlip2 = Line(Point(A1X,3.75), ptQ)
    leftFlip2.draw(win)
    leftFold = Polygon(Point(A1X,3.75), Point(A1X-.2, 3.55), ptQ)
    leftFold.setFill(color_rgb(179,169,204))
    leftFold.draw(win)

    #shadow above just above the tie 
    shadow = Polygon(ptT,ptU,ptA2,ptA4,ptA5, ptA3,ptA1)
    shadow.setFill(color_rgb(76,62,112))
    shadow.draw(win)

    #right section of collar
    rightFlip = Line(ptA4, Point(A4X, 3.75))
    rightFlip.draw(win)
    rightFlip2 = Line (Point(A4X,3.75),ptX)
    rightFlip2.draw(win)
    rightFold = Polygon(Point(A4X,3.75),Point(A4X+.2, 3.55), ptX)
    rightFold.draw(win)
    rightFold.setFill(color_rgb(179, 169, 204))

  

    #create tie

    ptTie1 = Point(4.8,4)
    ptTie2 = Point(5,4.15)

    #tie right side
    ptTie3 = Point(5.2,4)
    ptTie4 = Point(5.1, 3.8)
    ptTie5 = Point(5.2,3.3)
    ptTie6 = Point(5.2, 2.75)

    #tie left side

    ptTie7 = Point(4.8,4)
    ptTie8 = Point(4.9, 3.8)
    ptTie9 = Point(4.8,3.3)
    ptTie10 = Point(4.8, 2.75)

  
    #use polygon to create tie using above points
    tie = Polygon(ptTie1,ptTie2,ptTie3,ptTie4,ptTie5,ptTie6,ptA,
                  ptTie10,ptTie9,ptTie8,ptTie7)
    tie.setFill(color_rgb(64,96,122))
    tie.draw(win)

    #tie shadow, drawn after tie so it is visible

    tieShadow = Polygon (ptTie4, Point(4.9,3.7),Point(5.135,3.6))
    tieShadow.setFill(color_rgb(44,66,84))
    tieShadow.draw(win)

    #tie decorations
    tieLine = color_rgb (95,158,179)

    #give the tie some flare with some verticle/slanted blue lines
    # the lines are bent at the middle, which means they consist of
    # two lines each

    tieDec1 = Line (Point(4.93,3.68), Point(4.87,3.29))
    tieDec1.setFill(tieLine)
    tieDec1.draw(win)
    tieDec2 = Line (Point(4.87,3.29),Point(4.87,2.7))
    tieDec2.setFill(tieLine)
    tieDec2.draw(win)
    tieDec3 = Line (Point(4.99,3.6),Point(5,2.5))
    tieDec3.setFill(tieLine)
    tieDec3.draw(win)
    tieDec4 = Line (Point(5.07,3.56),Point(5.13,3.29))
    tieDec4.setFill(tieLine)
    tieDec4.draw(win)
    tieDec5 = Line (Point(5.13,3.29),Point(5.15,2.67))
    tieDec5.setFill(tieLine)
    tieDec5.draw(win)

    #make coat look more separated from the under shirt, gives more
    #definition to coat
    zipper = Line(Point(4.44,4.66),Point(4.44,3.32))
    zipper.setFill(color_rgb(64,96,122))
    zipper.setWidth(4)
    zipper2 = zipper.clone()
    zipper2.move(1.15,0)
    zipper.draw(win)
    zipper2.draw(win)

    #to make it look like coat collar is wrapping around neck 
    collarCrest = Line (Point(5.58,4.66),Point(5.87,4.95))
    collarCrest.setFill(color_rgb(64,96,122))
    collarCrest.setWidth(3)
    collarCrest.draw(win)
    collarCrest2 = Line (Point(4.42,4.66),Point(4.08,5.02))
    collarCrest2.setFill(color_rgb(64,96,122))
    collarCrest2.setWidth(3)
    collarCrest2.draw(win)

    #create a base for the head, use multiple ovals of different
    #coloration use color picker to select various skin tones that
    #show difference in lighting 

    headBase = Oval(Point(3.77,8.13),Point(6.2,4.6))
    headBase.setFill(color_rgb(214,139,144))
    headBase.setOutline(color_rgb(214,139,144))
    headBase.draw(win)
    headBase2 = Oval(Point(4.3,8.1),Point(6,4.9))
    headBase2.setFill(color_rgb(245,179,179))
    headBase2.setOutline(color_rgb(245,179,179))
    headBase2.draw(win)
    headBase3 = Oval(Point(4.7,8.0),Point(5.7,7.2))
    headBase3.setFill(color_rgb(247,205,205))
    headBase3.setOutline(color_rgb(247,205,205))
    headBase3.draw(win)
    headShine = Oval (Point(5.17,7.75),Point(5.43,7.55))
    headShine.setFill(color_rgb(250,235,235))
    headShine.setOutline(color_rgb(250,235,235))
    headShine.draw(win)

    #create hair, using a collection of points, use for loop to click
    # and return x and y values for each point, then draw polygon with
    # points
    hair1 = Point(3.98,6.47)
    hair1_1= Point(3.68,7.35)
    hair1_2 = Point(3.65,7.37)
    hair2 = Point(3.95,6.4)
    hair3 = Point(3.7,6.53)
    hair4 = Point(3.65,6.93)
    hair5 = Point(3.76,7.2)
    hair6 = Point(3.81,7.33)
    hair7 = Point(3.87,7.82)
    hair7_1 = Point(3.9,7.73)
    hair8 = Point(4.05,7.7)
    hair9 = Point(4.19,8.)
    hair10 = Point(4.3,8.1)
    hair10_1=Point(4.32,8.07)
    hair11 = Point(4.53,8.2)
    hair12 = Point(4.91,8.27)
    hair12_1 = Point(5.05,8.23)
    hair13 = Point(5.04,8.35)
    hair14 = Point(4.97,8.3)
    hair15 = Point(5.35,8.23)
    hair16 = Point(5.75, 8.28)
    hair16_1= Point(5.7,8.2)
    hair16_2=Point(5.67,8.16)
    hair17 = Point(5.97,7.95)
    hair18 = Point(6.12, 7.79)
    hair19 = Point(6.1, 7.63)
    hair20 = Point(6.29,7.37)
    hair21 = Point (6.35,7.17)
    hair21_1= Point(6.3,7.1)
    hair22 = Point(6.37, 6.58)
    hair23 = Point(6.17,6.65)

    #connect hair points together to create polygon, whole shape won't
    #be visible since it is behind headbase 

    hair = Polygon(hair1,hair2,hair3,hair4,hair5,hair1_1,hair1_2,hair6,
                   hair7,hair7_1,hair8,hair9,hair10,hair10_1,hair11,
                   hair12,hair13,hair14,hair12_1,hair15,hair16,hair16_1,
                   hair16_2,hair17,hair18,hair19,hair20,hair21,hair21_1,
                   hair22,hair23)

    # set fill of the hair (base) to a light gray

    hair.setFill(color_rgb(217,217,217))
    hair.setOutline("gray")
    hair.draw(win)

    #need to create a new head base to ensure that hair is layered
    # behind head

    headBase = Oval(Point(3.77,8.13),Point(6.1,5.2))
    headBase.setFill(color_rgb(214,139,144))
    headBase.setOutline(color_rgb(214,139,144))
    headBase.draw(win)

    #since Bernie is getting up there in years, give him some wrinkles
    # and rolls; it adds character!

    neckRoll = Polygon(Point(4.9,4.84),Point(4.6,5.03),Point(4.48,5.17),
                       Point(4.44,5.29),Point(4.4,5.51),Point(4.4,5.71),
                       Point(4.4, 5.79),Point(5.07,5.69))
    neckRoll.setFill(color_rgb(180,100,100))
    neckRoll.setOutline(color_rgb(180,100,100))
    neckRoll.draw(win)

    neckRoll2 = Polygon(Point(4,5.31),Point(4.16,5.17),Point(4.22,5.05),
                        Point(4.28,4.9),Point(4.5,4.7),Point(4.34,4.94),
                        Point(4.24,5.13),Point(4.14,5.29),Point(4,5.37))
    neckRoll2.setFill(color_rgb(180,100,100))
    neckRoll2.setOutline(color_rgb(180,100,100))
    neckRoll2.draw(win)

    #other part of new head base, overlap with neckroll
    headBase2 = Oval(Point(4.3,8.1),Point(6,4.8))
    headBase2.setFill(color_rgb(245,179,179))
    headBase2.setOutline(color_rgb(245,179,179))
    headBase2.draw(win)
    headBase3 = Oval(Point(4.7,8.0),Point(5.7,7.2))
    headBase3.setFill(color_rgb(247,205,205))
    headBase3.setOutline(color_rgb(247,205,205))
    headBase3.draw(win)
    headShine = Oval (Point(5.17,7.75),Point(5.43,7.55))
    headShine.setFill(color_rgb(250,235,235))
    headShine.setOutline(color_rgb(250,235,235))
    headShine.draw(win)

    #now, add some more layers to the hair, basically create hair for
    # one side, and flip along the vertical axis at x = 5 (width/2)

    rightHair1 = Point(5.65,8.15)
    rightHair2 = Point(5.9,7.7)
    rightHair3 = Point(5.96, 7.25)
    rightHair4 = Point(6, 6.6)
    rightHair5 = Point(6.13, 6.71)
    rightHair6 = Point(6.23,6.67)
    rightHair7 = Point(6.19,7.41)
    rightHair8 = Point(6.07, 7.71)
    

    rightHair = Polygon(rightHair1,rightHair2,rightHair3,rightHair4,
                        rightHair5,rightHair6,rightHair7,rightHair8)
    rightHair.setFill(color_rgb(238,238,238))
    rightHair.setOutline(color_rgb(238,238,238))
    rightHair.draw(win)

    #create hair other side, where x values of all points used are
    #reflections of the other points along x = 5 

    leftHair1 = Point(4.35,8.15)
    leftHair2 = Point(4.1,7.7)
    leftHair3 = Point(4.04,7.25)
    leftHair4 = Point(4,6.6)
    leftHair5 = Point(3.87,6.71)
    leftHair6 = Point(3.77,6.67)
    leftHair7 = Point(3.81,7.41)
    leftHair8 = Point(3.93,7.71)

    #give left side of head a darker tone (to create appearance of
    #shadow, give hair fill a lower, darker rgb value)
    leftHair = Polygon(leftHair1,leftHair2,leftHair3,leftHair4,
                       leftHair5,leftHair6,leftHair7,leftHair8)
    leftHair.setFill("gray")
    leftHair.setOutline("gray")
    leftHair.draw(win)

    #an active politician such as Bernie should be able to hear,
    #shouldn't he? again, use points to create a polygon for left ear

    leftEar1 = Point(3.92,6.59)
    leftEar2 = Point(3.82, 6.67)
    leftEar3 = Point(3.72,6.67)
    leftEar4 = Point(3.65, 6.61)
    leftEar5 = Point(3.6, 6.55)
    leftEar6 = Point(3.55, 6.39)
    leftEar6_1 = Point(3.56,6.35)
    leftEar6_2= Point(3.58,6.32)
    leftEar7 = Point(3.6,6.29)
    leftEar8 = Point(3.63,6.17)
    leftEar9 = Point(3.68,6)
    leftEar10 = Point(3.7, 5.83)
    leftEar11 = Point(3.75,5.79)
    leftEar12 = Point(3.84,5.79)
    leftEar13 = Point(3.92,5.81)

    leftEar = Polygon(leftEar1,leftEar2,leftEar3,leftEar4,leftEar5,
                      leftEar6,leftEar6_1,leftEar6_2,leftEar7,leftEar8,
                      leftEar9,leftEar10, leftEar11,leftEar12,leftEar13)
    leftEar.setFill(color_rgb(214,139,144))
    leftEar.setOutline(color_rgb(214,139,144))
    leftEar.draw(win)

    #give some depth to the ear, add crevices/shadows with lines and
    #ovals, use darker rgb value than that of ear base
    leftEarShadow = Oval(Point(3.62,6.52),Point(3.85,6.35))
    leftEarShadow.setFill(color_rgb(153,95,96))
    leftEarShadow.setOutline(color_rgb(153,95,96))
    leftEarShadow.draw(win)

    leftEarShadow2 = Oval(Point(3.82,6.32),Point(3.92,5.97))
    leftEarShadow2.setFill(color_rgb(160,90,90))
    leftEarShadow2.setOutline(color_rgb(160,90,90))
    leftEarShadow2.draw(win)

    leftEarLine1 = Line(Point(3.72,6.29),Point(3.8,5.93))
    leftEarLine2 = Line(Point(3.8,5.93),Point(3.86,5.89))
    leftEarLine3 = Line (Point(3.86,5.89),Point(3.92,5.87))

    leftEarLine1.setFill(color_rgb(153,95,96))
    leftEarLine2.setFill(color_rgb(153,95,96))
    leftEarLine3.setFill(color_rgb(153,95,96))

    leftEarLine1.draw(win)
    leftEarLine2.draw(win)
    leftEarLine3.draw(win)

    #now, create another set of points for other ear, with ALL x values
    #for left ear reflected across x = 5, should mirror ear to right
    #side 

    rightEar1 = Point(6.08,6.59)
    rightEar2 = Point(6.18,6.67)
    rightEar3 = Point(6.28,6.67)
    rightEar4 = Point(6.35,6.61)
    rightEar5 = Point(6.4,6.55)
    rightEar6 = Point(6.45,6.39)
    rightEar7 = Point(6.44,6.35)
    rightEar8 = Point(6.42,6.32)
    rightEar9 = Point(6.4,6.29)
    rightEar10 = Point(6.37,6.17)
    rightEar11 = Point(6.32,6)
    rightEar12 = Point(6.3, 5.83)
    rightEar13 = Point(6.25,5.79)
    rightEar14 = Point(6.16,5.79)
    rightEar15 = Point(6.08,5.81)

    rightEar = Polygon(rightEar1,rightEar2,rightEar3,rightEar4,
                       rightEar5,rightEar6,rightEar7,rightEar8,
                       rightEar9,rightEar10,rightEar11,rightEar12,
                       rightEar13,rightEar14,rightEar15)
    rightEar.setFill(color_rgb(214,139,144))
    rightEar.setOutline(color_rgb(214,139,144))
    rightEar.draw(win)

    rightEarShadow = Oval(Point(6.38,6.52),Point(6.15,6.35))
    rightEarShadow.setFill(color_rgb(153,95,96))
    rightEarShadow.setOutline(color_rgb(153,95,96))
    rightEarShadow.draw(win)

    rightEarShadow2 = Oval(Point(6.18,6.32),Point(6.08,5.97))
    rightEarShadow2.setFill(color_rgb(153,95,96))
    rightEarShadow2.setOutline(color_rgb(153,95,96))
    rightEarShadow2.draw(win)

    rightEarLine1 = Line(Point(6.28,6.29),Point(6.2,5.93))
    rightEarLine2 = Line(Point(6.2,5.93),Point(6.14,5.89))
    rightEarLine3 = Line(Point(6.14,5.89),Point(6.08,5.87))

    rightEarLine1.setFill(color_rgb(153,95,96))
    rightEarLine2.setFill(color_rgb(153,95,96))
    rightEarLine3.setFill(color_rgb(153,95,96))

    rightEarLine1.draw(win)
    rightEarLine2.draw(win)
    rightEarLine3.draw(win)

    #create left and right sideburns, can simply use lines
    #set their fills to different rgb values to create shadow appearance

    thatHairlineTho1 = Line (Point(3.9,6.9),Point(3.96, 6.4))
    thatHairlineTho1.setFill(color_rgb(200,200,200))
    thatHairlineTho1.setWidth(8)
    thatHairlineTho1.draw(win)

    thatHairlineTho2 = Line (Point(6.1,6.9),Point(6.04,6.4))
    thatHairlineTho2.setFill(color_rgb(232,232,232))
    thatHairlineTho2.setWidth(8)
    thatHairlineTho2.draw(win)

    

    #create left eyebrow with polygon class
    #since he has light, thin eyebrows, the entire polygon itself will
    # represent the whole shadow underneath his eyebrow, to simplify
    #things 

    leftEyebrow0 = Point(4.85,6.7)
    leftEyebrow00 = Point(4.78,6.72)
    leftEyebrow01 = Point(4.85,6.55)
    leftEyebrow1 = Point(4.84,6.79)
    leftEyebrow2 = Point(4.78, 6.91)
    leftEyebrow3 = Point(4.72,6.91)
    leftEyebrow4 = Point(4.48, 6.95)
    leftEyebrow5 = Point(4.44, 6.95)
    leftEyebrow6 = Point(4.28,6.83)

    eyebrowShadow = Polygon (leftEyebrow00,leftEyebrow0,leftEyebrow1,
                             leftEyebrow01,leftEyebrow2,leftEyebrow3,
                             leftEyebrow4,leftEyebrow5,leftEyebrow6)
    eyebrowShadow.setFill(color_rgb(173,108,114))
    eyebrowShadow.setOutline(color_rgb(173,108,148))
    eyebrowShadow.draw(win)

    #eyebrow will consist of multiple interconnected lines, since
    # it can't be just one straight segment

    leftEyebrowLine1 = Line(leftEyebrow1,leftEyebrow2)
    leftEyebrowLine1.setWidth(1.5)
    leftEyebrowLine1.setFill(color_rgb(92,56,60))
    leftEyebrowLine1.draw(win)
                             
    leftEyebrowLine2 = Line(leftEyebrow2,leftEyebrow3)
    leftEyebrowLine2.setWidth(1.5)
    leftEyebrowLine2.setFill(color_rgb(92,56,60))
    leftEyebrowLine2.draw(win)
    
    leftEyebrowLine3 = Line(leftEyebrow3,leftEyebrow4)
    leftEyebrowLine3.setWidth(1.3)
    leftEyebrowLine3.setFill(color_rgb(92,56,60))
    leftEyebrowLine3.draw(win)
                             
    leftEyebrowLine4 = Line(leftEyebrow4,leftEyebrow5)
    leftEyebrowLine4.setWidth(1.)
    leftEyebrowLine4.setFill(color_rgb(92,56,60))
    leftEyebrowLine4.draw(win)
                             
    leftEyebrowLine5 = Line(leftEyebrow5,leftEyebrow6)
    leftEyebrowLine5.setWidth(.75)
    leftEyebrowLine5.setFill(color_rgb(92,56,60))
    leftEyebrowLine5.draw(win)

    #create right eyebrow,use same setup as for left eyebrow 
    rightEyebrow1 = Point(5.16,6.79)
    rightEyebrow2 = Point(5.22,6.91)
    rightEyebrow3 = Point(5.28,6.91)
    rightEyebrow4 = Point(5.52,6.95)
    rightEyebrow5 = Point(5.56,6.95)
    rightEyebrow6 = Point(5.72,6.83)

    #use polygon to connect eyebrow points
    rightEyebrowShadow = Polygon(rightEyebrow1,rightEyebrow2,
                                 rightEyebrow3,rightEyebrow4,
                                 rightEyebrow5,rightEyebrow6)
    rightEyebrowShadow.setFill(color_rgb(173,108,114))
    rightEyebrowShadow.setOutline(color_rgb(173,108,114))
    rightEyebrowShadow.draw(win)

    rightEyebrowLine1 = Line(rightEyebrow1,rightEyebrow2)
    rightEyebrowLine1.setWidth(1.5)
    rightEyebrowLine1.setFill(color_rgb(92,56,60))
    rightEyebrowLine1.draw(win)
    
    rightEyebrowLine2 = Line(rightEyebrow2,rightEyebrow3)
    rightEyebrowLine2.setWidth(1.5)
    rightEyebrowLine2.setFill(color_rgb(92,56,60))
    rightEyebrowLine2.draw(win)

    rightEyebrowLine3 = Line(rightEyebrow3,rightEyebrow4)
    rightEyebrowLine3.setWidth(1.5)
    rightEyebrowLine3.setFill(color_rgb(92,56,60))
    rightEyebrowLine3.draw(win)
    
    rightEyebrowLine4 = Line(rightEyebrow4,rightEyebrow5)
    rightEyebrowLine4.setWidth(1.5)
    rightEyebrowLine4.setFill(color_rgb(92,56,60))
    rightEyebrowLine4.draw(win)

    rightEyebrowLine5 = Line(rightEyebrow5,rightEyebrow6)
    rightEyebrowLine5.setWidth(1.5)
    rightEyebrowLine5.setFill(color_rgb(92,56,60))
    rightEyebrowLine5.draw(win)

    #the little wrinkle over the bridge of his nose, use two
    #overlapping circles to create u-shaped crescent
    furrow1 = Circle (Point(4.98,6.97),.18)
    furrow1.setFill(color_rgb(119,80,80))
    furrow1.setOutline(color_rgb(119,80,80))
    furrow1.draw(win)
    furrow2 = furrow1.clone()
    furrow2.move(0,.04)
    furrow2.setFill(color_rgb(245,179,179))
    furrow2.setOutline(color_rgb(245,179,179))
    furrow2.draw(win)

    #use two overlapping circles to create eyebags under eye,
    #draw these BEFORE eye
    
    leftEyebag = Oval (Point(4.4,6.7),Point(4.7,6.6))
    leftEyebag.setFill(color_rgb(119,80,80))
    leftEyebag.setOutline(color_rgb(119,80,78))
    leftEyebag.draw(win)

    bigLeftEyebag = Oval( Point(4.4,6.75),Point(4.7,6.65))
    bigLeftEyebag.setFill(color_rgb(245,179,179))
    bigLeftEyebag.setOutline(color_rgb(245,179,179))
    bigLeftEyebag.draw(win)

    #create left eye with oval, use lines to trim edges
    
    leftEye = Oval(Point(4.42,6.8),Point(4.73,6.67))
    leftEye.setFill("white")
    leftEye.setOutline(color_rgb(92,56,60))
    leftEye.draw(win)
    leftEyeLine1 = Line(Point(4.54,6.8),Point(4.3,6.71))
    leftEyeLine1.setFill(color_rgb(92,56,60))
    leftEyeLine1.draw(win)

    #start with Right Eye here,create eyebags first again
    
    rightEyebag = Oval(Point(5.6,6.7),Point(5.3,6.6))
    rightEyebag.setFill(color_rgb(119,80,80))
    rightEyebag.setOutline(color_rgb(119,80,78))
    rightEyebag.draw(win)

    #bigger one overlaps smaller one to create an elipse
    bigRightEyebag = Oval(Point(5.6,6.75),Point(5.3,6.65))
    bigRightEyebag.setFill(color_rgb(245,179,179))
    bigRightEyebag.setOutline(color_rgb(245,179,179))
    bigRightEyebag.draw(win)

    #create the eyeball,give a dark outline to make it look old,
    # use lines for wrinkles

    rightEye = Oval(Point(5.58,6.8),Point(5.27,6.67))
    rightEye.setFill("white")
    rightEye.setOutline(color_rgb(92,56,60))
    rightEye.move(.05,0)
    rightEye.draw(win)
    rightEyeLine1 = Line(Point(5.46,6.8),Point(5.7,6.71))
    rightEyeLine1.setFill(color_rgb(92,56,60))
    rightEyeLine1.draw(win)

    #create iris using colored oval

    rightIris = Oval(Point(5.35,6.79),Point(5.5,6.7))
    rightIris.setFill("green4")
    rightIris.setOutline(color_rgb(12,82,25))
    rightIris.move(.05,0)
    rightIris.draw(win)

    #create left iris by cloning right one and moving left
    
    leftIris = rightIris.clone()
    leftIris.move(-.85,0)
    leftIris.draw(win)

    #create right puple with oval object
    
    rightPupil = Oval(Point(5.40,6.76),Point(5.46,6.73))
    rightPupil.setFill("black")
    rightPupil.move(.05,0)
    rightPupil.draw(win)

    #create left pupil by cloning right one and moving same distance
    #left as iris
    
    leftPupil = rightPupil.clone()
    leftPupil.move(-.85,0)
    leftPupil.draw(win)

    rightReflection = Oval(Point(5.42,6.77),Point(5.44,6.74))
    rightReflection.setFill("white")
    rightReflection.setOutline("white")
    rightReflection.move(.05,0)
    rightReflection.draw(win)
    
    leftReflection = rightReflection.clone()
    leftReflection.move(-.85,0)
    leftReflection.draw(win)

    #shadow under left eye behind glass lens
    faceShadow = Polygon(Point(4.3,6.6),Point(4.36,6.55),
                         Point(4.5,6.51),Point(4.4,6.4),
                         Point(4.36,6.35),Point(4.32,6.19))
    faceShadow.setFill(color_rgb(214,139,144))
    faceShadow.setOutline(color_rgb(214,139,144))
    faceShadow.draw(win)

    faceShadow2 = Polygon(Point(4.86,6.39),Point(4.75,6.31),
                          Point(4.64,6.27),Point(4.48,6.27),
                          Point(4.38,6.31),Point(4.34,6.31),
                          Point(4.42,6.39),Point(4.52,6.39),
                          Point(4.62,6.39),Point(4.72,6.41),
                          Point(4.84,6.47))
    faceShadow2.setFill(color_rgb(214,139,144))
    faceShadow2.setOutline(color_rgb(214,139,144))
    faceShadow2.draw(win)

    

    #8 total points for left lens polygon

    leftLensSide1 = Point(4.22,6.77)
    leftLensSide2 = Point(4.22,6.53)
    leftLensSide3 = Point(4.82, 6.77)
    leftLensSide4 = Point(4.82,6.53)

    leftLensTop1 = Point(4.3,6.81)
    leftLensTop2 = Point(4.75,6.81)
    leftLensBottom1 = Point(4.3,6.49)
    leftLensBottom2 = Point(4.75,6.49)

    leftLens = Polygon(leftLensTop2, leftLensSide3,leftLensSide4,
                       leftLensBottom2,leftLensBottom1, leftLensSide2,
                       leftLensSide1,leftLensTop1)
    leftLens.draw(win)

   
    #little plastic piece behind the lens on each side of nose
    
    leftBridgePiece = Line(Point(4.81,6.55),Point(4.81,6.72))
    leftBridgePiece.setWidth(3)
    leftBridgePiece.draw(win)

    #8 total points for right lens polygon, 4 here....

    rightLensSide1 = Point(5.78,6.77)
    rightLensSide2 = Point(5.78,6.53)
    rightLensSide3 = Point(5.18,6.77)
    rightLensSide4 = Point(5.18,6.53)

    
    #create the little plastic piece on the side of nose for the other
    # side
    
    rightBridgePiece = Line(Point(5.19,6.55),Point(5.19,6.72))
    rightBridgePiece.setWidth(3)
    rightBridgePiece.draw(win)

    # other 4 points for right lens polygon
    
    rightLensTop1 = Point(5.7,6.81)
    rightLensTop2 = Point(5.25,6.81)
    rightLensBottom1 = Point(5.7, 6.49)
    rightLensBottom2 = Point(5.25,6.49)

    #use two circles to create the bridge across nose
    
    bridge = Circle(Point(5,6.45),.2)
    bridge.draw(win)
    bridge2 = bridge.clone()
    bridge2.move(0,.06)
    bridge2.draw(win)

    #erase the remaining bottom portion of two circles with skin-colored
    #rectangle

    eraseExtraBridge = Rectangle(Point(4.8,6.488),Point(5.5,6))
    eraseExtraBridge.setFill(color_rgb(245,179,179))
    eraseExtraBridge.setOutline(color_rgb(245,179,179))
    eraseExtraBridge.draw(win)

    #create the right lens of the glasses using points established
    #before with Polygon 
    
    rightLens = Polygon(rightLensTop2,rightLensTop1,rightLensSide1,
                        rightLensSide2,rightLensBottom1,
                        rightLensBottom2,rightLensSide4,
                        rightLensSide3)
    rightLens.draw(win)

 
    #draw shadow under nose using Circle with fill that is darker than
    #regular skin tone
    underNoseShadow = Circle(Point(5,6.37),.1)
    underNoseShadow.setFill(color_rgb(180,100,100))
    underNoseShadow.setOutline(color_rgb(180,100,100))
    underNoseShadow.draw(win)

    #this shadow will be slightly lighter than the previous one
    underNoseShadow2 = Circle(Point(5,6.388),.1)
    underNoseShadow2.setFill(color_rgb(245,179,179))
    underNoseShadow2.setOutline(color_rgb(245,179,179))
    underNoseShadow2.draw(win)

    #make left side of face look darker by adding shadow to left of nose

    leftNoseShadow1 = Point(4.86,6.54)
    leftNoseShadow2 = Point(4.8,6.41)
    leftNoseShadow3 = Point(4.8, 6.3)
    leftNoseShadow4 = Point(4.96,6.3)

    leftNoseShadow = Polygon(leftNoseShadow1,leftNoseShadow2,
                             leftNoseShadow3,leftNoseShadow4)
    leftNoseShadow.setFill(color_rgb(214,139,144))
    leftNoseShadow.setOutline(color_rgb(214,139,144))
    leftNoseShadow.draw(win)

    #create nostrils using oval objects

    leftNostril = Oval(Point(4.8,6.35),Point(4.9,6.3))
    leftNostril.setFill(color_rgb(77,34,34))
    leftNostril.setOutline(color_rgb(77,34,34))
    leftNostril.draw(win)

    #clone the left nostril, move clone to right 

    rightNostril = leftNostril.clone()
    rightNostril.move(.3,0)
    rightNostril.draw(win)

    #give nose some depth by adding a highlight with Polygon object
    noseHighlightLeft = Polygon(Point(4.88,6.43),Point(4.84,6.37),
                                Point(4.9,6.37))
    noseHighlightLeft.setFill(color_rgb(245,179,179))
    noseHighlightLeft.setOutline(color_rgb(245,179,179))
    noseHighlightLeft.draw(win)

    #septum shadow, use collection of points, connect with Polygon class
    shadowUnderNose = Polygon(Point(4.94,6.23),Point(5,6.21),
                              Point(5.11,6.23),Point(5.13,6.15),
                              Point(4.94,6.17))
    shadowUnderNose.setFill(color_rgb(214,139,144))
    shadowUnderNose.setOutline(color_rgb(214,139,144))
    shadowUnderNose.draw(win)
    

    #smile wrinkles, left and right, using polygons

    smileWrinkleLeft = Polygon(Point(4.74,6.35),Point(4.6,6.19),
                               Point(4.54,6.09),Point(4.53,5.89),
                               Point(4.3,5.71),Point(4.57,5.69),
                               Point(4.59,5.83),Point(4.53,5.83),
                               Point(4.59,6.09),Point(4.68,6.21),
                               Point(4.75,6.3))
    smileWrinkleLeft.setFill(color_rgb(214,139,144))
    smileWrinkleLeft.setOutline(color_rgb(214,139,144))
    smileWrinkleLeft.draw(win)

    smileWrinkleRight = Polygon(Point(5.26,6.35),Point(5.4,6.19),
                                Point(5.46,6.09),Point(5.47,5.89),
                                Point(5.5,5.71),Point(5.43,5.54),
                                Point(5.38,5.83),Point(5.47,5.83),
                                Point(5.41,6.09),Point(5.32,6.21),
                                Point(5.25,6.4))
    smileWrinkleRight.setFill(color_rgb(214,139,144))
    smileWrinkleRight.setOutline(color_rgb(214,139,144))
    smileWrinkleRight.draw(win)

    #use oval overlapping with mouth to create bottom lip
    bottomLip = Oval(Point(4.73,5.73),Point(5.35,5.49))
    bottomLip.setFill(color_rgb(255,207,207))
    bottomLip.setOutline(color_rgb(255,215,215))
    bottomLip.draw(win)

    #use collection of points to create empty, black space for mouth
    
    mouth = Polygon(Point(4.6,5.83),Point(4.86,5.87),Point(5.21,5.87),
                   Point(5.39,5.84),Point(5.37,5.73),Point(5.28,5.6),
                   Point(5.05,5.54),Point(5.02,5.54),Point(4.98,5.54),
                   Point(4.86,5.58),Point(4.78,5.59),Point(4.67,5.69),
                   Point(4.62,5.74))
    mouth.setFill("black")
    mouth.setOutline(color_rgb(252,202,202))
    mouth.draw(win)

    #use a collection of points to create one polygon for bottom row of
    #teeth
    teeth = Polygon(Point(4.74,5.61),Point(4.74,5.69),Point(4.8,5.69),
                    Point(4.92,5.65),Point(5.03,5.63),Point(5.13,5.65),
                    Point(5.23,5.69),Point(5.25,5.69),Point(5.27,5.59),
                    Point(5.13,5.51),Point(5,5.49),Point(4.9,5.51))

    #make teeth light grey, draw them                  
    teeth.setFill(color_rgb(222,222,222))
    teeth.setOutline(color_rgb(170,170,170))
    teeth.draw(win)

    #shadow on left side of bottom row of teeth
    teethShadow1 = Line (Point(4.72,5.69),Point(4.82,5.62))
    teethShadow1.setFill(color_rgb(94,92,79))
    teethShadow1.setWidth(3)
    teethShadow1.draw(win)
    
    #shadow on right side of bottom row of teeth
    teethShadow2 = Line (Point(5.28,5.69),Point(5.18,5.58))
    teethShadow2.setFill(color_rgb(94,92,79))
    teethShadow2.setWidth(3)
    teethShadow2.draw(win)

    #add some more depth to his face by superimposing a darker-colored
    #polygon

    rightCheekShadow = Polygon(Point(5.9,6.57),Point(5.87,6.19),
                               Point(5.85,5.81),Point(5.85,5.47),
                               Point(5.87,5.43),Point(6,6),
                               Point(6,6.27),Point(5.95,6.73))
    rightCheekShadow.setFill(color_rgb(200,122,130))
    rightCheekShadow.setOutline(color_rgb(214,139,144))
    rightCheekShadow.draw(win)

    rightCheekShadow2 = Polygon(Point(5.57,5.09),
                                Point(5.63,4.98),Point(5.69,5.19),
                                Point(5.73,5.57),Point(5.73,5.95),
                                Point(5.67, 6.17),Point(5.59, 6.11),
                                Point(5.67,5.97),Point(5.67, 5.77),
                                Point(5.61, 5.45), Point( 5.55,5.17),
                                Point(5.49,4.98),Point(5.43,4.82))
    rightCheekShadow2.setFill(color_rgb(214,139,144))
    rightCheekShadow2.setOutline(color_rgb(214,139,144))
    rightCheekShadow2.draw(win)

    #shadow just above chin, under bottom lip
    
    chinShadow1 = Oval (Point(4.74,5.47),Point(5.33,5.31))
    
    chinShadow1.setFill(color_rgb(214,139,144))
    chinShadow1.setOutline(color_rgb(214,139,144))
    chinShadow1.draw(win)

    chinShadow2 = Oval (Point(4.8,5.42),Point(5.27,5.35))
    chinShadow2.setFill(color_rgb(200,120,120))
    chinShadow2.setOutline(color_rgb(200,120,120))
    chinShadow2.draw(win)

    #highlight on the chin, give it shape

    chinHighlight2 = Oval(Point(4.85,5.2),Point(5.25,4.95))
    chinHighlight2.setFill(color_rgb(255,200,200))
    chinHighlight2.setOutline(color_rgb(255,200,200))
    chinHighlight2.draw(win)

    chinHighlight = Oval (Point(4.95,5.17),Point(5.15,5))
    chinHighlight.setFill(color_rgb(255,224,225))
    chinHighlight.setOutline(color_rgb(255,225,225))
    chinHighlight.draw(win)

    #make neck thinner by superimposing hot pink polygon along edge
    
    eraseNeck = Polygon(Point(3.62,5.73),Point(4.1,5.17),
                        Point(4.02,5.51), Point(3.96,5.75))
    eraseNeck.setFill(hotPink)
    eraseNeck.setOutline(hotPink)
    eraseNeck.draw(win)

    #right glasses arm, must appear in front of face polygons
    rightGlassArm1 = Line (rightLensSide1, Point(6,6.72))
    rightGlassArm1.setWidth(3)
    rightGlassArm1.draw(win)
    rightGlassArm2 = Line (Point(6,6.72),Point(6.15, 6.61))
    rightGlassArm2.setWidth(2)
    rightGlassArm2.draw(win)

    #left glasses arm, must appear in front of face polygons

    leftGlassArm1 = Line (leftLensSide1, Point(4,6.72))
    leftGlassArm1.setWidth(3)
    leftGlassArm1.draw(win)
    leftGlassArm2 = Line (Point(4,6.72),Point(3.85, 6.61))
    leftGlassArm2.setWidth(2)
    leftGlassArm2.draw(win)

    
    #add another layer to coat, make it taller

    coat2 = Polygon(Point(3.3,4.8),Point(3.74,5.15),
                    Point(3.8,5.3),Point(3.86,5.47),
                    Point(3.94,5.51),Point(4.02,5.57),
                    Point(4.12,5.13),Point(4.06,5),Point(3.44,4.6))
    coat2.setFill("black")
    coat2.draw(win)

    coat3 = Polygon(Point(6.7,4.8),Point(6.26,5.15),Point(6.2,5.3),
                    Point(6.14,5.47),Point(6.06,5.51),Point(5.98,5.57),
                    Point(5.88,5.13),Point(5.94,5),Point(6.56,4.6))
    coat3.setFill("black")
    coat3.draw(win)


    #create 2 arrows (4 points) to move within for loops

    arrowPt1 = Point(9.5,.5)
    arrowPt2 = Point(10.5,-2.5)
    arrow = Line (arrowPt1,arrowPt2)
    arrow.setArrow("first")
    currentWidth = 27
    arrow.setWidth(currentWidth)
    arrow.draw(win)

    arrowPt3 = Point(.5,.5)
    arrowPt4 = Point(-.5,-2.5)
    arrow2 = Line(arrowPt3,arrowPt4)
    arrow2.setArrow ("first")
    arrow2.setWidth(currentWidth)
    arrow2.draw(win)

    #create blue blood droplet(democrat), clone it so there are two
    
    dropRadius  = .1
    blueBlood = Circle(Point(3.14,8.5),dropRadius)
    blueBlood.setFill("blue")
    blueBlood.setOutline("white")

    blueBlood2 = blueBlood.clone()
    blueBlood2.move(3.72,0)

    #create hotpink circle to cover arrow head upon contact, make it
    #look like arrow has actually pierced the heart
    
    punctureWoundA = Circle(Point(3.14,8.5),.2)
    punctureWoundA.setFill(hotPink)
    punctureWoundA.setOutline(hotPink)
    punctureWoundB =  Circle(Point(3.13, 8.49),.2)
    punctureWoundB.setFill("red4")
    punctureWoundB.setOutline("red4")


    punctureWound2A = punctureWoundA.clone()
    punctureWound2A.move(3.72,0)
    punctureWound2B = punctureWoundB.clone()
    punctureWound2B.move(3.74,0)
    
    
    
    

    #once bernie is drawn, instructions are given to user
    
    clickToShoot = Text(Point(5,1.5),"Click to shoot heart")
    clickToShoot.setFill("black")
    clickToShoot.setSize(14)
    clickToShoot.setFace("arial")
    clickToShoot.draw(win)

    #wait for user to click on window
    
    win.getMouse()

    #arrow begins moving toward its destination
    #width decreases as arrow moves to make it look as if it's moving
    #away 
    for i in range (8):
        currentWidth-=3
        arrow.move(-.33,1)
        arrow.setWidth(currentWidth)
        time.sleep(.05)
    #make heart look pierced with puncture wound shapes
        
    punctureWound2B.draw(win)
    punctureWound2A.draw(win)

    #wait half a second for blood to drop

    time.sleep(.5)
    
    #draw blue drop of blood, drops downward
    
    blueBlood2.draw(win)
    
    for i in range(7):
        blueBlood2.move(0,-1)
        time.sleep(.2)
    
    #wait for second click to launch another arrow
        
    win.getMouse()
    
    #initialize current arrow width again to 27
    currentWidth=27

    #width decreases as arrow moves to make it look as if it's moving
    #away 
    for i in range (8):
        currentWidth -= 3
        arrow2.move(.33,1)
        arrow2.setWidth(currentWidth)
        time.sleep(.05)
    #make heart look as if it's been pierced with puncturewound shapes
    punctureWoundB.draw(win)
    punctureWoundA.draw(win)

    #erase instructions to clear space for new text
    clickToShoot.undraw()
    
    
    #wait half a second for blood to drop
        
    time.sleep(.5)
    
    #draw blue blood drop, move it downward
    blueBlood.draw(win)
    for i in range(7):
        blueBlood.move(0,-1)
        time.sleep(.2)

    #create two more arrows, use them to accent the text at the bottom
    #they move from right to left, above and below the text
        
    arrow3 = Line(Point(10,1.66),Point(20,1.66))
    arrow3.setArrow("first")
    arrow3.setWidth(3)
    arrow3.draw(win)
    
    arrow4 = Line(Point(10,1.34),Point(20,1.34))
    arrow4.setArrow("first")
    arrow4.setWidth(3)
    arrow4.draw(win)

    #move arrows left, move each drop outward 
    for i in range (10):
        arrow3.move(-1,0)
        arrow4.move(-1,0)
        blueBlood.move(1,0)
        blueBlood2.move(-1,0)
        
    # create cute valentine-y text to make the user feel special
    # set the text to a unique style/face/size
    textCtr = Point(ptA.getX(), 1.5)
    feelTheBern = Text(textCtr, "My heart Berns for you.") 
    feelTheBern.setFace("arial")
    feelTheBern.setSize(14)
    feelTheBern.setStyle("bold")
    feelTheBern.draw(win)


    #wait 5 seconds, undraw valentine text
    
    time.sleep(5)
    feelTheBern.undraw()
    time.sleep(1/4)

    #instruct user on how to close the window
    msg = "Click anywhere to close this political valentine."
    clickToClose = Text(textCtr,msg)
    clickToClose.setFace("arial")
    clickToClose.setSize(14)
    clickToClose.setStyle("bold")
    clickToClose.draw(win)

    win.getMouse()
    win.close()

    
        
valentineGreeting()


