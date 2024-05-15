import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from suds.client import Client
import mysql.connector

# URL del archivo WSDL del servicio web
wsdl_url = 'http://192.168.218.199:8080/operacion/wsoperaciones?wsdl'
client = Client(wsdl_url)

# Conexión a la base de datos MySQL
db_host = '192.168.218.199'
db_port = '3306'
db_user = 'root'
db_password = ''
db_name = 'soap'

db_connection = mysql.connector.connect(
    host=db_host,
    port=db_port,
    user=db_user,
    password=db_password,
    database=db_name
)


def guardar_resultado(num1, num2, resultado, operacion):
    cursor = db_connection.cursor()
    sql = "INSERT INTO resultados (num1, num2, resultado, operacion) VALUES (%s, %s, %s, %s)"
    val = (num1, num2, resultado, operacion)
    cursor.execute(sql, val)
    db_connection.commit()
    cursor.close()


def obtener_operaciones():
    cursor = db_connection.cursor()
    cursor.execute("SELECT num1, operacion, num2, resultado FROM resultados")
    operaciones = cursor.fetchall()
    cursor.close()
    return operaciones


def actualizar():
    # Limpiar la tabla
    for row in treeview.get_children():
        treeview.delete(row)

    # Obtener operaciones desde la base de datos
    operaciones = obtener_operaciones()

    # Insertar operaciones en la tabla
    for operacion in operaciones:
        treeview.insert("", "end", values=operacion)



def sumar():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        result = client.service.sumar(num1, num2)
        resultado_entry.config(state="normal")
        resultado_entry.delete(0, "end")
        resultado_entry.insert("end", result)
        resultado_entry.config(state="readonly")
        guardar_resultado(num1, num2, result, "+")
        actualizar()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números enteros válidos.")


def restar():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        result = client.service.restar(num1, num2)
        resultado_entry.config(state="normal")
        resultado_entry.delete(0, "end")
        resultado_entry.insert("end", result)
        resultado_entry.config(state="readonly")
        guardar_resultado(num1, num2, result, "-")
        actualizar()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números enteros válidos.")


def multiplicar():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        result = client.service.multiplicar(num1, num2)
        resultado_entry.config(state="normal")
        resultado_entry.delete(0, "end")
        resultado_entry.insert("end", result)
        resultado_entry.config(state="readonly")
        guardar_resultado(num1, num2, result, "*")
        actualizar()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números enteros válidos.")


def limpiar():
    entry_num1.delete(0, "end")
    entry_num2.delete(0, "end")
    resultado_entry.config(state="normal")
    resultado_entry.delete(0, "end")
    resultado_entry.config(state="readonly")


# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")
root.geometry("600x400")

# Evitar que la ventana sea redimensionable
root.resizable(width=False, height=False)

# Crear y posicionar los widgets
label_num1 = tk.Label(root, text="Número 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(root, text="Número 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

button_limpiar = tk.Button(root, text="Limpiar", command=limpiar, width=8)
button_limpiar.grid(row=1, column=2, padx=(10, 5), pady=5)

label_result = tk.Label(root, text="Resultado:")
label_result.grid(row=2, column=0, padx=10, pady=5)

resultado_entry = tk.Entry(root, state="readonly", width=20)
resultado_entry.grid(row=2, column=1, padx=5, pady=5)

button_sumar = tk.Button(root, text="Sumar", command=sumar, width=8)
button_sumar.grid(row=3, column=0, padx=(10, 5), pady=5)

button_restar = tk.Button(root, text="Restar", command=restar, width=8)
button_restar.grid(row=3, column=1, padx=5, pady=5)

button_multiplicar = tk.Button(root, text="Multiplicar", command=multiplicar, width=8)
button_multiplicar.grid(row=3, column=2, padx=(5, 10), pady=5)

# Configurar las columnas para que sean más estrechas
root.grid_columnconfigure(0, weight=1, minsize=200)
root.grid_columnconfigure(1, weight=1, minsize=200)
root.grid_columnconfigure(2, weight=1, minsize=200)

# Crear tabla para mostrar operaciones
treeview = ttk.Treeview(root, columns=("Número 1", "Operación", "Número 2", "Resultado"), show="headings")
treeview.grid(row=4, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")

treeview.heading("Operación", text="Operación")
treeview.heading("Número 1", text="Número 1")
treeview.heading("Número 2", text="Número 2")
treeview.heading("Resultado", text="Resultado")

# Ajustar tamaño de las columnas
treeview.column("Número 1", width=50, anchor="center")
treeview.column("Operación", width=50, anchor="center")
treeview.column("Número 2", width=50, anchor="center")
treeview.column("Resultado", width=50, anchor="center")


# Actualizar tabla con las operaciones existentes
actualizar()

# Ejecutar la aplicación
root.mainloop()