from guizero import App, Text, Picture
app=App(title='Giới thiệu bản thân', width=1000, height=800, bg='lightblue')
text=Text(app, text='Giới Thiệu Bản Thân', size=30, color='green', font='Courier new bold')
text1=Text(app, text='Tên: Phạm Lê Gia Hưng\n'
                     'Tuổi: 12\n'
                     'Trường: THSC Cao Thắng\n'
                     'Giới tính: Nam\n'
                     'Sở thích: Chơi game và thể thao\n', size=17, color='red', font='Times new roman')
hinhanh=Picture(app,'slasher.png',width=500,height=500)
app.display()