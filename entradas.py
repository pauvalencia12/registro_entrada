import  tkinter as tk  
from registro_entradas import registrar_entradas
from registro_salidas import registrar_salidas



def eventos(event): 
    boton_presionado=event.widget.cget("text") 
    if(boton_presionado=="Registrar Entradas"):  
        registrar_entradas()
        
    elif (boton_presionado=="Registrar Salidas"): 
        registrar_salidas()



#ventana principal  

root=tk.Tk()
root.title("Calculadora Sistemas Numericos")
ventana=tk.Frame(root) 
ventana.config(width=300,height=200,bg="gray") 


btentrada=tk.Button(ventana,text="Registrar Entradas")  
btentrada.bind('<Button-1>',eventos)
btentrada.place(x=40,y=70,width=200)  

btsalida=tk.Button(ventana,text="Registrar Salidas") 
btsalida.bind('<Button-1>',eventos)
btsalida.place(x=40,y=120,width=200) 








#fin ventana principal   




ventana.pack()
root.mainloop()