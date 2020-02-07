from tkinter import *
from tkinter import messagebox
gato=Tk()
gato.resizable(1,1)
gato.title("Gato")
gato.geometry("400x300")
gato.config(bg="dark orange1")
gato.config(cursor="arrow")
tu=StringVar()
p1=StringVar()
p2=StringVar()
p3=StringVar()
p4=StringVar()
p5=StringVar()
p6=StringVar()
p7=StringVar()
p8=StringVar()
p9=StringVar()
p1.set("1")
p2.set("2")
p3.set("3")
p4.set("4")
p5.set("5")
p6.set("6")
p7.set("7")
p8.set("8")
p9.set("9")
fondo=PhotoImage(file="fondo.png")
x=PhotoImage(file="x.png")
o=PhotoImage(file="o.png")
empate=StringVar()
empate.set("9")
n1=StringVar()
n1.set("1")

contador=StringVar()
contador.set("0")
n2=StringVar()
n2.set("1")

contador2=StringVar()
contador2.set("0")
n3=StringVar()
n3.set("1")

def valida():
	if p1.get() == p2.get() and p1.get() == p3.get():
		if p1.get()=="x":
			messagebox.showinfo(message="gano o", title="Gana")
			contador.set(int(contador.get())+int(n2.get()))
		else:
			messagebox.showinfo(message="gano x", title="Gana")
			contador2.set(int(contador2.get())+int(n3.get()))
		desabilita()
	elif p4.get() == p5.get() and p4.get() == p6.get():
		if p4.get()=="x":
			messagebox.showinfo(message="gano o", title="Gana")
			contador.set(int(contador.get())+int(n2.get()))
		else:
			messagebox.showinfo(message="gano x", title="Gana")
			contador2.set(int(contador2.get())+int(n3.get()))
		desabilita()
	elif p7.get() == p8.get() and p7.get() == p9.get():
		if p7.get()=="x":
			messagebox.showinfo(message="gano o", title="Gana")
			contador.set(int(contador.get())+int(n2.get()))
		else:
			messagebox.showinfo(message="gano x", title="Gana")
			contador2.set(int(contador2.get())+int(n3.get()))
		desabilita()
	elif p1.get() == p4.get() and p1.get() == p7.get():
		if p1.get()=="x":
			messagebox.showinfo(message="gano o", title="Gana")
			contador.set(int(contador.get())+int(n2.get()))
		else:
			messagebox.showinfo(message="gano x", title="Gana")
			contador2.set(int(contador2.get())+int(n3.get()))
		desabilita()
	elif p2.get() == p5.get() and p2.get() == p8.get():
		if p2.get()=="x":
			messagebox.showinfo(message="gano o", title="Gana")
			contador.set(int(contador.get())+int(n2.get()))
		else:
			messagebox.showinfo(message="gano x", title="Gana")
			contador2.set(int(contador2.get())+int(n3.get()))
		desabilita()
	elif p3.get() == p6.get() and p3.get() == p9.get():
		if p3.get()=="x":
			messagebox.showinfo(message="gano o", title="Gana")
			contador.set(int(contador.get())+int(n2.get()))
		else:
			messagebox.showinfo(message="gano x", title="Gana")
			contador2.set(int(contador2.get())+int(n3.get()))
		desabilita()
	elif p1.get() == p5.get() and p1.get() == p9.get():
		if p1.get()=="x":
			messagebox.showinfo(message="gano o", title="Gana")
			contador.set(int(contador.get())+int(n2.get()))
		else:
			messagebox.showinfo(message="gano x", title="Gana")
			contador2.set(int(contador2.get())+int(n3.get()))
		desabilita()
	elif p3.get() == p5.get() and p3.get() == p7.get():
		if p3.get()=="x":
			messagebox.showinfo(message="gano o", title="Gana")
			contador.set(int(contador.get())+int(n3.get()))
		else:
			messagebox.showinfo(message="gano x", title="Gana")
			contador2.set(int(contador2.get())+int(n2.get()))
		desabilita()
	elif empate.get()=="0":
		messagebox.showinfo(message="EMPATE: Nadie gana", title="EMPATE")
		desabilita()

def posicion1():
	if tu.get()=="x":
		boton1.config(image=o)
		p1.set("x")
		tu.set("o")
		boton1.config(state=DISABLED)
	else:
		tu.set("x")
		p1.set("o")
		boton1.config(image=x)
		boton1.config(state=DISABLED)
	empate.set(int(empate.get())-int(n1.get()))
	valida()
def posicion2():
	if tu.get()=="x":
		boton2.config(image=o)
		p2.set("x")
		tu.set("o")
		boton2.config(state=DISABLED)
	else:
		tu.set("x")
		p2.set("o")
		boton2.config(image=x)
		boton2.config(state=DISABLED)
	empate.set(int(empate.get())-int(n1.get()))
	valida()
def posicion3():
	if tu.get()=="x":
		boton3.config(image=o)
		p3.set("x")
		tu.set("o")
		boton3.config(state=DISABLED)
	else:
		tu.set("x")
		p3.set("o")
		boton3.config(image=x)
		boton3.config(state=DISABLED)
	empate.set(int(empate.get())-int(n1.get()))
	valida()
def posicion4():
	if tu.get()=="x":
		boton4.config(image=o)
		p4.set("x")
		tu.set("o")
		boton4.config(state=DISABLED)
	else:
		tu.set("x")
		p4.set("o")
		boton4.config(image=x)
		boton4.config(state=DISABLED)
	empate.set(int(empate.get())-int(n1.get()))
	valida()
def posicion5():
	if tu.get()=="x":
		boton5.config(image=o)
		p5.set("x")
		tu.set("o")
		boton5.config(state=DISABLED)
	else:
		tu.set("x")
		p5.set("o")
		boton5.config(image=x)
		boton5.config(state=DISABLED)
	empate.set(int(empate.get())-int(n1.get()))
	valida()
def posicion6():
	if tu.get()=="x":
		boton6.config(image=o)
		p6.set("x")
		tu.set("o")
		boton6.config(state=DISABLED)
	else:
		tu.set("x")
		p6.set("o")
		boton6.config(image=x)
		boton6.config(state=DISABLED)
	empate.set(int(empate.get())-int(n1.get()))
	valida()
def posicion7():
	if tu.get()=="x":
		boton7.config(image=o)
		p7.set("x")
		tu.set("o")
		boton7.config(state=DISABLED)
	else:
		tu.set("x")
		p7.set("o")
		boton7.config(image=x)
		boton7.config(state=DISABLED)
	empate.set(int(empate.get())-int(n1.get()))
	valida()
def posicion8():
	if tu.get()=="x":
		boton8.config(image=o)
		p8.set("x")
		tu.set("o")
		boton8.config(state=DISABLED)
	else:
		tu.set("x")
		p8.set("o")
		boton8.config(image=x)
		boton8.config(state=DISABLED)
	empate.set(int(empate.get())-int(n1.get()))
	valida()
def posicion9():
	if tu.get()=="x":
		boton9.config(image=o)
		p9.set("x")
		tu.set("o")
		boton9.config(state=DISABLED)
	else:
		tu.set("x")
		p9.set("o")
		boton9.config(image=x)
		boton9.config(state=DISABLED)
	empate.set(int(empate.get())-int(n1.get()))
	valida()

def desabilita():
	boton1.config(state=DISABLED)
	boton2.config(state=DISABLED)
	boton3.config(state=DISABLED)
	boton4.config(state=DISABLED)
	boton5.config(state=DISABLED)
	boton6.config(state=DISABLED)
	boton7.config(state=DISABLED)
	boton8.config(state=DISABLED)
	boton9.config(state=DISABLED)

def reiniciar():
	boton1.config(state=NORMAL,image=fondo,)
	boton2.config(state=NORMAL,image=fondo,)
	boton3.config(state=NORMAL,image=fondo,)
	boton4.config(state=NORMAL,image=fondo,)
	boton5.config(state=NORMAL,image=fondo,)
	boton6.config(state=NORMAL,image=fondo,)
	boton7.config(state=NORMAL,image=fondo,)
	boton8.config(state=NORMAL,image=fondo,)
	boton9.config(state=NORMAL,image=fondo,)
	p1.set("1")
	p2.set("2")
	p3.set("3")
	p4.set("4")
	p5.set("5")
	p6.set("6")
	p7.set("7")
	p8.set("8")
	p9.set("9")
	tu.set("o")
	empate.set("9")
	n1.set("1")
def reinicia_marcador():
	contador.set("0")
	n2.set("1")
	contador2.set("0")
	n3.set("1")


boton1=Button(gato,text=".",bg="white",command=posicion1,image=fondo,textvariable=p1)
boton1.place(x=20,y=50)

boton2=Button(gato,text=".",bg="white",command=posicion2,image=fondo,textvariable=p2)
boton2.place(x=100,y=50)

boton3=Button(gato,text=".",bg="white",command=posicion3,image=fondo,textvariable=p3)
boton3.place(x=180,y=50)

boton4=Button(gato,text=".",bg="white",command=posicion4,image=fondo)
boton4.place(x=20,y=100)

boton5=Button(gato,text=".",bg="white",command=posicion5,image=fondo)
boton5.place(x=100,y=100)

boton6=Button(gato,text=".",bg="white",command=posicion6,image=fondo)
boton6.place(x=180,y=100)

boton7=Button(gato,text=".",bg="white",command=posicion7,image=fondo)
boton7.place(x=20,y=150)

boton8=Button(gato,text=".",bg="white",command=posicion8,image=fondo)
boton8.place(x=100,y=150)

boton9=Button(gato,text=".",bg="white",command=posicion9,image=fondo)
boton9.place(x=180,y=150)

boton9=Button(gato,text=".",bg="white",command=posicion9,image=fondo)
boton9.place(x=180,y=150)

reiniciar=Button(gato,text="Reiniciar",font="Arial",bg="white",command=reiniciar)
reiniciar.place(x=250,y=150)

reiniciar_m=Button(gato,text="Reiniciar Marcador",font="Arial",bg="white",command=reinicia_marcador)
reiniciar_m.place(x=250,y=190)

ganax=Label(gato, text="0",bg="white",font="timesnewroman 10 bold",relief="raised",width=2,textvariable=contador)
ganax.place(x=165,y=200)

etiquetax=Label(gato, text="O",bg="red2",font="timesnewroman 10 bold",relief="raised",width=2)
etiquetax.place(x=190,y=200)

ganao=Label(gato, text="0",bg="white",font="timesnewroman 10 bold",relief="raised",width=2,textvariable=contador2)
ganao.place(x=165,y=230)

etiquetao=Label(gato, text="X",bg="orange1",font="timesnewroman 10 bold",relief="raised",width=2)
etiquetao.place(x=190,y=230)

gato.mainloop()