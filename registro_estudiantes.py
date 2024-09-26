import tkinter as tk
from tkinter import messagebox

# Función para registrar al estudiante
def registrar_estudiante():
    # Obtener los datos ingresados
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()
    clase = entry_clase.get()
    seccion = entry_seccion.get()
    estado = var_estado.get()
    materias = []
    if optativa1.get(): materias.append("Matemáticas")
    if optativa2.get(): materias.append("Ciencias")
    if optativa3.get(): materias.append("Arte")
    comentarios = text_comentarios.get("1.0", tk.END).strip()
    nivel_escolar = nivel_var.get()
    
    # Mostrar los datos en la consola de VS Code
    print(f"Nombre: {nombre} {apellido}, Edad: {edad}, Clase: {clase}, Sección: {seccion}")
    print(f"Estado de inscripción: {estado}")
    print(f"Materias Optativas: {', '.join(materias)}")
    print(f"Nivel Escolar: {nivel_escolar}")
    print(f"Comentarios: {comentarios}")
    
    messagebox.showinfo("Registro", "Estudiante registrado correctamente")

# Función para limpiar el formulario
def limpiar_formulario():
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_clase.delete(0, tk.END)
    entry_seccion.delete(0, tk.END)
    var_estado.set(None)
    optativa1.set(False)
    optativa2.set(False)
    optativa3.set(False)
    text_comentarios.delete("1.0", tk.END)
    nivel_var.set("")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Registro de Estudiantes")

# Frame para los datos personales
frame_personal = tk.Frame(ventana)
frame_personal.pack(pady=10)

tk.Label(frame_personal, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(frame_personal)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_personal, text="Apellido:").grid(row=1, column=0, padx=5, pady=5)
entry_apellido = tk.Entry(frame_personal)
entry_apellido.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_personal, text="Edad:").grid(row=2, column=0, padx=5, pady=5)
entry_edad = tk.Entry(frame_personal)
entry_edad.grid(row=2, column=1, padx=5, pady=5)

# Frame para los detalles académicos
frame_academico = tk.Frame(ventana)
frame_academico.pack(pady=10)

tk.Label(frame_academico, text="Clase:").grid(row=0, column=0, padx=5, pady=5)
entry_clase = tk.Entry(frame_academico)
entry_clase.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_academico, text="Sección:").grid(row=1, column=0, padx=5, pady=5)
entry_seccion = tk.Entry(frame_academico)
entry_seccion.grid(row=1, column=1, padx=5, pady=5)

# Frame para el estado de inscripción
frame_inscripcion = tk.Frame(ventana)
frame_inscripcion.pack(pady=10)

var_estado = tk.StringVar()
var_estado.set(None)

tk.Label(frame_inscripcion, text="Estado de inscripción:").pack(anchor=tk.W)
tk.Radiobutton(frame_inscripcion, text="Inscrito", variable=var_estado, value="Inscrito").pack(anchor=tk.W)
tk.Radiobutton(frame_inscripcion, text="No Inscrito", variable=var_estado, value="No Inscrito").pack(anchor=tk.W)

# Frame para materias optativas
frame_optativas = tk.Frame(ventana)
frame_optativas.pack(pady=10)

tk.Label(frame_optativas, text="Materias Optativas:").pack(anchor=tk.W)
optativa1 = tk.BooleanVar()
optativa2 = tk.BooleanVar()
optativa3 = tk.BooleanVar()
tk.Checkbutton(frame_optativas, text="Matemáticas", variable=optativa1).pack(anchor=tk.W)
tk.Checkbutton(frame_optativas, text="Ciencias", variable=optativa2).pack(anchor=tk.W)
tk.Checkbutton(frame_optativas, text="Arte", variable=optativa3).pack(anchor=tk.W)

# Frame para comentarios adicionales
frame_comentarios = tk.Frame(ventana)
frame_comentarios.pack(pady=10)

tk.Label(frame_comentarios, text="Comentarios:").pack(anchor=tk.W)
text_comentarios = tk.Text(frame_comentarios, height=4, width=40)
text_comentarios.pack(padx=5, pady=5)

# Menú desplegable para nivel escolar
nivel_var = tk.StringVar()
nivel_var.set("Primaria")

tk.Label(ventana, text="Nivel Escolar:").pack(pady=5)
menu_nivel = tk.OptionMenu(ventana, nivel_var, "Primaria", "Secundaria")
menu_nivel.pack(pady=5)

# Botones de acción
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=20)

tk.Button(frame_botones, text="Registrar Estudiante", command=registrar_estudiante).pack(side=tk.LEFT, padx=10)
tk.Button(frame_botones, text="Limpiar", command=limpiar_formulario).pack(side=tk.LEFT, padx=10)

ventana.mainloop()
