import customtkinter as ctk
from customtkinter import CTk, CTkEntry, CTkButton, set_appearance_mode, set_default_color_theme

FONT_TYPE = "Meiryo"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # メンバー変数の設定
        self.fonts = (FONT_TYPE, 15)
        # フォームサイズ設定
        self.geometry("350x200")
        self.title("Basic GUI")

        # フォームのセットアップをする
        self.setup_form()
    
    def setup_form(self):
        # ctk のフォームデザイン設定
        ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        # テキストボックスを表示する
        self.textbox = ctk.CTkEntry(master=self, placeholder_text="テキストを入力してください", width=220, font=self.fonts)
        self.textbox.place(x=60, y=50)

        # ボタンを表示する
        self.button = ctk.CTkButton(master=self, text="クリックしてね", command=self.button_function, font=self.fonts)
        self.button.place(x=100, y=100)
    
    def button_function(self):
        # テキストボックスに入力されたテキストを表示する
        print(self.textbox.get())


if __name__ == "__main__":
    # アプリケーション実行
    app = App()
    app.mainloop()