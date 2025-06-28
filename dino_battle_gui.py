
import tkinter as tk
import random

# Lista de dinosaurios y armas
dinosaurios = ["T-Rex", "Triceratops", "Velociraptor", "Stegosaurus"]
armas = [
    "espada", "lanza", "ballesta", "mazo", "hacha",
    "mosquete", "pistola de chispa", "arcabuz", "cañón portátil"
]

# Inicializar puntuaciones
puntuacion = {"Dino 1": 0, "Dino 2": 0}
round_actual = 1

# Función para simular un round
def pelear():
    global round_actual
    if puntuacion["Dino 1"] == 2 or puntuacion["Dino 2"] == 2:
        return

    dino1 = random.choice(dinosaurios)
    dino2 = random.choice(dinosaurios)
    arma1 = random.choice(armas)
    arma2 = random.choice(armas)

    resultado_texto = f"Round {round_actual}:\n"
    resultado_texto += f"{dino1} ataca con {arma1}\n"
    resultado_texto += f"{dino2} ataca con {arma2}\n"

    ganador = random.choice(["Dino 1", "Dino 2"])
    puntuacion[ganador] += 1
    resultado_texto += f"🏆 Gana el round: {ganador}!\n"

    if puntuacion["Dino 1"] == 2 or puntuacion["Dino 2"] == 2:
        resultado_texto += f"\n🎉 ¡{ganador} gana la batalla 2 de 3 rounds!"

    resultado_label.config(text=resultado_texto)
    round_actual += 1

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Batalla de Dinosaurios")
ventana.geometry("400x300")

titulo = tk.Label(ventana, text="🦖 Batalla de Dinosaurios 🦕", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

boton_pelear = tk.Button(ventana, text="Iniciar Round", command=pelear, font=("Arial", 12))
boton_pelear.pack(pady=10)

resultado_label = tk.Label(ventana, text="", font=("Arial", 12), justify="left")
resultado_label.pack(pady=10)

ventana.mainloop()
