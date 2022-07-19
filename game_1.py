from tkinter import *
from random import randrange as rnd, choice
import time

window = Tk()
window.geometry('800x600')
window.title("Поймай шарик!")
c = Canvas(window,width=800,height=600,bg='yellow')
c.pack()
colors = ['pink','violet','brown','red','green','cyan','blue','magenta','black']
x = 0
y = 0
r = 0
points = 0
miss = 0
zero = 0


def new_ball():

    global x, y, r, zero, res, points
    c.delete(ALL)
    res = c.create_text(300,20,text="Попаданий :" + str(points)+ " очков"
                               +'/'+"Промахи :"+str(miss)+" раз"+'/'+
                               "Упущено :"+str(zero)+" шаров", font = 'Arial 15')
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(20,50)
    target = c.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    if points < 20:
        window.after(rnd(500, 800),new_ball)
    else:
        c.delete(ALL)
        res = c.create_text(350,250,text="  Вы выйграли! Вы набрали: " + str(points) + "  балла(ов)", font = 'Arial 20')
    zero+=1


def click(event):

    global points, miss, zero, res, xz
    if abs(x-event.x) < r/2 and abs(y-event.y)<r/2:
        points += 2
        zero-=1
    elif abs(x-event.x) < r and abs(y-event.y)<r:
        points += 1
        zero-=1
    else:
        miss += 1
    c.delete(ALL)
    res = c.create_text(300,20,text="Попаданий :" + str(points)+ " очков"
                               +'/'+"Промахи :"+str(miss)+" раз"+'/'+
                               "Упущено :"+str(zero)+" шаров", font = 'Arial 15')
window.after(800,new_ball)
c.bind('<Button-1>',click)
mainloop()