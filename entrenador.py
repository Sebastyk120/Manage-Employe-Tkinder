import os
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import cv2
import numpy as np
from numpy import resize


class Train:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1530x790+0+0")
		self.root.title("Control de empleados y nomina Heavens Fruits S.A.S")

		title_lbl = Label(self.root, text="Entrenador de Datos IA", font=("book antiqua", 35, "bold"), bg="white",fg="Red")
		title_lbl.place(x=0, y=0, width=1530, height=45)

		img_top=Image.open(r'C:\Proyecto Heavens\Images\bigsur.jpg')
		img_top=img_top.resize((1530,325),Image.ANTIALIAS)
		self.photoimg_top=ImageTk.PhotoImage(img_top)

		f_lbl=Label(self.root,image=self.photoimg_top)
		f_lbl.place(x=0,y=55,width=1530,height=325)

		#Boton
		b1_1=Button(self.root,text="Entrenador De Datos",command=self.entrenador_clasificador,cursor="hand2",font=("book antiqua",30),bg="red",fg="white")
		b1_1.place(x=0,y=380,width=1530,height=60)

		img_bottom=Image.open(r'C:\Proyecto Heavens\Images\bigsur.jpg')
		img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)
		self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

		f_lbl=Label(self.root,image=self.photoimg_bottom)
		f_lbl.place(x=0,y=440,width=1530,height=325)


	def entrenador_clasificador(self):
		data_dir=("coleccion_IA")
		path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
		
		faces=[]
		ids=[]

		for image in path:
			img=Image.open(image).convert('L') # Escala de Grises
			imageNp=np.array(img,'uint8')
			id=int(os.path.split(image)[1].split('.')[1])

			faces.append(imageNp)
			ids.append(id)
			cv2.imshow("Entrenador",imageNp)
			cv2.waitKey(1)==13
		ids=np.array(ids)

		#================= Entrenador de Clasificación y Guardar =================
		clf=cv2.face.LBPHFaceRecognizer_create()
		clf.train(faces,ids)
		clf.write("classifier.xml")
		cv2.destroyAllWindows()
		messagebox.showinfo("Resultado", "Entrenados de datos IA completado")






if __name__ == '__main__':
	root=Tk()
	obj=Train(root)
	root.mainloop()