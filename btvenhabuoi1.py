"""Bài tập 2.1 (Cơ bản):

Tạo cửa sổ kích thước 600x400, tiêu đề "Luyện tập Bài 2".
Bài tập 2.2 (Định dạng):

Đặt màu nền là "lightblue".
Thêm một Text "Xin chào, tôi đang học GUIZERO", màu "red", size 16.
Bài tập 2.3 (Sáng tạo):

Tạo một cửa sổ với tiêu đề "Hộp thoại của tôi".
Chèn 2 Text: một dòng giới thiệu tên bạn, một dòng ghi "Học GUI thật thú vị!".
Thử thay đổi màu chữ từng dòng."""


# Bài tập 2.1 (Cơ bản)
from guizero import App

app = App(title="Luyện tập Bài 2.1", width=600, height=400)
app.display()

# Bài tập 2.2 (Định dạng)
from guizero import App, Text

app = App(title="Luyện tập Bài 2.2", width=600, height=400, bg="lightblue")
text = Text(app, text="Xin chào, tôi đang học GUIZERO", color="red", size=16)
app.display()

# Bài tập 2.3 (Sáng tạo)
from guizero import App, Text

app = App(title="Hộp thoại của tôi 2.3", width=400, height=300)
ten = Text(app, text="Mình tên là BQY MKJ", color="blue", size=14)
dong2 = Text(app, text="Học GUI thật thú vị!", color="green", size=16)
app.display()

