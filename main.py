# from turtle import Turtle, Screen
#
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "squirtle", "charmander"])
table.add_column("Table", ["Electric", "water", "Fire"])


table.align = "l" #значение по левому краю
print(table)
