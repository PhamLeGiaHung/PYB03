from guizero import App,Text,Picture
app = App(title = "Thiệp chúc mừng" , height= 1000, width= 1000)
text = Text(app,text = "Chúc mừng sinh nhật!")
picture = Picture(app, image= "q.png")
text2 =Text(app,text = "Khám phá những điều kì diệu bên trong!")
app.display()