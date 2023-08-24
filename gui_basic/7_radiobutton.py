from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

Label(root, text="메뉴를 선택하세요").pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root,text="햄버거",value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root,text="치즈버거",value=2, variable=burger_var)
btn_burger3 = Radiobutton(root,text="치킨버거",value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료를 선택하세요").pack()

drinkvar = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drinkvar)
btn_drink1.select() # 기본값 선택
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drinkvar)

btn_drink1.pack()
btn_drink2.pack()



def btncmd():
    print(burger_var.get()) # 햄버거 중 선택된 라디오 항목의 값(value)
    print(drinkvar.get()) # 음료중 선택된 값을 출력

btn = Button(root, text="주문", command=btncmd)
btn.pack()


root.mainloop()
