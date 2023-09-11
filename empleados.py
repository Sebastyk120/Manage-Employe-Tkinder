from tkinter import *
from tkinter import messagebox, ttk
import cv2
import mysql.connector
from numpy import resize
from PIL import Image, ImageTk


class Empleados:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1530x790+0+0")
		self.root.title("Control de empleados y nomina Heavens Fruits S.A.S")

		#==============================Variables===============================

		self.var_Departamento=StringVar()
		self.var_Cargo_Empleado=StringVar()
		self.var_Ano=StringVar()
		self.var_Contrato=StringVar()
		self.var_Id_Empleado=StringVar()
		self.var_Nombre_Empleado=StringVar()
		self.var_Subdepartamento=StringVar()
		self.var_Cargo_No=StringVar()
		self.var_Genero=StringVar()
		self.var_nacimiento=StringVar()
		self.var_Correo=StringVar()
		self.var_Telefono=StringVar()
		self.var_Direccion=StringVar()
		self.var_Jefe_Directo=StringVar()

		# Primera Imagen (Empleados):
		img=Image.open(r'Images\win11.jpg')
		img=img.resize((500,130),Image.ANTIALIAS)
		self.photoimg=ImageTk.PhotoImage(img)

		f_lbl=Label(self.root,image=self.photoimg)
		f_lbl.place(x=0,y=0,width=500,height=130)

		# Segunda Imagen (Empleados):
		img1=Image.open(r'Images\win11.jpg')
		img1=img1.resize((500,130),Image.ANTIALIAS)
		self.photoimg1=ImageTk.PhotoImage(img1)

		f_lbl=Label(self.root,image=self.photoimg1)
		f_lbl.place(x=500,y=0,width=500,height=130)

		# Tercera imagen (Empleados):
		img2=Image.open(r'Images\win11.jpg')
		img2=img2.resize((500,130),Image.ANTIALIAS)
		self.photoimg2=ImageTk.PhotoImage(img2)

		f_lbl=Label(self.root,image=self.photoimg2)
		f_lbl.place(x=1000,y=0,width=500,height=130)

		# Imagen Background(IA):
		img3=Image.open(r'fondo.jpg')
		img3=img3.resize((1530,710),Image.ANTIALIAS)
		self.photoimg3=ImageTk.PhotoImage(img3)

		bg_img=Label(self.root,image=self.photoimg3)
		bg_img.place(x=0,y=130,width=1530,height=710)

		title_lbl=Label(bg_img,text="Sistema De Administración De Empleados",font=("book antiqua",35,"bold"),bg="white",fg="dark orange")
		title_lbl.place(x=0,y=0,width=1530,height=45)

		main_frame=Frame(bg_img,bd=2,bg="white")
		main_frame.place(x=20,y=50,width=1480,height=600)

		# Marco de nivel izquierdo:
		Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Formulario De Empleados",font=("book antiqua",12,"bold"))
		Left_frame.place(x=10,y=10,width=730,height=580)

		img_left=Image.open(r'Images\bigsur.jpg')
		img_left=img_left.resize((720,130),Image.ANTIALIAS)
		self.photoimg_left=ImageTk.PhotoImage(img_left)

		f_lbl=Label(Left_frame,image=self.photoimg_left)
		f_lbl.place(x=5,y=0,width=720,height=130)


		#Información del empleado a registrar:
		Empleados_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Secciones Para Empleados",font=("book antiqua",12,"bold"),fg="black")
		Empleados_frame.place(x=5,y=135,width=720,height=115)

		# Departamentos Heavens:
		dep_label=Label(Empleados_frame,text="Departamento: ",font=("book antiqua",12,"bold"),bg="white")
		dep_label.grid(row=0,column=0,padx=10,sticky=W)

		dep_combo=ttk.Combobox(Empleados_frame,textvariable=self.var_Departamento,font=("book antiqua",10,"bold"),state="readonly",width=20)
		dep_combo["values"]=("Seleccione","Gerencia","Logistica","Compras","Recursos Humanos","Recibo","Operativos","Administrativos")
		dep_combo.current(0)
		dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

		# Cargos Del Empleado Heavens:
		cargo_label=Label(Empleados_frame,text="Cargo Empleado:",font=("book antiqua",12,"bold"),bg="white")
		cargo_label.grid(row=0,column=2,padx=10,sticky=W)

		cargo_combo=ttk.Combobox(Empleados_frame,textvariable=self.var_Cargo_Empleado,font=("book antiqua",10,"bold"),state="readonly",width=20)
		cargo_combo["values"]=("Seleccione","Gerente","Coordinador","Empacador","Asistente","Conductor","Jefe","Administrativo")
		cargo_combo.current(0)
		cargo_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

		# Año de ingreso a Heavens:
		ano_label=Label(Empleados_frame,text="Año De Ingreso:",font=("book antiqua",12,"bold"),bg="white")
		ano_label.grid(row=1,column=0,padx=10,sticky=W)

		ano_combo=ttk.Combobox(Empleados_frame,textvariable=self.var_Ano,font=("book antiqua",10,"bold"),state="readonly",width=20)
		ano_combo["values"]=("Seleccione","2021","2020","2019","2018","2017","2016","2015")
		ano_combo.current(0)
		ano_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

		# Tipo de contrato:
		contrato_label=Label(Empleados_frame,text="Contrato:",font=("book antiqua",12,"bold"),bg="white")
		contrato_label.grid(row=1,column=2,padx=10,sticky=W)

		contrato_combo=ttk.Combobox(Empleados_frame,textvariable=self.var_Contrato,font=("book antiqua",10,"bold"),state="readonly",width=20)
		contrato_combo["values"]=("Seleccione","Indefinido","Termino_Fijo","Obra_O_labor","Temporal","Prestación_De_servicios")
		contrato_combo.current(0)
		contrato_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

		#Datos del empleado a registrar:
		class_Empleado_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Datos Empleados Heavens",font=("book antiqua",12,"bold"),fg="black")
		class_Empleado_frame.place(x=5,y=250,width=720,height=300)


		# Id empleado:
		EmpleadoId_label=Label(class_Empleado_frame,text="Empleado Id:",font=("book antiqua",12,"bold"),bg="white")
		EmpleadoId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

		EmpleadoID_entry=ttk.Entry(class_Empleado_frame,textvariable=self.var_Id_Empleado,width=20,font=("book antiqua",12,"bold"))
		EmpleadoID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

		# Nombre empleado:
		EmpleadoName_label=Label(class_Empleado_frame,text="Nombre Empleado:",font=("book antiqua",12,"bold"),bg="white")
		EmpleadoName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

		EmpleadoName_entry=ttk.Entry(class_Empleado_frame,textvariable=self.var_Nombre_Empleado,width=20,font=("book antiqua",12,"bold"))
		EmpleadoName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

		# class Sub Departamento de Empleado:
		class_div_label=Label(class_Empleado_frame,text="Subdepartamento:",font=("book antiqua",12,"bold"),bg="white")
		class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)


		div_combo=ttk.Combobox(class_Empleado_frame,textvariable=self.var_Subdepartamento,font=("book antiqua", 10, "bold"), state="readonly", width=20)
		div_combo["values"]=("Seleccione","Financiero","Operaciones","Gestion","Tecnología","Publicidad","Inventarios")
		div_combo.current(0)
		div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

		# Codigo de Cargo:
		roll_no_label=Label(class_Empleado_frame,text="Codigo de Cargo:",font=("book antiqua",12,"bold"),bg="white")
		roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

		roll_no_entry=ttk.Entry(class_Empleado_frame,textvariable=self.var_Cargo_No,width=20,font=("book antiqua",12,"bold"))
		roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

		# Genero de Empleado:
		gender_label=Label(class_Empleado_frame,text="Genero:",font=("book antiqua",12,"bold"),bg="white")
		gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

		gender_combo=ttk.Combobox(class_Empleado_frame,textvariable=self.var_Genero,font=("book antiqua",10,"bold"),state="readonly",width=20)
		gender_combo["values"]=("Masculino","Femenino")
		gender_combo.current(0)
		gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

		# Fecha de nacimiento de Empleado:
		dob_label=Label(class_Empleado_frame,text="Fecha De Nacimiento:",font=("book antiqua",12,"bold"),bg="white")
		dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

		dob_entry=ttk.Entry(class_Empleado_frame,textvariable=self.var_nacimiento,width=20,font=("book antiqua",12,"bold"))
		dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

		# Email de Empleado:
		email_label=Label(class_Empleado_frame,text="Correo:",font=("book antiqua",12,"bold"),bg="white")
		email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

		email_entry=ttk.Entry(class_Empleado_frame,textvariable=self.var_Correo,width=20,font=("book antiqua",12,"bold"))
		email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

		# Telefono de Empleado:
		phone_label=Label(class_Empleado_frame,text="Numero De Telefono:",font=("book antiqua",12,"bold"),bg="white")
		phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

		phone_entry=ttk.Entry(class_Empleado_frame,textvariable=self.var_Telefono,width=20,font=("book antiqua",12,"bold"))
		phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

		# Dirección de Empleado:
		address_label=Label(class_Empleado_frame,text="Dirección:",font=("book antiqua",12,"bold"),bg="white")
		address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

		address_entry=ttk.Entry(class_Empleado_frame,textvariable=self.var_Direccion,width=20,font=("book antiqua",12,"bold"))
		address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

		# Jefe directo de Empleado:
		jefed_label=Label(class_Empleado_frame,text="Jefe Directo:",font=("book antiqua",12,"bold"),bg="white")
		jefed_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

		jefed_entry=ttk.Entry(class_Empleado_frame,textvariable=self.var_Jefe_Directo,width=20,font=("book antiqua",12,"bold"))
		jefed_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

		#Botones (IA):
		self.var_radio1=StringVar()
		radionbtn1=ttk.Radiobutton(class_Empleado_frame,variable=self.var_radio1,text="IA de muestra asignada",value="Yes")
		radionbtn1.grid(row=6,column=0)


		radionbtn2=ttk.Radiobutton(class_Empleado_frame,variable=self.var_radio1,text="IA sin asignar",value="No")
		radionbtn2.grid(row=6,column=1)

		# Botones para Reconocimiento por Empleado:
		btn_frame=Frame(class_Empleado_frame,bd=2,relief=RIDGE,bg="White")
		btn_frame.place(x=0,y=220,width=750,height=40)

		save_btn=Button(btn_frame,text="Guardar",command=self.add_data,width=21,font=("book antiqua",10,"bold"),bg="dark orange",fg="black")
		save_btn.grid(row=0,column=0)

		update_btn=Button(btn_frame,text="Actualizar",command=self.update_data,width=21,font=("book antiqua",10,"bold"),bg="dark orange",fg="black")
		update_btn.grid(row=0,column=1)

		delete_btn=Button(btn_frame,text="Eliminar",command=self.delete_data,width=21,font=("book antiqua",10,"bold"),bg="dark orange",fg="black")
		delete_btn.grid(row=0,column=2)

		reset_btn=Button(btn_frame,text="Limpiar",command=self.reset_data,width=21,font=("book antiqua",10,"bold"),bg="dark orange",fg="black")
		reset_btn.grid(row=0,column=3)

		btn_frame1=Frame(class_Empleado_frame,bd=2,relief=RIDGE,bg="White")
		btn_frame1.place(x=0,y=250,width=715,height=35)

		take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Capturar nuevo rostro",width=45,font=("book antiqua",10,"bold"),bg="dark orange",fg="black")
		take_photo_btn.grid(row=0,column=0)

		update_photo_btn=Button(btn_frame1,text="Actualizar rostro",width=45,font=("book antiqua",10,"bold"),bg="dark orange",fg="black")
		update_photo_btn.grid(row=0,column=1)


		# Marco de nivel derecho:
		Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Base de Datos",font=("book antiqua",12,"bold"),fg="black")
		Right_frame.place(x=750,y=10,width=720,height=580)

		img_right=Image.open(r'Images\bigsur.jpg')
		img_right=img_right.resize((720,130),Image.ANTIALIAS)
		self.photoimg_right=ImageTk.PhotoImage(img_right)

		f_lbl=Label(Right_frame,image=self.photoimg_right)
		f_lbl.place(x=5,y=0,width=720,height=130)

		# =============== Base Datos Empleados (Busqueda) =====================================
		Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Base De Datos Empleados",font=("book antiqua",12,"bold"),fg="black")
		Search_frame.place(x=5,y=135,width=710,height=70)

		search_label=Label(Search_frame,text="Buscar por:",font=("book antiqua",14,"bold"),bg="blue",fg="white")
		search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

		search_combo=ttk.Combobox(Search_frame,font=("book antiqua",13,"bold"),state="readonly",width=15)
		search_combo["values"]=("Seleccione","Roll No","Telefono No")
		search_combo.current(0)
		search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

		search_entry=ttk.Entry(Search_frame,width=15,font=("book antiqua",12,"bold"))
		search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

		search_btn=Button(Search_frame,text="Buscar",width=12,font=("book antiqua",12,"bold"),bg="dark orange",fg="black")
		search_btn.grid(row=0,column=3,padx=4)

		showAll_btn=Button(Search_frame,text="Mostrar Todo",width=12,font=("book antiqua",12,"bold"),bg="dark orange",fg="black")
		showAll_btn.grid(row=0,column=4,padx=4)

		# =============== Base Datos Empleados (Tabla) =====================================
		table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
		table_frame.place(x=5,y=210,width=710,height=350)

		scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
		scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

		self.empleados_table=ttk.Treeview(table_frame,column=("Departamento","CargoEmpleado","Ano","Contrato","IdEmpleado","NombreEmpleado","Subdepartamento","NumeroCargo","Genero","Fechadenacimiento","Correo","Telefono","Direccion","JefeDirecto","IA"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)

		scroll_x.config(command=self.empleados_table.xview)
		scroll_y.config(command=self.empleados_table.yview)


		self.empleados_table.heading("Departamento",text="Departamento")
		self.empleados_table.heading("CargoEmpleado",text="Cargo Empleado")
		self.empleados_table.heading("Ano",text="Año")
		self.empleados_table.heading("Contrato",text="Contrato")
		self.empleados_table.heading("IdEmpleado",text="Id Empleado")
		self.empleados_table.heading("NombreEmpleado",text="Nombre Empleado")
		self.empleados_table.heading("Subdepartamento",text="Subdepartamento")
		self.empleados_table.heading("NumeroCargo",text="Cargo No")
		self.empleados_table.heading("Genero",text="Genero")
		self.empleados_table.heading("Fechadenacimiento",text="Fecha de nacimiento")
		self.empleados_table.heading("Correo",text="Correo")
		self.empleados_table.heading("Telefono",text="Telefono")
		self.empleados_table.heading("Direccion",text="Dirección")
		self.empleados_table.heading("JefeDirecto",text="Jefe Directo")
		self.empleados_table.heading("IA",text="Imagen IA")
		self.empleados_table["show"]="headings"

		self.empleados_table.column("Departamento",width=100)
		self.empleados_table.column("CargoEmpleado",width=100)
		self.empleados_table.column("Ano",width=100)
		self.empleados_table.column("Contrato",width=100)
		self.empleados_table.column("IdEmpleado",width=100)
		self.empleados_table.column("NombreEmpleado",width=100)
		self.empleados_table.column("Subdepartamento",width=100)
		self.empleados_table.column("NumeroCargo",width=100)
		self.empleados_table.column("Genero",width=100)
		self.empleados_table.column("Fechadenacimiento",width=100)
		self.empleados_table.column("Correo",width=100)
		self.empleados_table.column("Telefono",width=100)
		self.empleados_table.column("Direccion",width=100)
		self.empleados_table.column("JefeDirecto",width=100)
		self.empleados_table.column("IA",width=100)

		self.empleados_table.pack(fill=BOTH,expand=1)
		self.empleados_table.bind("<ButtonRelease>",self.get_cursor)
		self.fetch_data()

	# =========================== Guardar de base de datos ==================================

	def add_data(self):
		if self.var_Departamento.get()=="Seleccione" or self.var_Nombre_Empleado.get()=="" or self.var_Id_Empleado.get()=="":
			messagebox.showerror("Error","Todos los campos son requeridos",parent=self.root)
		else:
			try:
				conn=mysql.connector.connect(host="localhost",port=3306,username="root",password="Melo@123",database="reconocimiento")
				my_cursor=conn.cursor()
				my_cursor.execute("insert into empleados values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
																			self.var_Departamento.get(),
																			self.var_Cargo_Empleado.get(),
																			self.var_Ano.get(),
																			self.var_Contrato.get(),
																			self.var_Id_Empleado.get(),
																			self.var_Nombre_Empleado.get(),
																			self.var_Subdepartamento.get(),
																			self.var_Cargo_No.get(),
																			self.var_Genero.get(),
																			self.var_nacimiento.get(),
																			self.var_Correo.get(),
																			self.var_Telefono.get(),
																			self.var_Direccion.get(),
																			self.var_Jefe_Directo.get(),
																			self.var_radio1.get()


																	))
				conn.commit()
				self.fetch_data()
				conn.close()
				messagebox.showinfo("Guardado","Empleado guardado con exito",parent=self.root)

			except Exception as es:
				messagebox.showerror("Error",f"Generado por :{str(es)}",parent=self.root)


	#======================================Obtener De Base de Datos====================================
	def fetch_data(self):
		conn = mysql.connector.connect(host="localhost", username="root", password="Melo@123",database="reconocimiento")
		my_cursor = conn.cursor()
		my_cursor.execute("select * from empleados")
		data = my_cursor.fetchall()

		if len(data)!=0:
			self.empleados_table.delete(*self.empleados_table.get_children())
			for i in data:
				self.empleados_table.insert("",END,values=i)
			conn.commit()
		conn.close()

	#==========================Obtener cursor ======================================================
	def get_cursor(self,event=""):
		cursor_focus = self.empleados_table.focus()
		content=self.empleados_table.item(cursor_focus)
		data=content["values"]

		self.var_Departamento.set(data[0]),
		self.var_Cargo_Empleado.set(data[1]),
		self.var_Ano.set(data[2]),
		self.var_Contrato.set(data[3]),
		self.var_Id_Empleado.set(data[4]),
		self.var_Nombre_Empleado.set(data[5]),
		self.var_Subdepartamento.set(data[6]),
		self.var_Cargo_No.set(data[7]),
		self.var_Genero.set(data[8]),
		self.var_nacimiento.set(data[9]),
		self.var_Correo.set(data[10]),
		self.var_Telefono.set(data[11]),
		self.var_Direccion.set(data[12]),
		self.var_Jefe_Directo.set(data[13]),
		self.var_radio1.set(data[14])

	#==================================Actualizar base de datos ===============================
	def update_data(self):
		if self.var_Departamento.get()=="Seleccione" or self.var_Nombre_Empleado.get()=="" or self.var_Id_Empleado.get()=="":
			messagebox.showerror("Error","Todos los campos son requeridos",parent=self.root)
		else:
			try:
				Upadate=messagebox.askyesno("Actualizar","¿Desea actualizar los datos del empleado?",parent=self.root)
				if Upadate>0:
					conn=mysql.connector.connect(host="localhost",username="root", password="Melo@123",database="reconocimiento")
					my_cursor = conn.cursor()
					my_cursor.execute("update empleados set Departamento=%s,CargoEmpleado=%s,Ano=%s,Contrato=%s,NombreEmpleado=%s,Subdepartamento=%s,NumeroCargo=%s,Genero=%s,Fechadenacimiento=%s,Correo=%s,Telefono=%s,Direccion=%s,JefeDirecto=%s,IA=%s where IdEmpleado=%s",(
						self.var_Departamento.get(),
						self.var_Cargo_Empleado.get(),
						self.var_Ano.get(),
						self.var_Contrato.get(),
						self.var_Nombre_Empleado.get(),
						self.var_Subdepartamento.get(),
						self.var_Cargo_No.get(),
						self.var_Genero.get(),
						self.var_nacimiento.get(),
						self.var_Correo.get(),
						self.var_Telefono.get(),
						self.var_Direccion.get(),
						self.var_Jefe_Directo.get(),
						self.var_radio1.get(),
						self.var_Id_Empleado.get()
						))
				else:
					if not Upadate:
						return
				conn.commit()
				self.fetch_data()
				conn.close()
				messagebox.showinfo("Guardado","Datos correctamente actualizados",parent=self.root)
			except Exception as es:
				messagebox.showerror("Error",f"Generado por :{str(es)}",parent=self.root)
#=============================================== Eliminar De la  Base de datos =================================================
	def delete_data(self):
		if self.var_Id_Empleado.get()=="":
			messagebox.showerror("Error", "Es requerido el ID de empleado",parent=self.root)
		else:
			try:
				delete=messagebox.askyesno("Eliminador de empleado", "¿Desea eliminar al empleado de la base de datos?",parent=self.root)
				if delete >0:
					conn=mysql.connector.connect(host="localhost",username="root", password="Melo@123",database="reconocimiento")
					my_cursor = conn.cursor()
					sql="delete from empleados where IdEmpleado=%s"
					val=(self.var_Id_Empleado.get(),)
					my_cursor.execute(sql,val)
				else:
					if not delete:
						return
				conn.commit()
				self.fetch_data()
				conn.close()
				messagebox.showinfo("Eliminar","Empleado eliminado correctamente de la base de datos", parent=self.root)
			except Exception as es:
				messagebox.showerror("Error",f"Generado por :{str(es)}",parent=self.root)

# ================================== Boton de Limpiar ======================================================================== #
	def reset_data(self):
		self.var_Departamento.set("Seleccione"),
		self.var_Cargo_Empleado.set("Seleccione"),
		self.var_Ano.set("Seleccione"),
		self.var_Contrato.set("Seleccione"),
		self.var_Id_Empleado.set(""),
		self.var_Nombre_Empleado.set(""),
		self.var_Subdepartamento.set("Seleccione"),
		self.var_Cargo_No.set(""),
		self.var_Genero.set("Masculino"),
		self.var_nacimiento.set(""),
		self.var_Correo.set(""),
		self.var_Telefono.set(""),
		self.var_Direccion.set(""),
		self.var_Jefe_Directo.set(""),
		self.var_radio1.set("")
#===================================== Generar conjunto de IA (En fotos) ========================================================#

	def  generate_dataset(self):
		if self.var_Departamento.get()=="Seleccione" or self.var_Nombre_Empleado.get()=="" or self.var_Id_Empleado.get()=="":
			messagebox.showerror("Error","Todos los campos son requeridos",parent=self.root)
		else:
			try:
				conn=mysql.connector.connect(host="localhost",username="root", password="Melo@123",database="reconocimiento")
				my_cursor = conn.cursor()
				my_cursor.execute("select * from empleados")
				myresult=my_cursor.fetchall()
				id=0
				for x in myresult:
					id+=1
				my_cursor.execute("update empleados set Departamento=%s,CargoEmpleado=%s,Ano=%s,Contrato=%s,NombreEmpleado=%s,Subdepartamento=%s,NumeroCargo=%s,Genero=%s,Fechadenacimiento=%s,Correo=%s,Telefono=%s,Direccion=%s,JefeDirecto=%s,IA=%s where IdEmpleado=%s",(
					self.var_Departamento.get(),
					self.var_Cargo_Empleado.get(),
					self.var_Ano.get(),
					self.var_Contrato.get(),
					self.var_Nombre_Empleado.get(),
					self.var_Subdepartamento.get(),
					self.var_Cargo_No.get(),
					self.var_Genero.get(),
					self.var_nacimiento.get(),
					self.var_Correo.get(),
					self.var_Telefono.get(),
					self.var_Direccion.get(),
					self.var_Jefe_Directo.get(),
					self.var_radio1.get(),
					self.var_Id_Empleado.get()==id+1
					))
				conn.commit(conn)
				self.fetch_data()
				self.reset_data()
				conn.close()

				# =================  Algoritmo para detectar rostro frontal desde open cv =================
				clasificador_facial=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

				def face_cropped(img):
					gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
					faces=clasificador_facial.detectMultiScale(gray,1.3,5)
					# Scaling Factor=1.3
					#Minimun Neigbor=5

					for (x,y,w,y,h) in faces:
						face_cropped=img[y:y+h,x:x+w]
						return face_cropped

				cap=cv2.VideoCapture(0)
				img_id=0
				while True:
					ret,my_frame=cap.read()
					if face_cropped(my_frame) is not None:
						img_id+=1
					face=cv2,resize(face_cropped(my_frame),(450,450))
					face=cv2.cvtColor(face,cv2.COLOR_BGRA2GRAY)
					file_name_path="coleccion_IA/user."+str(id)+"."+str(img_id)+".jpg"
					cv2.imwrite(file_name_path,face)
					cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
					cv2.imshow("Reconociendo tu rostro", face)

					if cv2.waitKey(1)==13 or int (img_id)==200:
						break
				cap.release()
				cv2.destroyAllWindows()
				messagebox.showinfo("Resultado","Datos generados con exito.")
			except Exception as es:
				messagebox.showerror("Error",f"Generado por :{str(es)}",parent=self.root)


if __name__ == '__main__':
	root=Tk()
	obj=Empleados(root)
	root.mainloop()
