import tkinter as tk  


def registrar_salidas(): 

    nombre=""
    documento="" 
    hora_salida="" 
    observaciones=""

    root=tk.Tk() 
    root.title("Registrar Salidas") 

    ventana=tk.Frame(root) 
    ventana.config(width=300,height=400,bg="pink")  

    lbnombre=tk.Label(ventana,text="Nombre") 
    lbnombre.place(x=20,y=20) 

    etnombre=tk.Entry(ventana,textvariable=nombre) 
    etnombre.place(x=20,y=37) 

    lbdocumento=tk.Label(ventana,text="Documento ") 
    lbdocumento.place(x=20,y=77)   

    etdocumento=tk.Entry(ventana,textvariable=documento) 
    etdocumento.place(x=20,y=95)


    lbhora=tk.Label(ventana,text="Hora de salida") 
    lbhora.place(x=20,y=134)  

    ethora=tk.Entry(ventana,textvariable=hora_salida) 
    ethora.place(x=20,y=153) 


    lbobservaciones=tk.Label(ventana,text="Observaciones") 
    lbobservaciones.place(x=20,y=187)  

    etobservaciones=tk.Text(ventana,height=10,width=20) 
    etobservaciones.place(x=20,y=210) 

    btnregistrar=tk.Button(ventana,text="Registar Salida") 
    btnregistrar.place(x=20,y=330)


    








    ventana.pack() 
    root.mainloop()
