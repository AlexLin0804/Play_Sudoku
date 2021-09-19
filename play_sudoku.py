#################################################
# hw7.py
#
# Your Name:
# Your Andrew ID:
#################################################

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

import cs112_m20_unit7_linter
from cmu_112_graphics import *
import math

####################################
# Add your hw5 and hw6 functions here!
# You may need to modify them a bit.
# Those are: isLegalSudoku and
# drawSudokuBoard
# OR
# getValidChessMoves and
# drawChessBoard
####################################



####################################
# customize these functions
####################################



def drawBoard(canvas, app):


    num_small_sqaure = int(math.sqrt(app.num))

    # without bold 
    for i in range(app.num):
        for j in range(app.num):
            canvas.create_rectangle(app.margin + i*app.small_side, 
                                    app.margin + j*app.small_side, 
                                    app.margin + (i+1)*app.small_side, 
                                    app.margin + (j+1)*app.small_side)

    #add bold 
    for i in range(num_small_sqaure):
        for j in range(num_small_sqaure):
            canvas.create_rectangle(app.margin + i*app.small_side*3, 
                                    app.margin + j*app.small_side*3, 
                                    app.margin + (i+1)*app.small_side*3, 
                                    app.margin + (j+1)*app.small_side*3,
                                    width = 5)



def appStarted(app):

    # Basic components 
    app.board = [
                  [ 1, 2, 3, 4, 5, 6, 7, 8, 9],
                  [ 5,'', 8, 1, 3, 9, 6, 2, 4],
                  [ 4, 9, 6, 8, 7, 2, 1, 5, 3],
                  [ 9, 5, 2, 3, 8, 1, 4, 6, 7],
                  [ 6, 4, 1, 2, 9, 7, 8, 3, 5],
                  [ 3, 8, 7, 5, 6, 4,'', 9, 1],
                  [ 7, 1, 9, 6, 2, 3, 5, 4, 8],
                  [ 8, 6, 4, 9, 1, 5, 3, 7, 2],
                  [ 2, 3, 5, 7, 4, 8, 9, 1, 6]
                ]

    app.cannot_delete = [
                  [ 1, 2, 3, 4, 5, 6, 7, 8, 9],
                  [ 5, 0, 8, 1, 3, 9, 6, 2, 4],
                  [ 4, 9, 6, 8, 7, 2, 1, 5, 3],
                  [ 9, 5, 2, 3, 8, 1, 4, 6, 7],
                  [ 6, 4, 1, 2, 9, 7, 8, 3, 5],
                  [ 3, 8, 7, 5, 6, 4, 0, 9, 1],
                  [ 7, 1, 9, 6, 2, 3, 5, 4, 8],
                  [ 8, 6, 4, 9, 1, 5, 3, 7, 2],
                  [ 2, 3, 5, 7, 4, 8, 9, 1, 6]
                ]

    app.answer = [
                  [ 1, 2, 3, 4, 5, 6, 7, 8, 9],
                  [ 5, 7, 8, 1, 3, 9, 6, 2, 4],
                  [ 4, 9, 6, 8, 7, 2, 1, 5, 3],
                  [ 9, 5, 2, 3, 8, 1, 4, 6, 7],
                  [ 6, 4, 1, 2, 9, 7, 8, 3, 5],
                  [ 3, 8, 7, 5, 6, 4, 2, 9, 1],
                  [ 7, 1, 9, 6, 2, 3, 5, 4, 8],
                  [ 8, 6, 4, 9, 1, 5, 3, 7, 2],
                  [ 2, 3, 5, 7, 4, 8, 9, 1, 6]
                ]

                

    app.margin = 20
    app.num = 9
    app.side = app.width - 2*app.margin
    app.small_side = app.side / app.num

    #starting coordinate for the highlighted sqaure
    app.x1 = app.margin 
    app.y1 = app.margin 
    app.x2 = app.margin + app.small_side 
    app.y2 = app.margin + app.small_side

    #current position
    app.i = 0 # col
    app.j = 0 # row 

    # word 
    app.word_gap = app.small_side / 2


def mousePressed(app, event):
    r,c = xy_to_rc(app, event.x, event.y)
    app.x1 = app.margin + r*app.small_side
    app.y1 = app.margin + c*app.small_side
    app.x2 = app.margin + (r+1)*app.small_side 
    app.y2 = app.margin + (c+1)*app.small_side


def xy_to_rc(app, x,y):

    r = (x - app.margin) // app.small_side
    c = (y - app.margin) // app.small_side

    return r, c
    

def keyPressed(app, event):

    #fill
    if (app.board[app.j][app.i] == ''):
        if(event.key in '123456789' and not event.key in cannot_fill(app)):
            app.board[app.j][app.i] = int(event.key)

    # delete
    if (event.key == 'Delete'):
        if (not app.cannot_delete[app.j][app.i]):
            app.board[app.j][app.i] = ''

    # change position 
    if (event.key == 'Left'):  
        if (app.x1 - app.small_side < app.margin - 1):
            app.x1 = app.margin + (app.num - 1)*app.small_side
            app.x2 = app.margin + app.num*app.small_side
            app.i = 8
           
        else:
            app.x1 -= app.small_side
            app.x2 -= app.small_side
            app.i -= 1
             
    elif (event.key == 'Right'): 
        if (app.x1 + app.small_side >= app.width - app.margin):
            app.x1 = app.margin
            app.x2 = app.margin + app.small_side
            app.i = 0
           
        else:
            app.x1 += app.small_side
            app.x2 += app.small_side 
            app.i += 1
            
    elif (event.key == 'Up'): 
        if (app.y1 - app.small_side < app.margin - 1):
            app.y1 = app.margin + (app.num - 1)*app.small_side
            app.y2 = app.margin + app.num*app.small_side
            app.j = 8
        else:
            app.y1 -= app.small_side
            app.y2 -= app.small_side
            app.j -= 1
           
    
    elif (event.key == 'Down'): 
        if (app.y1 + app.small_side >= app.height - app.margin):
            app.y1 = app.margin
            app.y2 = app.margin + app.small_side
            app.j = 0
        else:
            app.y1 += app.small_side
            app.y2 += app.small_side
            app.j += 1
    



def redrawAll(app, canvas):


    #highlighted
    canvas.create_rectangle(app.x1,app.y1,app.x2,app.y2,fill = 'yellow')

    # board
    drawBoard(canvas, app)

    #numbers
    for i in range(app.num):
        for j in range(app.num):
            if(app.cannot_delete[j][i]):
                canvas.create_text(app.margin + (i)*app.small_side 
                                    + app.word_gap, 
                                   app.margin + (j)*app.small_side 
                                    + app.word_gap,
                                   text = app.board[j][i],
                                   font = "Arial 25",
                                   fill = 'darkblue')
            else:
                canvas.create_text(app.margin + (i)*app.small_side 
                                    + app.word_gap, 
                                   app.margin + (j)*app.small_side 
                                    + app.word_gap,
                                   text = app.board[j][i],
                                   font = "Arial 25",
                                   fill = 'black')

    #win 
    if(win(app)):
        canvas.create_text(app.width/2, app.height/2,
                           text = "You Win!",
                           font = 'Arial 100 bold',
                           fill = 'green',)


def win(app):
    for i in range(app.num):
        for j in range(app.num):
            if (app.answer[j][i] != app.board[j][i]): 
                return False
    return True

def cannot_fill(app): 
    cannot_set = set()
    for i in range(app.num):

        cannot_set.add(str(app.board[app.j][i]))
        cannot_set.add(str(app.board[i][app.i]))

    return cannot_set







####################################
# Main
####################################

def main():
    #cs112_m20_unit7_linter.lint()
    runApp(width=600, height=600)

if __name__ == "__main__":
    main()
