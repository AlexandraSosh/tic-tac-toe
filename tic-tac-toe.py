print("Игра крестики-нолики")

game_field = list(range(1, 10))


def draw_field(game_field):
    print("-" * 13)
    for i in range(3):
        print("|", game_field[0 + i * 3], "|", game_field[1 + i * 3], "|", game_field[2 + i * 3], "|")
        print("-" * 13)


def game_condition(condition):
    mean = None
    while not mean:
        answer = input("Выбери клетку для " + condition + "? ")
        try:
            answer = int(answer)
        except:
            print("Некорректный ввод. Введите число от 1 до 9.")
            continue
        if 1 <= answer <= 9:
            if (str(game_field[answer - 1]) not in "XO"):
                game_field[answer - 1] = condition
                mean = True
            else:
                print("Уже занято, выбери другую клетку.")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def check_win(game_field):
    victory_check = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in victory_check:
        if game_field[each[0]] == game_field[each[1]] == game_field[each[2]]:
            return game_field[each[0]]
    return False


def main(game_field):
    counter = 0
    win = None
    while not win:
        draw_field(game_field)
        if counter % 2 == 0:
            game_condition("X")
        else:
            game_condition("O")
        counter += 1
        if counter > 4:
            tmp = check_win(game_field)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_field(game_field)


main(game_field)

input("Нажмите Enter для выхода!")