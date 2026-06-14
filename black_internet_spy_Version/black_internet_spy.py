import os
import sys
import time

# Цветовые коды для терминала
R = "\033[31m"
P = '\033[1;35m'
B = '\033[1;34m' 
G = "\033[32m"
Y = "\033[33m"
O = "\033[33m"
W = "\033[0m"


def show_logo(current_target="НЕ ВКАЗАНО"):
    """Оригинальный логотип автора и динамическая рамка статуса"""
    print("\033[H\033[J", end="")
    print(
        f"""{R}
          
  ▄██████▄     ▄████████    ▄████████    ▄████████ ███▄▄▄▄      ▄████████  ▄█   ▄█    █▄     ▄████████       ▄██████▄     ▄████████  ▄█  ███▄▄▄▄       ███     
 ███    ███   ███    ███   ███    ███   ███    ███ ███▀▀▀██▄   ███    ███ ███  ███    ███   ███    ███      ███    ███   ███    ███ ███  ███▀▀▀██▄ ▀█████████▄  
 ███    ███   ███    █▀    ███    █▀    ███    █▀  ███   ███   ███    █▀  ███▌ ███    ███   ███    █▀       ███    ███   ███    █▀  ███▌ ███   ███    ▀███▀▀██ 
 ███    ███  ▄███▄▄▄      ▄███▄▄▄      ▄███▄▄▄     ███   ███   ███        ███▌ ███    ███  ▄███▄▄▄          ███    ███   ███        ███▌ ███   ███     ███   ▀ 
 ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀     ▀▀███▀▀▀     ███   ███ ▀███████████ ███▌ ███    ███ ▀▀███▀▀▀          ███    ███ ▀███████████ ███▌ ███   ███     ███     
 ███    ███   ███          ███          ███    █▄  ███   ███          ███ ███  ███    ███   ███    █▄       ███    ███          ███ ███  ███   ███     ███     
 ███    ███   ███          ███          ███    ███ ███   ███    ▄█    ███ ███  ███    ███   ███    ███      ███    ███    ▄█    ███ ███  ███   ███     ███     
  ▀██████▀    ███          ███          ██████████  ▀█   █▀   ▄████████▀  █▀    ▀██████▀    ██████████       ▀██████▀   ▄████████▀  █▀    ▀█   █▀     ▄████▀   
                                                                                                                                                                    
      
{W}"""
    )

      
    print(
        f"{R}                                   ╔═════════════════════════════════════════════════════════════════════════════════════════════╗{W}"
    )
    print(
        f"{R}                                   ║{W}                                 Создатель:  ℂ𝕠ц𝕖𝕒льℍ𝕠𝕔ь                                     {R}║{W}"
    )
    print(
        f"{R}                                   ╠═════════════════════════════════════════════════════════════════════════════════════════════╣{W}"
    )
    print(
        f"{R}                                   ║{W}                      🎯 АКТИВНАЯ ЦЕЛЬ ДЛЯ АТАК НА ВВОД: {O}{current_target:<34}{W}  {R}║{W}"
    )
    print(
        f"{R}                                   ╠═════════════════════════════════════════════════════════════════════════════════════════════╣{W}"
    )
    print(
        f"{R}                                   ║             {W}  [{O}1{W}] Maigret Scan       [{O}4{W}] Social-Analyzer    [{O}7{W}] PChange Target              {R}║{W}"
    )
    print(
        f"{R}                                   ║             {W}  [{O}2{W}] Sherlock Scan      [{O}5{W}] Holehe (Email)     [{O}0{W}] Exit System                 {R}║{W}"
    )
    print(
        f"{R}                                   ║             {W}  [{O}3{W}] H8mail (Email)     [{O}6{W}] Dossier Generator                                  {R}║{W}"
    )
    print(
        f"{R}                                   ╚═════════════════════════════════════════════════════════════════════════════════════════════╝{W}"
    )


def run_scan(module_name, target):
    print(f"\n{Y}[*] Ініціалізація модуля {module_name}...")
    time.sleep(1)
    print(f"{G}[+] Сканирование об'єкта '{target}' успешно розпочато!{W}\n")

    venv_python = os.path.expanduser("~/maigret_osint/venv/bin/python")
    holehe_bin = os.path.expanduser("~/maigret_osint/venv/bin/holehe")
    h8mail_bin = os.path.expanduser("~/maigret_osint/venv/bin/h8mail")
    sherlock_bin = os.path.expanduser("~/maigret_osint/venv/bin/sherlock")

    if module_name == "MAIGRET":
        os.system(f"{venv_python} -m maigret {target} -a")

    elif module_name == "SHERLOCK":
        os.system(f"{sherlock_bin} {target} --timeout 5")

    elif module_name == "SOCIAL_ANALYZER":
        os.system(
            f"{venv_python} -m social-analyzer --cli --mode 'fast' --username '{target}' --websites 'all' --filter 'good'"
        )
    elif module_name == "DOSSIER":
        DOSSIER(target)
    elif module_name == "HOLEHE":
        os.system(f"{holehe_bin} {target}")

    elif module_name == "H8MAIL":
        os.system(f"{h8mail_bin} -t {target}")

def main_menu():
    target = ""

    while True:
        current_target = target if target else "НЕ ВКАЗАНО"
        show_logo(current_target)

        choice = input(f"{G}\n[>] Выберите Действие: {W}").strip()

        if choice in ["1", "2", "3", "4", "5","6"]:
            if not target and choice != "6":
                if choice in ["3", "5"]:
                    prompt_text = (
                        f"\n{O}[+] Введите Email для поиска витоков: {W}"
                    )
                else:
                    prompt_text = f"\n{O}[+] Введите ник для поиска: {W}"

                target = input(prompt_text).strip()
                if not target:
                    print(f"\n{R}[-] error: Ввод не может быть пустым!{W}")
                    time.sleep(1.5)
                    continue


            if choice == "1":
                run_scan("MAIGRET", target)
            elif choice == "2":
                run_scan("SHERLOCK", target)
            elif choice == "3":
                run_scan("H8MAIL", target)    
            elif choice == "4":
                run_scan("SOCIAL_ANALYZER", target)
            elif choice == "5":
                run_scan("HOLEHE", target)
            elif choice == "6":
                run_scan("DOSSIER", target)

            input(f"\n{Y}[ Нажмите Enter для перехода в Menu]{W}")       
        elif choice == "7":
            new_target = (
                input(
                    f"\n{G}[+] Введите новый никнейм, Email: {W}"
                )
                .strip()
            )
            if new_target:
                target = new_target
            else:
                print(f"\n{R}[-] error: Ввод не может быть пустым!{W}")
                time.sleep(1.5)

        elif choice == "0":
            print(
                f"\n{R}[*] Сессию завершено. Блокнот закрыто Выход...{W}\n"
            )
            break
        else:
            print(f"\n{R}[-] Неверный выбор. Попробуйте еще раз.{W}")
            time.sleep(1)
def DOSSIER(target):
    print(f"{Y}[?] ЗАПОЛНЕНИЕ ДАННЫХ ОБЪЕКТА (Оставьте пустым, если нет данных):{W}\n")
    
    fio = input(f" {O}├──{W} Введите ФИО: ").strip()
    nickname = input(f" {O}├──{W} Введите Никнейм (username): ").strip()
    phone = input(f" {O}├──{W} Введите Номер телефона: ").strip()
    email = input(f" {O}├──{W} Введите Электронную почту (Email): ").strip()
    location = input(f" {O}├──{W} Где живет (Город/Адрес): ").strip()
    school = input(f" {O}├──{W} Где учиться (Школа/Адрес): ").strip()
    bio = input(f" {O}├──{W} Дополнительные заметки/работа: ").strip()
    fioR = input(f" {O}├──{W} Введите ФИО родителей: ").strip() #родители 
    phone0 = input(f" {O}├──{W} Введите Номер родителей (матери или отца): ").strip()
    bior = input(f" {O}├──{W} Введите роботу родителей: ").strip()
    valid = input(f" {O}└──{W} Введите кем был валидован: ").strip()

    print(f"\n{Y}[*] Анализ и структурирование информации...{W}")
    time.sleep(1.5)
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{G}[+] СФОРМИРОВАННОЕ ДОСЬЕ ОБЪЕКТА{W}") 
    print(f"{B} Target Profile:{W}")
    
    if fio:
        print(f" {O}├──{W} ФИО: {G}{fio}{W}")
    if nickname:
        print(f" {O}├──{W} Никнейм: {P}@{nickname}{W} ◄")
    if phone:
        print(f" {O}├──{W} Телефон: {Y}{phone}{W}")
    if email:
        print(f" {O}├──{W} Email: {Y}{email}{W}")
    if location:
        print(f" {O}├──{W} Место жительства: {G}{location}{W} ⟵")
    if school:
        print(f" {O}├──{W} Учиться в : {G}{school}{W} ⟵")
    if bio:
        print(f" {O}├──{W} Примечания: {W}{bio}{W}")
    if fioR:
        print(f" {O}├──{W} Фио родителей: {W}{fioR}{W}")
    if phone0:
        print(f" {O}├──{W} Номер родителей: {W}{phone0}{W}")
    if bior:
        print(f" {O}├──{W} Робота родителей: {W}{bior}{W}")
    if valid:
        print(f" {O}└──{W} Validated By: {W}{valid}{W}")
    else:
        print(f" {O}└──{W} Конец записи.")
if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{R}[*] Процес закончено оператором.{W}\n")
        sys.exit(0)
