from guizero import Picture,App,Text,Box

app = App(title="Báo VNEXPRESS",width= 1000,height=1000)
box0 = Box(app,align="left")
box1 = Box(box0)
box2 = Box(box0)
box3 = Box(app,align="right")
text1 = Text(box1,text= "Người Việt mua ôtô điện nhiều thứ hai Đông Nam Á",size= 20,color= "Black",bold= True)
text2 = Text(box1,text= 
'Sau 8 tháng đầu 2025, thị trường Việt tiêu thụ 89.970 xe thuần điện, Thái Lan dẫn \n'
'đầu với 92.665 xe.\n'
'Việt Nam là thị trường ôtô lớn thứ 4 Đông Nam Á về doanh số xe mới hàng năm sau \n'
'Indonesia, Malaysia, Thái Lan, nhưng nếu tính riêng xe thuần điện chạy bằng pin \n'
'(BEV - Battery Electric Vehicle), Việt Nam hiện xếp thứ hai.\n' ,size= 25,color= "blue",align="top")
thongke = Picture(box2,'thongke.png')
quangcao = Picture(box3,'quangcao.png')
app.display()