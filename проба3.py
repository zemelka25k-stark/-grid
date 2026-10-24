from tkinter import*
from tkinter import Tk

root = Tk()
root.title("123")
root.geometry("1000x500")
root.resizable(False, False)

def finish():
    root.destroy()
    print("Он покинул это место....")
root.protocol("WM_DELETE_WINDOW", finish)

for i in range(5): root.columnconfigure(index=i , weight=4)
for j in range(6): root.columnconfigure(index=j , weight=5)

for i in range(7):
    for j in range(5):
        btn = Button(text=f"({i},{j}")
        btn.grid(row=i,column=j, columnspan=4, rowspan=2)

btn2 = Button(root, text="k")
btn2.grid(row=10, column=5, rowspan=2, ipadx=5, ipady=2)
btn3 = Button(root, text="n")
btn3.grid(row=11, column=5, ipadx=5, ipady=2)

sp1 = [1,2,4,8,16]
sp2 = [3,5,6,7]
for sp1 in list(range(2)):
    for sp2 in list(range(2)): 
     btn8 = Button(text=f"({sp1},{sp2})")
    btn8.grid(row=sp1,column=sp2, ipady=3)
        

root.mainloop()