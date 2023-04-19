#!/usr/bin/env python
# coding: utf-8

# In[6]:


import sqlite3


# In[7]:


#La función comienza conectándose a la base de datos SQLite utilizando el archivo conversaciones.db. 
#Luego, solicita el nombre del usuario que está agregando las nuevas preguntas y respuestas.
def train_bot():
    conn = sqlite3.connect('conversaciones.db')
    c = conn.cursor()
    user_name = input("Nombre de usuario: ")
    while True:
        pregunta = input("Pregunta: ")
        if pregunta.lower() == 'adios':
            break
        respuesta = input("Respuesta: ")
        c.execute("INSERT INTO conversaciones (user_name, user_input, bot_response) VALUES (?, ?, ?)", (user_name, pregunta, respuesta))
    conn.commit()
    print("Pregunta y respuesta agregadas a la base de datos.")

train_bot()



#se inicia un bucle while que solicita continuamente la entrada del
#usuario para la pregunta y la respuesta. Si la entrada del usuario para la pregunta es "adios",
#el bucle se interrumpe y la función finaliza.


# In[ ]:





# In[ ]:




