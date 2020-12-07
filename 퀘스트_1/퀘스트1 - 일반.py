from tkinter import *

def movie():
    top = Toplevel()
    top.title("PYTHON CINEMA Start")
    top.geometry("510x320")
        
    menubar = Menu(top) #메뉴바 생성
    top.config(menu = menubar) # 메뉴바 표시
    movemenu = Menu(menubar, tearoff = 0)
    reservmenu = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = "이동",menu = movemenu)
    movemenu.add_command(label = "메인", command = top.destroy)
        
    movie = PhotoImage(file = "movie.png")
    good = PhotoImage(file = "good.png") 
    Button(top,image = movie, command = open_2018).grid(row = 1, column = 1)
    Button(top,image = good, command = open_select).grid(row = 1, column = 2)
    Label(top, text = "2018 개봉영화",font=35, bg="#b3ffff",width=25).grid(row = 2, column = 1)
    Label(top, text = "추천영화",font=35, bg="#b3ffff",width=25).grid(row = 2, column = 2)
    Label(top, text = "2018년에 개봉한 ",width=25).grid(row = 3,column = 1)
    Label(top, text = "영화에 대한 정보입니다. ",width=25).grid(row = 4,column = 1)
    Label(top, text = "관리자가 추천하는",width=25).grid(row = 3,column = 2)
    Label(top, text = "영화에 대한 정보입니다.",width=25).grid(row = 4,column = 2)

    top.mainloop()

def open_2018():
        
    movie_2018 = Toplevel()
    movie_2018.title("2018 개봉영화")
    movie_2018.geometry("930x400")

    menubar = Menu(movie_2018) #메뉴바 생성
    movie_2018.config(menu = menubar) # 메뉴바 표시
    movemenu = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = "이동",menu = movemenu)
    movemenu.add_command(label = "영화구분", command = movie_2018.destroy)

    movie_list = []
    for i in range(1,4):
        movie_list.append(PhotoImage(file = "image/movie_2018/"+str(i)+".png"))

    v1 = IntVar()
    rb1 = Radiobutton(movie_2018, image = movie_list[0],variable = v1, value = 0)
    rb2 = Radiobutton(movie_2018, image = movie_list[1],variable = v1, value = 1)
    rb3 = Radiobutton(movie_2018, image = movie_list[2],variable = v1, value = 2)
    bt = Button(movie_2018, text = "영화 정보 보기", command = myRb_2018(v1.get()))

    rb1.pack(side=LEFT)
    rb2.pack(side=LEFT)
    rb3.pack(side=LEFT)
    bt.pack(side =LEFT)

    movie_2018.mainloop()


def open_select():
    movie_select = Toplevel()
    movie_select.title("관리자 추천영화")
    movie_select.geometry("840x400")

    menubar = Menu(movie_select) #메뉴바 생성
    movie_select.config(menu = menubar) # 메뉴바 표시
    movemenu = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = "이동",menu = movemenu)
    movemenu.add_command(label = "영화구분", command = movie_select.destroy)

    movie_list = []
    for i in range(1,4):
        movie_list.append(PhotoImage(file = "image/movie_select/"+str(i)+".png"))

    v1 = IntVar()
    rb1 = Radiobutton(movie_select, image = movie_list[0],variable = v1, value = 0, command = myRb_select(v1.get()))
    rb2 = Radiobutton(movie_select, image = movie_list[1],variable = v1, value = 1, command = myRb_select(v1.get()))
    rb3 = Radiobutton(movie_select, image = movie_list[2],variable = v1, value = 2, command = myRb_select(v1.get()))

    rb1.pack(side=LEFT)
    rb2.pack(side=LEFT)
    rb3.pack(side=LEFT)

    movie_select.mainloop()

def myRb_2018(rv):
    if rv == 0:
        fr=open('fengshui.txt','r')
        read=fr.read()
        print(read)
        print(rv)
        fr.close()            
    elif rv ==1:
        fr=open('avengers.txt','r')
        read=fr.read()
        print(read)
        fr.close()            
    elif rv ==2:
        fr=open('incredibles2.txt','r')
        read=fr.read()
        print(read)
        fr.close()

def myRb_select(v1):
    if v1 == 0:
        fr=open('bewithyou.txt','r')
        read=fr.read()
        print(read)
        fr.close()
            
    elif v1 ==1:
        fr=open('interstellar.txt','r')
        read=fr.read()
        print(read)
        fr.close()
            
    elif v1 ==2:
        fr=open('littleforest.txt','r')
        read=fr.read()
        print(read)
        fr.close()
            
window = Tk()
window.title("PYTHON CINEMA Main") 

menubar = Menu(window) #메뉴바 생성
window.config(menu = menubar) # 메뉴바 표시

exitmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "나가기",menu = exitmenu)
exitmenu.add_command(label = "종료", command = window.destroy)

pycinema = PhotoImage(file = "python_cinema.png") #표지이미지 삽입
Button(window,image = pycinema, command = movie).grid(row = 1, column = 1) #표지이미지 화면 출력

canvas = Canvas(window, bg = "#ff8", width = 500, height = 50)
canvas.grid(row=2,column =1)

x = 150 
width = 250
canvas.create_text(x, 30, text = "PYTHON CINEMA를 눌러 영화를 확인하세요!", tags = "text") 
dx = 3 

while True:
    canvas.move("text",dx, 0) 
    canvas.after(100) 
    canvas.update() 
    if x < width :
        x += dx 
    else : 
        x = 150 
        canvas.delete ("text") 
        canvas.create_text(x,30,text="PYTHON CINEMA를 눌러 영화를 확인하세요!",tags="text")
        
window.mainloop()

        
    
