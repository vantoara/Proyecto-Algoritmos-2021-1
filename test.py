
question = "Tengo el siguiente string: frase  = \"tengo en mi cuenta 50,00 $\". Escribe en una línea de código como extraer de este string los 50 en formato entero"
list_question = question.split()
phrase = list_question[6:11]
phrase = " ".join(phrase).replace("\"","").replace(",",".")
print(phrase)