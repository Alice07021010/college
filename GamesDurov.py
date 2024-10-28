import time
import random

def print_delayed(text, delay=1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()
    time.sleep(delay)


def start_game():
    print_delayed("Вы один из самых богатых людей ОАЭ, имеете огромное влияние и успех, но что-то пошло не так....")
    print_delayed("Итак, Вы находитесь в холодной камере одной из французских тюрем...")
    time.sleep(1)

    print_delayed("Ваша цель — сбежать, ради своих 100 детишек! Что вы будете делать?")
    print_delayed("1. Осмотреть камеру")
    print_delayed("2. Поговорить с сокамерником")

    choice1 = input("Выберите 1 или 2: ")

    if choice1 == '1':
        explore_cell()
    elif choice1 == '2':
        talk_to_cellmate()
    else:
        print_delayed("Неверный ввод. Игра завершена.")


def explore_cell():
    print_delayed("Вы осматриваете свою камеру и замечаете трещину в стене.")
    print_delayed("Также вы видите окно, но оно заперто решеткой.")

    print_delayed("Что вы будете делать?")
    print_delayed("1. Пытаться снести стену, как в 2010 году")
    print_delayed("2. Попробовать открыть окно")

    choice2 = input("Выберите 1 или 2: ")

    if choice2 == '1':
        print_delayed("Вы сносите стену, но попадаете в соседнюю камеру...")
        end_game(
            "Соседей не было и вы остались в ловушке, издалека слышен крик охраны 'Durov, ramène le mur!', что переводится как 'Дуров, верни стену!'.")
    elif choice2 == '2':
        print_delayed("Вы долго пытались открыть окно, но оно слишком крепкое.")
        end_game("Ваши усилия привлекли внимание охраны.")
    else:
        print_delayed("Неверный ввод. Игра завершена.")


def talk_to_cellmate():
    print_delayed("Вы начинаете разговор с сокамерником.")
    print_delayed("Он предлагает вам план побега, но вам нужно принять решение.")

    print_delayed("Что вы хотите сделать?")
    print_delayed("1. Согласиться на план сокамерника")
    print_delayed("2. Отклонить предложение и действовать самостоятельно")

    choice3 = input("Выберите 1 или 2: ")

    if choice3 == '1':
        print_delayed("Вы и ваш сокамерник начали планировать побег. Но охрана заметила вас!")
        fight_guard()
    elif choice3 == '2':
        print_delayed("Вы решили действовать в одиночку и пытаетесь придумать свой собственный план.")
        explore_cell()
    else:
        print_delayed("Неверный ввод. Игра завершена.")


def fight_guard():
    print_delayed("Вы сталкиваетесь с охранником! У вас есть несколько бумажных самолетиков, которые вы сделали ранее.")
    print_delayed("Как вы хотите с ним справиться?")

    print_delayed("1. Бросить в охранника самолетики")
    print_delayed("2. Попробовать отвлечь охранника и сбежать")

    choice4 = input("Выберите 1 или 2: ")

    if choice4 == '1':
        paper_airplane_battle()
    elif choice4 == '2':
        distract_guard_and_escape()
    else:
        print_delayed("Неверный ввод. Игра завершена.")


def paper_airplane_battle():
    print_delayed("Вы быстро запускаете самолетики в сторону охранника!")
    for i in range(3):
        print_delayed(f"Бум! Самолетик {i + 1} попал в охранника!")
        time.sleep(0.5)

    print_delayed("Охранник растерян и начинает отступать, вы видите возможность сбежать!")
    print_delayed("Вам удалось сбежать из камеры!")
    print_delayed("Вы на свободе, теперь нужно добраться до выхода из тюрьмы.")
    end_game("Поздравляем! Вы смогли сбежать, вы спасены и дети не остались без отца и алиментов!!!!")


def distract_guard_and_escape():
    print_delayed("Вы бросаете свои вещи в другую сторону, чтобы отвлечь охранника.")
    print_delayed("Пока охранник смотрит, вы медленно крадётесь к выходу.")

    if random.random() > 0.5:
        print_delayed("Вы успешно прошли мимо охранника и выбрались из тюрьмы!")
        end_game("Поздравляем! Вы на свободе!")
    else:
        print_delayed("К сожалению, охранник заметил вас и схватил!")
        end_game("Игра окончена. Вас поймали.")



def end_game(message):
    print_delayed(message)
    print_delayed("Спасибо за игру!")
    exit()


if __name__ == "__main__":
    start_game()
