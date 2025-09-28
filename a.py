from guizero import App, Text, PushButton

def on_click():
    greeting.value = "Bạn đã nhấn nút!"

app = App(title="Xin chào GUIZERO", width=420, height=180)
greeting = Text(app, text="Xin chào, thế giới!", size=14)
btn = PushButton(app, text="Nhấn tôi", command=on_click)
app.display()