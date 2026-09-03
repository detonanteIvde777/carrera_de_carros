from tkinter import *
import random

# ------------------ variables globales ------------------
BASE = 800
ALTURA = 400
x_carro1 = 50
y_carro1 = 100
x_carro2 = 50
y_carro2 = 250
tamano_carro = 60
META = 700
juego_activo = True

# ------------------ funciones ------------------

def mover_derecha(carro):
    global x_carro1, x_carro2
    if carro == 1:
        if x_carro1 < BASE:
            x_carro1 = x_carro1 + random.randint(1, 10)
            canvas.coords(carro1_cuerpo, x_carro1, y_carro1, x_carro1+tamano_carro, y_carro1+30)
            canvas.coords(carro1_rueda1, x_carro1+10, y_carro1+30, x_carro1+20, y_carro1+40)
            canvas.coords(carro1_rueda2, x_carro1+40, y_carro1+30, x_carro1+50, y_carro1+40)
    else:
        if x_carro2 < BASE:
            x_carro2 = x_carro2 + random.randint(1, 10)
            canvas.coords(carro2_cuerpo, x_carro2, y_carro2, x_carro2+tamano_carro, y_carro2+30)
            canvas.coords(carro2_rueda1, x_carro2+10, y_carro2+30, x_carro2+20, y_carro2+40)
            canvas.coords(carro2_rueda2, x_carro2+40, y_carro2+30, x_carro2+50, y_carro2+40)

def iniciar_carrera():
    global juego_activo
    if juego_activo:
        mover_derecha(1)
        mover_derecha(2)
        
        # verificar ganador
        if x_carro1 >= META:
            juego_activo = False
            etiqueta_ganador.config(text="¡GANÓ CARRO ROJO!", fg="red")
        elif x_carro2 >= META:
            juego_activo = False
            etiqueta_ganador.config(text="¡GANÓ CARRO AZUL!", fg="blue")
        else:
            ventana_principal.after(100, iniciar_carrera)

def reiniciar():
    global x_carro1, x_carro2, juego_activo
    x_carro1 = 50
    x_carro2 = 50
    juego_activo = True
    etiqueta_ganador.config(text="")
    iniciar_carrera()

# ------------------ ventana principal ------------------
ventana_principal = Tk()
ventana_principal.title("Tema B - Competencia de Carritos")
ventana_principal.geometry(f"{BASE}x{ALTURA+100}")
ventana_principal.resizable(False, False)

frame_graficacion = Frame(ventana_principal, width=BASE, height=ALTURA, bg="gray")
frame_graficacion.place(x=0, y=0)

canvas = Canvas(frame_graficacion, width=BASE, height=ALTURA, bg="lightgreen")
canvas.place(x=0, y=0)

# carretera
canvas.create_rectangle(0, 80, BASE, 160, fill="gray", outline="")
canvas.create_rectangle(0, 230, BASE, 310, fill="gray", outline="")
# linea meta
canvas.create_line(META+60, 80, META+60, 310, fill="white", width=5, dash=(10,5))

# carro 1 - con objetos basicos del Canvas (cuadrados, circulos)
carro1_cuerpo = canvas.create_rectangle(x_carro1, y_carro1, x_carro1+tamano_carro, y_carro1+30, fill="red")
carro1_rueda1 = canvas.create_oval(x_carro1+10, y_carro1+30, x_carro1+20, y_carro1+40, fill="black")
carro1_rueda2 = canvas.create_oval(x_carro1+40, y_carro1+30, x_carro1+50, y_carro1+40, fill="black")

# carro 2
carro2_cuerpo = canvas.create_rectangle(x_carro2, y_carro2, x_carro2+tamano_carro, y_carro2+30, fill="blue")
carro2_rueda1 = canvas.create_oval(x_carro2+10, y_carro2+30, x_carro2+20, y_carro2+40, fill="black")
carro2_rueda2 = canvas.create_oval(x_carro2+40, y_carro2+30, x_carro2+50, y_carro2+40, fill="black")

# frame controles
frame_controles = Frame(ventana_principal, width=BASE, height=100)
frame_controles.place(x=0, y=ALTURA)

btn_iniciar = Button(frame_controles, text="INICIAR CARRERA", command=iniciar_carrera, bg="green", fg="white", width=20, height=2)
btn_iniciar.place(x=100, y=20)

btn_reiniciar = Button(frame_controles, text="REINICIAR", command=reiniciar, bg="orange", width=20, height=2)
btn_reiniciar.place(x=500, y=20)

etiqueta_ganador = Label(frame_controles, text="", font=("Arial", 16, "bold"))
etiqueta_ganador.place(x=300, y=60)

ventana_principal.mainloop()