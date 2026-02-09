from combate import info_personaje,pelea, como_jugar, entrenar
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Cargar las imagenenes


img_general = Image.open("home.png")
img_cuchillo = Image.open("cuchillo.png")
img_help = Image.open("help.png")
img_entrenamiento = Image.open("entrenamiento.png")

# Redimensionar las imagenes

img_redimensionada = img_general.resize((100,100))
cuchillo_redimensionado = img_cuchillo.resize((32,32))
help_redimensionado = img_help.resize((32,32))
entrenamiento_redimensionado = img_entrenamiento.resize((32,32))

# Configurar ventana

ventana = tk.Tk()
ventana.title("Juego de Batalla - Inicio")
ventana.geometry("500x500")

# Cargar las imagenes para que tk las reconozca
imagen_general = ImageTk.PhotoImage(img_redimensionada)
cuchillo_general = ImageTk.PhotoImage(cuchillo_redimensionado)
help_general = ImageTk.PhotoImage(help_redimensionado)
entrenamiento_general = ImageTk.PhotoImage(entrenamiento_redimensionado)

# Label principal
label_info = tk.Label(ventana, text="Bienvenido. \n Seleccione una de estas opciones", font=("Arial", 10))
label_info.pack(pady=5)




# Label de la imagen
label_imagen = tk.Label(ventana, image=imagen_general, compound="top")
label_imagen.pack(pady=10)

# Botones

tk.Button(ventana, text="Info PJ", command=info_personaje, bg="green").pack(pady=5)
tk.Button(ventana, text="Combate", command= pelea, bg="green", image=cuchillo_general, compound="left").pack(pady=5)
tk.Button(ventana, text="Ayuda", command=como_jugar, bg="green", image=help_general, compound="left" ).pack(pady=5)
tk.Button(ventana, text="Entrenamiento", command=entrenar, bg="green", image=entrenamiento_general, compound="left").pack(pady=5)


ventana.mainloop()