from guizero import App, Text, Picture
app=App(title='Giới thiệu đặc sản', width=1000, height=800, bg='lightblue')
text=Text(app, text='Giới Thiệu Đặc sản', size=30, color='green', font='Courier new bold')
text1=Text(app, text='Tên: Phở\n'
                     'Đặc sản: Việt Nam\n'
                     'Hương vị rất ngon\n'
                     'Chế biến từ sợi mì,thịt bò và nước lèo\n'
                     'Hãy thử 1 lần\n', size=17, color='red', font='Times new roman')
hinhanh=Picture(app,'pho.png',width=700,height=600)
app.display()