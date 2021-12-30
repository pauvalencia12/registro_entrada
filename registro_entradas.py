import tkinter as tk  


def registrar_entradas():  
    nombre=""
    documento=""
    hora=""
    observaciones=""

    root=tk.Tk() 
    root.title("Registrar Entradas") 
    ventana=tk.Frame(root) 
    ventana.config(width=300,height=400,bg="pink")  
    
    lbnombre=tk.Label(ventana,text="Nombre") 
    lbnombre.place(x=20,y=20)  

    etnombre=tk.Entry(ventana,textvariable=nombre) 
    etnombre.place(x=20,y=37) 
    

    lbdocumento=tk.Label(ventana,text="documento")
    lbdocumento.place(x=20,y=77)

    etdocumento=tk.Entry(ventana,text="documento")
    etdocumento.place(x=20,y=95)

    lbhora=tk.Label(ventana,text="hora")
    lbhora.place(x=20,y=134)

    ethora=tk.Entry(ventana,text="hora")
    ethora.place(x=20,y=153)

    lbobservaciones=tk.Label(ventana,text="observaciones")
    lbobservaciones.place(x=20,y=187)

    etobservaciones=tk.Text(ventana,height=10,width=20)
    etobservaciones.place(x=20,y=210)

    btnregistrar=tk.Button(ventana,text="registrar entrada")
    btnregistrar.place(x=200,y=330)




    ventana.pack() 
    root.mainloop()