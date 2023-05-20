from ui import screen


continuar = True


while continuar:
    screen.clean()
    screen.menu()

    option = int(input())

    if option == 1:
        screen.clean()
        screen.option1()
     

    if option == 2:
        screen.clean()
        screen.menu_search()
        option_sub_menu = int(input())

    if option == 3:
        screen.clean()
        screen.option3()

    if option == 4:
        break

    if option == 5:
        break

    if option == 6:
        continuar = False