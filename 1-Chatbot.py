#!/usr/bin/env python
# coding: utf-8

# In[15]:


import re
import random
import sqlite3
import csv


# In[16]:


conn = sqlite3.connect('conversaciones.db')
c = conn.cursor()

# aqui Creamos una tabla llamada "conversaciones" si es que no existe
c.execute('''CREATE TABLE IF NOT EXISTS conversaciones
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
               user_name TEXT,
               user_input TEXT,
               bot_response TEXT,
               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')


# In[ ]:


c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())

#La consulta SQL que se ejecuta es SELECT name FROM sqlite_master WHERE type='table'
# la cual obtiene los nombres de todas las tablas que existen en la base de datos actual.


# In[18]:


def prob_mensaje(mensaje, lista_palabras, single_response=False, palabras_requeridas=[]):
    puntaje = 0
    for palabra in lista_palabras:
        if palabra in mensaje:
            puntaje += 1
    if single_response:
        return puntaje
    else:
        for palabra in palabras_requeridas:
            if palabra not in mensaje:
                return 0
        return puntaje


#Si se proporciona una lista de palabras requeridas, la función comprueba que todas las palabras estén presentes en el
#mensaje del usuario. Si palabras_requeridas es verdadero o si single_response es verdadero, la 
#función devuelve el porcentaje multiplicado por 100. Si no, devuelve 0.


# In[19]:


def check_all_messages(mensaje):
    prob_mayor = {}
    c.execute("SELECT bot_response FROM conversaciones WHERE user_input=?", (mensaje,))
    respuestas = c.fetchall()
    for r in respuestas:
        bot_response = r[0]
        prob_mayor[bot_response] = prob_mensaje(mensaje, [''], single_response=True)

    if prob_mayor:
        best_match = max(prob_mayor, key=prob_mayor.get)
        return best_match
    else:
        return error()
# se itera a través de cada respuesta almacenada en respuestas. En cada iteración,
#se obtiene la respuesta almacenada y se utiliza la función prob_mensaje para calcular 
#la probabilidad de que esa respuesta sea la mejor respuesta para el mensaje del usuario. 
#La probabilidad se almacena en el diccionario prob_mayor junto con la respuesta almacenada como clave.

#Después de calcular las probabilidades de todas las respuestas almacenadas, 
#se verifica si prob_mayor tiene algún elemento. Si es así, se busca la respuesta con la mayor probabilidad 
#utilizando la función max con el parámetro key=prob_mayor.get, que se utiliza para buscar el valor máxim0
    


# In[ ]:



# In[20]:


#la funcion devuelve una respuesta aleatoria de las definidas en la lista
def error():
    respuestas = ['Perdón, no te entendí', 'Podrías reformular tu pregunta', 'No sé de qué me estás hablando',
                  'Lo siento, no te entendí', 'Por favor, ¿podrías decirlo de otra forma?']
    return random.choice(respuestas)


# In[ ]:





# In[21]:


user_name = input('Con quien tengo esta conversacion?:..') #aca podria ir la etapa login de usuario, 
def get_response(user_input):
   response = check_all_messages(user_input)
   if response:
       return response
   else:
       return "No estaria entendiendo..."

while True:
  
   user_input = input('Bot:..')
   bot_response = get_response(user_input)
   c.execute("INSERT INTO conversaciones (user_name, user_input, bot_response) VALUES (?, ?, ?)",
             (user_name, user_input, bot_response))
   conn.commit()
   print("Bot: " + bot_response)

   if user_input.lower() == 'adios':
       break

while True:
   user_input = input("Usuario: ")
   if user_input.lower() == "adios":
       print("Bot: ¡Hasta luego!")
       break
   else:
       bot_response = get_response(user_input)
       c.execute("INSERT INTO conversaciones (user_name, user_input, bot_response) VALUES (?, ?, ?)",
                 (user_name, user_input, bot_response))
       conn.commit()
       print("Bot: " + bot_response)
       
       
#esta etapa consiste en dos bucles while anidados,se solicita continuamente la entrada del usuario y 
#se procesa utilizando la función get_response. Si la respuesta no es None,
#se inserta en la base de datos junto con el nombre del usuario y la entrada del usuario. 
#Si la entrada del usuario es "adios", el bucle interior termina y el programa finaliza.


# In[ ]:




