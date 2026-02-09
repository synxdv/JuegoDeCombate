import tkinter as tk
from tkinter import messagebox
import random
from PIL import ImageTk, Image

# Estadisticas personaje
vida = 100
damage = 10
damage_enemigo = random.randint(10,50)
vida_enemigo = random.randint(50,100) 

    

def info_personaje():

    def mostrar_info():
        global vida,damage

        messagebox.showinfo(f"Info", f"Vida {vida} \n Daño {damage}")
    

    ventana = tk.Toplevel()
    ventana.title("Informacion sobre tu personaje")
    ventana.geometry("300x300")

    tk.Button(ventana, text="Mostrar info",command=mostrar_info , bg="red").pack(pady=5)

    ventana.mainloop()

def como_jugar():
    ventana = tk.Toplevel()
    ventana.title("Ayuda")
    ventana.geometry("400x400")

    ayuda_label = tk.Label(ventana, text="Para jugar es sencillo, solo debes seleccionar el apartado llamado (batalla) " \
    "\n El combate es por turnos, no es dificil de entender. La vida y el daño del enemigo es completamente aleatoria \n " \
    "Por ende nunca pelearas contra el mismo.", font=("Arial", 12))
    ayuda_label.pack(pady=5)

    ventana.mainloop()

        
def pelea():

    # Variables. Llamando a las globales 

    global vida_enemigo,vida,vida_enemigo

    

    def atacar():
        global damage,vida_enemigo,vida
   
        
        
        vida_enemigo -= damage
        messagebox.showinfo("Daño hecho", f"Le has hecho {damage} de daño al enemigo...")
        label.config(text=f"Tu vida {vida}. \n Vida del enemigo {vida_enemigo}")

        if vida_enemigo <= 0:
            messagebox.showinfo("GG","HAS GANADO!! Lograste derrotar a tu enemigo")
            ventana.destroy()
        else:  
            siguiente_turno()

    def siguiente_turno():
        global vida,damage_enemigo,vida_enemigo
 

        vida -= damage_enemigo
        messagebox.showinfo("Daño recibido", f"El enemigo te ataco y te quito {damage_enemigo} de vida..")
        label.config(text=f"Tu vida {vida}. \n Vida del enemigo {vida_enemigo}")

        if vida <= 0:
            messagebox.showinfo("Has muerto.", "Tu vida llego a 0")
            ventana.destroy()


    # Cargar la imagen
    img_golpe = Image.open("pegar.png")

    # Redimensionarla
    golpe_redimensionado = img_golpe.resize((32,32))




    ventana = tk.Toplevel()
    ventana.title("Combate!")
    ventana.geometry("400x400")

    # Cargarlas para que Tk las reconozca

    img_general = ImageTk.PhotoImage(golpe_redimensionado)

    label = tk.Label(ventana, text=f"Tu vida {vida}. \n Vida del enemigo {vida_enemigo}", font=("Arial", 12))
    label.pack(pady=5)

    # Imagen de golpeo


    # Botones

    tk.Button(ventana, text="ATACAR!", command=atacar, bg="red", image=img_general, compound="left").pack(pady=5)

    ventana.mainloop()


def entrenar():

    global vida, damage

    def entrenamiento():
        global vida,damage

        vida += random.randint(10,20)
        damage += random.randint(10,20)
        messagebox.showinfo("GG", f"Tu vida ha subido a {vida} y tu Daño a {damage}")
    
    ventana = tk.Toplevel()
    ventana.title("ENTRENAMIENTO")
    ventana.geometry("400x300")

    label_mensaje = tk.Label(ventana, text="Presiona el boton para entrenar", font=("Arial", 13))
    label_mensaje.pack(pady=5)

    tk.Button(ventana, text="Entrenar", command=entrenamiento ,bg="Blue").pack(pady=5)

