from tkinter import *

class PythonCinema:
    def __init__(self):
        window = Tk()
        window.title("PYTHON CINEMA Main") 

        menubar = Menu(window) #메뉴바 생성
        window.config(menu = menubar) # 메뉴바 표시

        exitmenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "나가기",menu = exitmenu)
        exitmenu.add_command(label = "종료", command = window.destroy)

        pycinema = PhotoImage(file = "python_cinema.png") #표지이미지 삽입
        Button(window,image = pycinema, command = self.movie).grid(row = 1, column = 1) #표지이미지 화면 출력

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

    def movie(self):
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
        Button(top,image = movie, command = self.open_2018).grid(row = 1, column = 1)
        Button(top,image = good, command = self.open_select).grid(row = 1, column = 2)
        Label(top, text = "2018 개봉영화",font=35, bg="#b3ffff",width=25).grid(row = 2, column = 1)
        Label(top, text = "추천영화",font=35, bg="#b3ffff",width=25).grid(row = 2, column = 2)
        Label(top, text = "2018년에 개봉한 ",width=25).grid(row = 3,column = 1)
        Label(top, text = "영화에 대한 정보입니다. ",width=25).grid(row = 4,column = 1)
        Label(top, text = "관리자가 추천하는",width=25).grid(row = 3,column = 2)
        Label(top, text = "영화에 대한 정보입니다.",width=25).grid(row = 4,column = 2)

        top.mainloop()
            
    def open_2018(self):
        
        movie_2018 = Toplevel()
        movie_2018.title("2018 개봉영화")
        movie_2018.geometry("840x400")

        menubar = Menu(movie_2018) #메뉴바 생성
        movie_2018.config(menu = menubar) # 메뉴바 표시
        movemenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "이동",menu = movemenu)
        movemenu.add_command(label = "영화구분", command = movie_2018.destroy)

        self.movie_list = []
        for i in range(1,4):
            self.movie_list.append(PhotoImage(file = "image/movie_2018/"+str(i)+".png"))
            
        self.Radio_list = []
        self.v1 = IntVar()
        for i in range(3):
            self.Radio_list.append(Radiobutton(movie_2018, image = self.movie_list[i],variable = self.v1, value = i, command = self.myRb_2018))
            self.Radio_list[i].pack(side=LEFT)

        movie_2018.mainloop()

    def open_select(self):
        movie_select = Toplevel()
        movie_select.title("관리자 추천영화")
        movie_select.geometry("840x400")

        menubar = Menu(movie_select) #메뉴바 생성
        movie_select.config(menu = menubar) # 메뉴바 표시
        movemenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "이동",menu = movemenu)
        movemenu.add_command(label = "영화구분", command = movie_select.destroy)

        self.movie_list = []
        for i in range(1,4):
            self.movie_list.append(PhotoImage(file = "image/movie_select/"+str(i)+".png"))
            
        self.Radio_list = []
        self.v1 = IntVar()
        for i in range(3):
            self.Radio_list.append(Radiobutton(movie_select, image = self.movie_list[i],variable = self.v1, value = i, command = self.myRb_select))
            self.Radio_list[i].pack(side=LEFT)

        movie_select.mainloop()

    def myRb_2018(self):
        if self.v1.get() == 0:
            fr=open('fengshui.txt','r')
            read=fr.read()
            print(read)
            fr.close()
            
        elif self.v1.get() ==1:
            fr=open('avengers.txt','r')
            read=fr.read()
            print(read)
            fr.close()
            
        elif self.v1.get() ==2:
            fr=open('incredibles2.txt','r')
            read=fr.read()
            print(read)
            fr.close()

    def myRb_select(self):
        if self.v1.get() == 0:
            fr=open('bewithyou.txt','r')
            read=fr.read()
            print(read)
            fr.close()
            
        elif self.v1.get() ==1:
            fr=open('interstellar.txt','r')
            read=fr.read()
            print(read)
            fr.close()
            
        elif self.v1.get() ==2:
            fr=open('littleforest.txt','r')
            read=fr.read()
            print(read)
            fr.close()

PythonCinema()

        
    
