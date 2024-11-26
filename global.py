import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuración de la aplicación
st.title("Resolución de Ejercicios de Optimización")
st.write("Selecciona el ejercicio que deseas visualizar y analizar.")

# Botones para seleccionar ejercicios
exercise = None
if st.button("Ejercicio 1"):
    exercise = 1
if st.button("Ejercicio 2"):
    exercise = 2
if st.button("Ejercicio 3"):
    exercise = 3
if st.button("Ejercicio 4"):
    exercise = 4
if st.button("Ejercicio 5"):
    exercise = 5

# Ejercicio 1
if exercise == 1:
    st.header("Ejercicio 1: Verificar si x = 2 y x = 0 son minimizadores globales o locales para f(x) = x^2 - 4x + 5")
    st.write("""
    1. Calcular la derivada de f(x):  
       f'(x) = 2x - 4
    
    2. Encontrar los puntos críticos:  
       f'(x) = 0 → x = 2
    
    3. Evaluar f(x) en x = 2:  
       f(2) = (2)^2 - 4(2) + 5 = 1
    
    4. Evaluar f(x) en x = 0:  
       f(0) = (0)^2 - 4(0) + 5 = 5
    
    Conclusión:  
    - x = 2 es un mínimo global.  
    - x = 0 no es un mínimo global ni local.
    """)

    # Gráfica
    def f1(x):
        return x**2 - 4*x + 5

    x_vals = np.linspace(-1, 5, 500)
    y_vals = f1(x_vals)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x_vals, y_vals, label="f(x) = x^2 - 4x + 5")
    ax.scatter(2, f1(2), color='red', label="Mínimo Global (x=2)")
    ax.legend(loc='upper left', frameon=True)
    ax.set_title("Gráfica de f(x) = x^2 - 4x + 5")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid()
    st.pyplot(fig)

# Ejercicio 2
if exercise == 2:
    st.header("Ejercicio 2: Determinar si f(x) = |x| tiene un mínimo global o local en x = 0")
    st.write("""
    1. La función f(x) = |x| representa la distancia absoluta desde x al origen.  
    2. Evaluar f(x) en x = 0:  
       f(0) = |0| = 0
    
    Conclusión:  
    x = 0 es un mínimo global de f(x).
    """)

    # Gráfica
    def f2(x):
        return np.abs(x)

    x_vals = np.linspace(-2, 2, 500)
    y_vals = f2(x_vals)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x_vals, y_vals, label="f(x) = |x|")
    ax.scatter(0, f2(0), color='red', label="Mínimo Global (x=0)")
    ax.legend(loc='upper right', frameon=True)
    ax.set_title("Gráfica de f(x) = |x|")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid()
    st.pyplot(fig)

# Ejercicio 3
if exercise == 3:
    st.header("Ejercicio 3: Explicar por qué f(x) = sin(x) en [0, π] tiene un mínimo global")
    st.write("""
    1. La función es continua en el intervalo cerrado [0, π].  
    2. En [0, π], sin(x) decrece y alcanza su mínimo en x = π.  
       En este punto, sin(π) = 0.
    
    Conclusión:  
    El mínimo global ocurre en x = π, donde sin(x) = 0.
    """)

    # Gráfica
    def f3(x):
        return np.sin(x)

    x_vals = np.linspace(0, np.pi, 500)
    y_vals = f3(x_vals)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x_vals, y_vals, label="f(x) = sin(x)")
    ax.scatter(np.pi, f3(np.pi), color='red', label="Mínimo Global (x=π)")
    ax.legend(loc='lower right', frameon=True)
    ax.set_title("Gráfica de f(x) = sin(x) en [0, π]")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid()
    st.pyplot(fig)

# Ejercicio 4
if exercise == 4:
    st.header("Ejercicio 4: Encontrar el mínimo global de f(x, y) = x^2 + y^2 con x^2 + y^2 ≤ 1")
    st.write("""
    1. La función f(x, y) = x^2 + y^2 mide la distancia al origen al cuadrado.  
    2. El mínimo global ocurre en (x, y) = (0, 0).
    """)

    # Gráfica
    theta = np.linspace(0, 2*np.pi, 500)
    x_circle = np.cos(theta)
    y_circle = np.sin(theta)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.fill(x_circle, y_circle, alpha=0.2, label="x^2 + y^2 ≤ 1")
    ax.scatter(0, 0, color='red', label="Mínimo Global (0, 0)")
    ax.legend(loc='upper left', frameon=True)
    ax.set_title("Gráfica de la restricción y el mínimo")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.axis('equal')
    ax.grid()
    st.pyplot(fig)

# Ejercicio 5
if exercise == 5:
    st.header("Ejercicio 5: Diseñar un ejemplo donde un mínimo global no sea único")
    st.write("""
    1. Ejemplo: f(x) = x^2 en [-1, 1].  
    2. Los mínimos globales ocurren en x = -1 y x = 1, ambos con f(x) = 1.
    """)

    # Gráfica
    def f5(x):
        return x**2

    x_vals = np.linspace(-1, 1, 500)
    y_vals = f5(x_vals)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x_vals, y_vals, label="f(x) = x^2")
    ax.scatter([-1, 1], [f5(-1), f5(1)], color='red', label="Mínimos Globales (x=-1, x=1)")
    ax.legend(loc='upper left', frameon=True)
    ax.set_title("Gráfica de f(x) = x^2 en [-1, 1]")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid()
    st.pyplot(fig)
