# MENU

from ui import screen

continuar = True

while continuar:
    screen.clean()
    screen.menu()

    option = screen.selectOption()

    if option == 5:
        continuar = False