import tkinter as tk  


def registrar_entradas():  
    nombre=""
    root=tk.Tk() 
    root.title("Registrar Entradas") 
    ventana=tk.Frame(root) 
    ventana.config(width=300,height=400,bg="blue")  
    
    lbnombre=tk.Label(ventana,text="Nombre") 
    lbnombre.place(x=20,y=20)  

    etnombre=tk.Entry(ventana,textvariable=nombre) 
    etnombre.place(x=20,y=37) 
    



    ventana.pack() 
    root.mainloop()