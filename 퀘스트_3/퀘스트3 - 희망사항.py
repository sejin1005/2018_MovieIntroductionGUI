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
        menubar.add_cascade(label = "보기",menu = reservmenu)
        movemenu.add_command(label = "메인", command = top.destroy)
        reservmenu.add_command(label = "예약내역", command = self.reservation_text)
        
        movie = PhotoImage(file = "movie.png")
        good = PhotoImage(file = "good.png") 
        Button(top,image = movie, command = self.open_2018).grid(row = 1, column = 1)
        Button(top,image = good, command = self.open_select).grid(row = 1, column = 2)
        Label(top, text = "2018 개봉영화",font=35, bg="#b3ffff",width=25).grid(row = 2, column = 1)
        Label(top, text = "추천영화",font=35, bg="#b3ffff",width=25).grid(row = 2, column = 2)
        Label(top, text = "영화에 대한 정보, ",width=25).grid(row = 3,column = 1)
        Label(top, text = "포토이미지를 제공합니다. ",width=25).grid(row = 4,column = 1)
        Label(top, text = "관리자가 추천하는",width=25).grid(row = 3,column = 2)
        Label(top, text = "영화에 대한 정보입니다.",width=25).grid(row = 4,column = 2)
        
        top.mainloop()

    def reservation_text(self):
        
        reserv = Toplevel()
        reserv.title("예약 내역 조회")
        reserv.geometry("300x400")

        menubar = Menu(reserv) #메뉴바 생성
        reserv.config(menu = menubar) # 메뉴바 표시
        movemenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "이동",menu = movemenu)
        movemenu.add_command(label = "영화구분", command = reserv.destroy)
   
        frame1 = Frame(reserv)
        reservImage = PhotoImage(file = "reservation.png")
        Label(frame1,image = reservImage).grid(row = 1, column = 1)
        
        frame2 = Frame(reserv)
        scrollbar = Scrollbar(frame2)
        scrollbar.pack(side="right",fill="y")
        text = Text(frame2, width = 40, height = 10, yscrollcommand = scrollbar.set)
        text.pack(side="left")
        scrollbar["command"] = text.yview
        #f=open('reservation.txt','r')   # 윈도우창에 읽어오는 방법을 모르겠습니다.
        #a=f.read()
        #text.insert(a)
        #print(a)
        #f.close()
        
        frame1.pack()
        frame2.pack()
        reserv.mainloop()
            
    def open_2018(self):
        
        movie_2018 = Toplevel()
        movie_2018.title("2018 개봉영화")
        movie_2018.geometry("840x700")

        menubar = Menu(movie_2018) #메뉴바 생성
        movie_2018.config(menu = menubar) # 메뉴바 표시
        movemenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "이동",menu = movemenu)
        movemenu.add_command(label = "영화구분", command = movie_2018.destroy)

        frame1 = Frame(movie_2018)

        self.movie_list = []
        for i in range(1,4):
            self.movie_list.append(PhotoImage(file = "image/movie_2018/"+str(i)+".png"))
            
        self.Radio_list = []
        self.v1 = IntVar()
        for i in range(3):
            self.Radio_list.append(Radiobutton(frame1, image = self.movie_list[i],variable = self.v1, value = i, command = self.myRb_2018))
            self.Radio_list[i].pack(side=LEFT)
        
        frame2 = Frame(movie_2018)

        self.bagic_list = []
        self.fengshui_list = []
        self.avengers_list = []
        self.incredibles2_list = []
        
        for i in range(1,5):
            self.bagic_list.append(PhotoImage(file = "image/bagics/"+str(i)+".png"))
            self.fengshui_list.append(PhotoImage(file = "image/fengshui/"+str(i)+".png"))
            self.avengers_list.append(PhotoImage(file = "image/avengers/"+str(i)+".png"))
            self.incredibles2_list.append(PhotoImage(file = "image/incredibles2/"+str(i)+".png"))
            
        self.label_list = [] 
        for i in range(4):
            self.label_list.append(Label(frame2, image = self.bagic_list[i])) 
            self.label_list[i].pack(side=LEFT)

        frame3 = Frame(movie_2018)
        
        scrollbar = Scrollbar(frame3)
        scrollbar.pack(side="right",fill="y")
        text = Text(frame3, width = 110, height = 10, yscrollcommand = scrollbar.set)
        text.pack(side="left")
        scrollbar["command"] = text.yview

        frame4 = Frame(movie_2018)
        Button(frame4, text = "예약",bg = "#ff8", width = 110, font=30, command = self.reserv_list).pack()

        frame1.pack()
        frame2.pack()
        frame3.pack()
        frame4.pack()
        movie_2018.mainloop()

    def open_select(self):
        movie_select = Toplevel()
        movie_select.title("관리자 추천영화")
        movie_select.geometry("840x700")

        menubar = Menu(movie_select) #메뉴바 생성
        movie_select.config(menu = menubar) # 메뉴바 표시
        movemenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "이동",menu = movemenu)
        movemenu.add_command(label = "영화구분", command = movie_select.destroy)

        frame1 = Frame(movie_select)
        
        self.movie_list = []
        for i in range(1,4):
            self.movie_list.append(PhotoImage(file = "image/movie_select/"+str(i)+".png"))
            
        self.Radio_list = []
        self.v1 = IntVar()
        for i in range(3):
            self.Radio_list.append(Radiobutton(frame1, image = self.movie_list[i],variable = self.v1, value = i, command = self.myRb_select))
            self.Radio_list[i].pack(side=LEFT)

        frame2 = Frame(movie_select)

        self.bagic_list = []
        self.bewithyou_list = []
        self.interstellar_list = []
        self.littleforest_list = []
        
        for i in range(1,5):
            self.bagic_list.append(PhotoImage(file = "image/bagics/"+str(i)+".png"))
            self.bewithyou_list.append(PhotoImage(file = "image/bewithyou/"+str(i)+".png"))
            self.interstellar_list.append(PhotoImage(file = "image/interstellar/"+str(i)+".png"))
            self.littleforest_list.append(PhotoImage(file = "image/littleforest/"+str(i)+".png"))
            
        self.label_list = [] 
        for i in range(4):
            self.label_list.append(Label(frame2, image = self.bagic_list[i])) 
            self.label_list[i].pack(side=LEFT)

        frame3 = Frame(movie_select)
        
        scrollbar = Scrollbar(frame3)
        scrollbar.pack(side="right",fill="y")
        text = Text(frame3, width = 110, height = 10, yscrollcommand = scrollbar.set)
        text.pack(side="left")
        scrollbar["command"] = text.yview

        frame4 = Frame(movie_select)
        Button(frame4, text = "예약",bg = "#ff8", width = 110, font=30, command = self.reserv_list).pack()

        frame1.pack()
        frame2.pack()
        frame3.pack()
        frame4.pack()
        movie_select.mainloop()

    def myRb_2018(self):
        if self.v1.get() == 0:
            for i in range(4):
                self.label_list[i]["image"] = self.fengshui_list[i]
            fr=open('fengshui.txt','r')
            read=fr.read()
            #text.insert(a)
            print(read)
            fr.close()
            
        elif self.v1.get() ==1:
            for i in range(4):
                self.label_list[i]["image"] = self.avengers_list[i] #-> 파일에서 읽어들인 텍스트정보를 frame2 = Frame(movie_2018)에 있는 label에 출력
            fr=open('avengers.txt','r')
            read=fr.read()
            #text.insert(a) -> 파일에서 읽어들인 텍스트정보를 frame3 = Frame(movie_2018)에 있는 text박스에 출력
            print(read)
            fr.close()
            
        elif self.v1.get() ==2:
            for i in range(4):
                self.label_list[i]["image"] = self.incredibles2_list[i]
            fr=open('incredibles2.txt','r')
            read=fr.read()
            #text.insert(a)
            print(read)
            fr.close()

    def myRb_select(self):
        if self.v1.get() == 0:
            for i in range(4):
                self.label_list[i]["image"] = self.bewithyou_list[i]
            fr=open('bewithyou.txt','r')
            read=fr.read()
            print(read)
            fr.close()
            
        elif self.v1.get() ==1:
            for i in range(4):
                self.label_list[i]["image"] = self.interstellar_list[i]
            fr=open('interstellar.txt','r')
            read=fr.read()
            print(read)
            fr.close()
            
        elif self.v1.get() ==2:
            for i in range(4):
                self.label_list[i]["image"] = self.littleforest_list[i]
            fr=open('littleforest.txt','r')
            read=fr.read()
            print(read)
            fr.close()

    def reserv_list(self):
        print("성공")
        
         # v1.get()값을 어떻게 읽어와야 하는지 모르겠습니다.
         
         #if self.v1.get() == 0:
            #fw=open('reservation.txt','w')
            #data="명당 - 다운로드: https://nstore.naver.com/movie/detail.nhn?productNo=3694860 \n"
            #fw.write(data)
            #fw.close()

        #elif self.v1.get() ==1:
            #fw=open('reservation.txt','w')
            #data="어벤져스: 인피니티 워 - 다운로드: https://nstore.naver.com/movie/detail.nhn?productNo=3593762 \n"
            #fw.write(data)
            #fw.close()

        #elif self.v1.get() ==2:
            #fw=open('reservation.txt','w')
            #data="인크레더블2 다운로드: https://nstore.naver.com/movie/detail.nhn?productNo=3766058 \n"
            #fw.write(data)
            #fw.close()

PythonCinema()

        
    
