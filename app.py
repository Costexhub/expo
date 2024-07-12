import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Funciones exponenciales")
st.markdown("""
Una función exponencial representa la relación entre una entrada y una salida, donde usamos multiplicaciones repetidas en un valor inicial para obtener la salida para cualquier entrada dada. Las funciones exponenciales pueden crecer o decaer muy rápidamente.

La ecuación general de una función exponencial es de la forma:

$$
y = b^x
$$

Donde:

I) b: Es la base de la función exponencial. Debe ser un número real mayor que 0 y distinto de 1. El valor de la base determina si la función es creciente o decreciente:

Si b es > 1, la función es creciente.

Si b se encuentra entre 0 y 1, la función es decreciente.

II) x: Es el exponente de la función exponencial. Debe ser un número real mayor que 0.

III) y: Es el valor de la función exponencial para la entrada x.

IV) k: Tambien existe un valor k que modifica a la funcion ya sea multiplicando, sumando o restando.








""")

st.subheader("¿Como se grafican?")

st.markdown("""
Para graficar estas funciones debemos ingresarle valores a x en la funcion dada, para asi hallar los valores correspondientes de cada x para cada y. Y ubicar los valores (x,y) en el plano cartesiano.

Por ejemplo tomemos la función:
""")

with st.container(border=True):
    st.markdown("**Digite el valor de b y x para su funcion**")

    col1, col2 = st.columns(2)

    with col1:
     b = st.number_input("b", value=1.0)
    with col2:
     x = st.text_input("x", value="x")

st.latex(f"y = {b if b%1!=0 else int(b)} ^{{{x}}}")

st.markdown("""
la grafica de la función dada es:
""")

with st.container(border=True):

    col1, col2,= st.columns(2)

    with col1:
        if 0<b<1:
            ini =-10
            fin = 10
           
            x=np.linspace(ini,fin,100)
            y=b**x


            fig, ax = plt.subplots()
            ax.plot(x , y)
            st.pyplot(fig)
            st.markdown("La funcion dada es decreciente porque 0<b<1 ")
        

        elif b>1:
              with col2:
               ini =-10
               fin = 10

               x=np.linspace(ini,fin,100)
               y=b**x

               fig, ax = plt.subplots()
               ax.plot(x, y)
               st.pyplot(fig)
               st.markdown("La funcion dada es creciente porque b>1 ")
        else:
          st.markdown("debe ingresar un valor de b mayor que 0 y distinto de 1") 

   









