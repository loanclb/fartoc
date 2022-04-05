def check_answer():
    answered = False
    while answered == False:
        answer = input("""
          Que souhaites-tu calculer/convertir ? (poussée | cvtctof | cvtftoc | energie) :
            >> """)
        if answer == "poussée":
            answered = True
            return "poussée"
        if answer == "cvtftoc":
            answered = True
            return "cvtftoc"
        if answer == "cvtctof":
            answered = True
            return "cvtctof"
        if answer =="energie":
            answered = True
            return "energie"
        else:
            print("""
              Erreur, merci de vérifier la frappe
            """)
            

def f_to_c():
  c_temp = (f_temp - 32) * 5/9
  return c_temp

def c_to_f():
  f_temp = c_temp * (9/5) + 32
  return f_temp

def get_force(mass, acceleration):
  return mass * acceleration

def get_energy(mass, c = 3*10**8):
  return mass * c ** 2

def get_work (mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

def checkInt(str):
    if str[0] in ('-', '+'):
        str(str)
        return str[1:].isdigit()
    return str.isdigit()

def checkFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def checkStr(value):
    try:
        str(value)
        return True
    except ValueError:
      return False

def checkCalculable(value):
  intValue = checkInt(value)
  if intValue == True:
    return "int"
  floatValue = checkFloat(value)
  if floatValue == True:
    return "float"
  else:
    return "str"

def checkAgain():
  ag_answer = input("""
    Souhaites-tu calculer autre chose ? (y/n)
    >> """)
  if ag_answer == "y":
    return True
  elif ag_answer =="n":
    return False

#start
print("""
*****************************************************************
*                                                               *
*    ::::::::::  :::    ::::::::::::::::::::::::::::  ::::::::  *
*  :+:       :+: :+:  :+:    :+:   :+:   :+:    :+::+:    :+:   *
*  +:+      +:+   +:+ +:+    +:+   +:+   +:+    +:++:+          *
*  :#::+::#+#++:++#++:+#++:++#:    +#+   +#+    +:++#+          *
*  +#+     +#+     +#++#+    +#+   +#+   +#+    +#++#+          *
*  #+#     #+#     #+##+#    #+#   #+#   #+#    #+##+#    #+#   *
*  ###     ###     ######    ###   ###    ########  ########    *
*                                                               *
*****************************************************************

| >> dev par loanclb
| >> python3

Ce programme me sert d'entraînement, j'apprends encore le python, inspiré d'un exercice de Codecademy

""")

answer=""
ag_answer = ""
is_over = False
massStr = False
accStr = False

while is_over == False:
  checked = check_answer()

  if checked == "cvtctof":
    c_answer = ""
    calculable = False
    while calculable == False:
      c_temp1 = input("""
Taper la température en Celsius à convertir en Fahrenheit : 
>> """)
      c_answer = checkCalculable(c_temp1)
      if c_answer == "int" or c_answer == "float":
        calculable = True
        if c_answer == "int":
          c_temp = int(c_temp1)
        elif c_answer == "float":
          c_temp = float(c_temp1)
      else:
        print("""
          Erreur, veuillez taper un nombre
          """)
    c_in_fahrenheit = c_to_f()
    print("""
      La température """ + c_temp1 +" °C vaut " + str(c_in_fahrenheit) +""" °F.
      """)
    again = checkAgain()
    c_in_farhenheit = 0
    if again == True:
      is_over = False
    elif again == False:
        is_over = True
        print("""
          Merci d'avoir utilisé fartoc ! À bientôt !
        """)


  elif checked == "cvtftoc":
    f_answer = ""
    calculable = False
    while calculable == False:
      f_temp1 = input("""
        Taper la température en Celsius à convertir en Fahrenheit : 
        >> """)
      f_answer = checkCalculable(f_temp1)
      if f_answer == "int" or f_answer == "float":
        calculable = True
        if f_answer == "int":
          f_temp = int(f_temp1)
        elif f_answer == "float":
          f_temp = float(f_temp1)
      else:
        print("""
          Erreur, veuillez taper un nombre
          """)
    f_in_celsius = f_to_c()
    print("""
      La température """ + f_temp1 +" °C vaut " + str(f_in_celsius) +""" °F.
      """)
    again = checkAgain()
    f_in_celsius = 0
    if again == True:
      is_over = False
    elif again == False:
      is_over = True
      print("""
        Merci d'avoir utilisé fartoc ! À bientôt !
      """)
      
  if checked == "energie":
    object_massAnswer = ""
    object_accAnswer = ""
    calculable = False
    while calculable == False:
      object_mass1 = input("""
        Donner la masse de l'objet (kg) : 
          >> """)
      object_acceleration1 = input("""
        Donner la vitesse de l'objet (km/h):
          >> """)
      object_massAnswer = checkCalculable(object_mass1)
      object_accAnswer = checkCalculable(object_acceleration1)
      if (object_massAnswer == "int" or object_massAnswer == "float") and (object_accAnswer == "int" or object_accAnswer == "float"):
        calculable = True
        if object_massAnswer == "int":
          object_mass = int(object_mass1)
        elif object_massAnswer =="float":
          object_mass = float(object_mass1)
        if object_accAnswer == "int":
          object_acceleration = int(object_acceleration1)
        elif object_accAnswer =="float":
          object_acceleration = float(object_acceleration1)
      else:
        print("""
          Vous avez tapé du texte dans l'un des champs, et non un nombre, veuillez réessayer
          """)

    object_force = get_force(object_mass, object_acceleration)
    print("""
      L'objet a """ + str(object_force) +" newtons de force, avec pour paramètres " + object_mass1 + "kg de masse, " + object_acceleration1 + "km/h de vitesse.") 
    again = checkAgain()
    if again == True:
      is_over = False
    elif again == False:
      is_over = True
      print("""
        Merci d'avoir utilisé fartoc ! À bientôt !
      """)


  if checked == "poussée":
    object_massAnswer = ""
    object_accAnswer = ""
    object_distanceAnswer = ""
    calculable = False
    while calculable == False:
      object_mass1 = input("""
        Donner la masse de l'objet (kg): 
          >> """)
      object_acceleration1 = input("""
        Donner la vitesse de l'objet (km/h) :
          >> """)
      object_distance1 = input("""
        Donner sur quelle distance (m): 
          >> """)
      object_massAnswer = checkCalculable(object_mass1)
      object_accAnswer = checkCalculable(object_acceleration1)
      object_distanceAnswer = checkCalculable(object_distance1)

      if (object_massAnswer == "int" or object_massAnswer == "float") and (object_accAnswer == "int" or object_accAnswer == "float") and (object_distanceAnswer == "int" or object_distanceAnswer == "float"):
        calculable = True
        if object_massAnswer == "int":
          object_mass = int(object_mass1)
        elif object_massAnswer =="float":
          object_mass = float(object_mass1)
        if object_accAnswer == "int":
          object_acceleration = int(object_acceleration1)
        elif object_accAnswer =="float":
          object_acceleration = float(object_acceleration1)
        if object_distanceAnswer == "int":
          object_distance = int(object_distance1)
        elif object_distanceAnswer == "float":
          object_distance = float(object_distance1)
      else:
        print("""
          Vous avez tapé du texte dans l'un des champs, et non un nombre, veuillez réessayer
          """)

    
    object_work = get_work(object_mass, object_acceleration, object_distance)
    print("""
      L'objet délivre """ + str(object_work) + " newtons de poussée sur " + str(object_distance) + " mètres, à la vitesse de " + object_acceleration1 + "km/h.")
    again = checkAgain()
    if again == True:
      is_over = False
    elif again == False:
      is_over = True
      print("""
          Merci d'avoir utilisé fartoc ! À bientôt !
        """)
    
