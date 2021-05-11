import turtle
import random

screen = turtle.getscreen()

screen.setup(width=500, height=350)

words = ["apercevoir",
         "ascensseur",
         "aspirateur",
         "bijouterie",
         "brouillard",
         "capitaines",
         "celebrites",
         "definition",
         "economiser",
         "entraineur"]

words = [i.upper() for i in words]
word = random.choice(words)
run = True
score = 15

turtle.up()

hide = word[0] + " " + " ".join("_" for _ in range(8)) + " " + word[-1]
turtle.setx(-160)
turtle.write(hide, font=("arial", 30, 'normal'))

turtle.setpos(-200, -175)
turtle.write(f"score : {score}", font=("arial", 30, 'normal'))

letter = turtle.textinput("Choississez une lettre", "Veuillez ne mettre qu'une seule lettre")

while run:
    if letter is None:
        break
    if letter.upper() not in word:
        score -= 1

    tab = hide.split()
    for i in range(len(word)):
        if word[i] == letter.upper():
            tab[i] = letter.upper()
    hide = " ".join(tab)

    turtle.clear()
    turtle.setpos(-160, 0)
    turtle.write(hide, font=("arial", 30, 'normal'))
    turtle.setpos(-200, -175)
    turtle.write(f"score : {score}", font=("arial", 30, 'normal'))

    if "".join(hide.split()) == word:
        turtle.setpos(-160, 100)
        turtle.write("Bravo, vous avez gagné", font=("arial", 15, 'normal'))
        break
    if score == 0:
        turtle.setpos(-160, 100)
        turtle.write(f'Dommage, le mot était "{word}"', font=("arial", 15, 'normal'))
        break

    if letter.upper() in word:
        letter = turtle.textinput("Choississez une lettre", "Veuillez ne mettre qu'une seule lettre")
    else:
        letter = turtle.textinput("Mauvaise lettre !", "Veuillez ne mettre qu'une seule lettre")

    if len(letter) != 1:
        continue

turtle.mainloop()
