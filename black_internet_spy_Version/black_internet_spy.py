import os
import sys
import time

# Цветовые коды для терминала
R = "\033[31m"
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
        f"{R}                                   ║             {W}  [{O}1{W}] Maigret Scan       [{O}4{W}] Social-Analyzer    [{O}6{W}] PChange Target              {R}║{W}"
    )
    print(
        f"{R}                                   ║             {W}  [{O}2{W}] Sherlock Scan      [{O}5{W}] Holehe (Email)     [{O}0{W}] Exit System                 {R}║{W}"
    )
    print(
        f"{R}                                   ║             {W}  [{O}3{W}] H8mail (Email)                                                            {R}║{W}"
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

        if choice in ["1", "2", "3", "4", "5",]:
            if not target:
                
                if choice in ["5", "6"]:
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
            

            input(f"\n{Y}[ Нажмите Enter для перехода в Menu]{W}")

        elif choice == "6":
            new_target = (
                input(
                    f"\n{G}[+] Введите новый никнейм, Email {W}"
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


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{R}[*] Процес закончено оператором.{W}\n")
        sys.exit(0)
