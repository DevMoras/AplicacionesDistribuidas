import json

import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# Función para hacer la llamada al servicio web y obtener el resultado
def llamar_servicio(operacion, numero1, numero2):
    url = f"http://localhost:8080/ApiRestWeb/webresources/operaciones/{operacion}"
    params = {'num': numero1, 'num1': numero1, 'num2': numero2}

    try:
        response = requests.get(url, params=params)
        response_json = response.json()

        # Imprimir la respuesta para depuración
        print("Respuesta del servidor:", response_json)

        # Verificar si la respuesta es un objeto JSON y contiene la clave 'resultado'
        if isinstance(response_json, dict) and 'resultado' in response_json:
            resultado = response_json['resultado']
            return resultado
        else:
            # Si no es un objeto JSON válido o no contiene 'resultado', simplemente devolver la respuesta tal cual
            return response_json
    except json.JSONDecodeError as e:
        messagebox.showerror("Error", f"Error al decodificar JSON: {e}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error de conexión", f"No se pudo establecer conexión con el servidor: {e}")


# Función para manejar el evento del botón "Calcular"
def calcular():
    operacion = operaciones_combobox.get()
    num1 = float(numero1_entry.get())
    num2 = float(numero2_entry.get())

    resultado = llamar_servicio(operacion, num1, num2)
    if resultado is not None:
        resultado_label.config(text=f"Resultado: {resultado}")


# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Calculadora")

tk.Label(root, text="Operación:").grid(row=0, column=0, padx=5, pady=5)
operaciones_combobox = tk.ttk.Combobox(root,
                                       values=["suma", "resta", "multiplicacion", "division", "potencia", "modulo",
                                               "factorial", "raizCuadrada", "logaritmo", "sin", "cos", "tan", "e",
                                               "sinh", "cosh", "tanh"])
operaciones_combobox.grid(row=0, column=1, padx=5, pady=5)
operaciones_combobox.current(0)

tk.Label(root, text="Número 1:").grid(row=1, column=0, padx=5, pady=5)
numero1_entry = tk.Entry(root)
numero1_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Número 2:").grid(row=2, column=0, padx=5, pady=5)
numero2_entry = tk.Entry(root)
numero2_entry.grid(row=2, column=1, padx=5, pady=5)

calcular_button = tk.Button(root, text="Calcular", command=calcular)
calcular_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

resultado_label = tk.Label(root, text="")
resultado_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
