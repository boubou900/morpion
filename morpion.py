import turtle
turtle=turtle.Turtle()
turtle.pen(fillcolor="red", pencolor="blue", pensize=10)
turtle.speed(9)
def face_9():
  turtle.penup()
  turtle.left(90)
  turtle.forward(300)
  turtle.left(90)
  turtle.forward(300)
  turtle.left(180)
  turtle.pendown()
  for i in range(3):
       for i in range(4):
           turtle.forward(200)
           turtle.right(90)
       turtle.forward(200)
  turtle.right(90)
  turtle.forward(200)
  for i in range(2):
      for i in range(4):
        turtle.forward(200)
        turtle.right(90)
      turtle.forward(200)
  turtle.right(90)
  turtle.forward(200)
  for i in range(2):
    for i in range(4):
        turtle.forward(200)
        turtle.right(90)
    turtle.forward(200)
  turtle.right(90)
  turtle.forward(400)
  for i in range(2):
    turtle.right(90)
    turtle.forward(200)
def rond():
  turtle.circle(60)
def croix():
  turtle.right(45)
  turtle.forward(120)
  turtle.penup()
  turtle.left(135)
  turtle.forward(85)
  turtle.left(135)
  turtle.pendown()
  turtle.forward(120)
  turtle.left(135)
def test(x):
  jeu=False
  n=0
  for i in range(3):
    if x[n]==x[n+1] and x[n]==x[n+2]:
      jeu=True
    n=n+3
  for i in range(3):
    if x[i]==x[i+3] and x[i]==x[i+6]:
      jeu=True
  if x[0]==x[4] and x[0]==x[8]:
    jeu=True
  if x[2]==x[4] and x[2]==x[6]:
    jeu=True
  return jeu
def place(nouv,listej_1,listej_2):
  if nouv[0]==1:
    listej_1[nouv[1]]=1
    placer_croix(nouv[1])
  if nouv[0]==2:
    listej_2[nouv[1]]=1
    placer_rond(nouv[1])
  return listej_1,listej_2
def demande(quel_joueur):
  case_j=print(input(int("quel case voulez vous placer?")))
  return case_j
def placer_croix(placement):
  if placement==1:
    turtle.setpos(60,30)
    croix()
def placer_rond():

joueur_1=print(input("qui est joueur 1?il aura les croix"))
joueur_2=print(input("qui est joueur 2?il aura les ronds"))
print("les cases sont numérotés comme lorque l'on lit une bd, la premiere case possede l'indice 0")
listej_1=["f","f","f","f","f","f","f","f","f"]
listej_2=["f","f","f","f","f","f","f","f","f"]