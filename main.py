import os
from tkinter import *
import PIL
from PIL import Image,ImageTk
import mysql.connector

from empleados import Empleados
from entrenador import Train


class Reconocimiento_facial_heavens:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Control de empleados y nomina Heavens Fruits S.A.S")
        
        
        # Primera Imagen (Uchuva):
        img=Image.open(r'Images\babyheavens.jpg')
        img=img.resize((500,500),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # Segunda Imagen (Mango):
        img1=Image.open(r'Images\babyheavens.jpg')
        img1=img1.resize((500,500),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        # Tercera imagen (Guayaba):
        img2=Image.open(r'Images\babyheavens.jpg')
        img2=img2.resize((500,500),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)


        # Imagen Background():
        img3=Image.open(r'fondo.jpg')
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="Control Heavens Fruits S.A.S",font=("book antiqua",35,"bold"),bg="white",fg="dark orange")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # Boton (Empleados):
        img4=Image.open(r'Images\empleado.jpg')
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.empleados_detalles,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Menú Empleados",command=self.empleados_detalles,cursor="hand2",font=("book antiqua",15),bg="red",fg="black")
        b1_1.place(x=200,y=300,width=220,height=40)


        # Boton (Reconocimiento Facial):
        img5=Image.open(r'Images\Reconocimiento_facial.png')
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Reconocimiento Facial",cursor="hand2",font=("book antiqua",15),bg="red",fg="black")
        b1_1.place(x=500,y=300,width=220,height=40)


        # Boton (Asistencia por Reconocimiento Facial):
        img6=Image.open(r'Images\control_asistencia.jpg')
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Asistencia IA",cursor="hand2",font=("book antiqua",15),bg="red",fg="black")
        b1_1.place(x=800,y=300,width=220,height=40)


        # Boton (Proyectos adicionales, pdte Help):
        img7=Image.open(r'Images\control_asistencia.jpg')
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Proyectos a futuro help",cursor="hand2",font=("book antiqua",15),bg="red",fg="black")
        b1_1.place(x=1100,y=300,width=220,height=40)


        # Boton (Entramiento de reconocimiento facial):
        img8=Image.open(r'Images\control_asistencia.jpg')
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Entrenador IA",cursor="hand2",command=self.train_data,font=("book antiqua",15),bg="red",fg="black")
        b1_1.place(x=200,y=580,width=220,height=40)


        # Boton (Imagenes Guardadas):
        img9=Image.open(r'Images\control_asistencia.jpg')
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Rostros Guardados",cursor="hand2",command=self.open_img,font=("book antiqua",15),bg="red",fg="black")
        b1_1.place(x=500,y=580,width=220,height=40)



        # Boton (Sugerencias por parte del equipo de Heavens para desarrollo):
        img10=Image.open(r'Images\control_asistencia.jpg')
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Sugerencias equipo Heavens",cursor="hand2",font=("book antiqua",12),bg="red",fg="black")
        b1_1.place(x=800,y=580,width=220,height=40)

        #Boton (Salir):
        img11=Image.open(r'Images\control_asistencia.jpg')
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Salir",cursor="hand2",font=("book antiqua",12),bg="red",fg="black")
        b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("coleccion_IA")


# ==================== Funciones de botones =================================
    def empleados_detalles(self):
        self.new_window=Toplevel(self.root)
        self.app=Empleados(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

if __name__ == "__main__":
    root=Tk()
    obj=Reconocimiento_facial_heavens(root)
    root.mainloop()