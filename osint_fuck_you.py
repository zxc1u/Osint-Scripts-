import os
import sys
import time
# ну и зачем ?
G = '\033[1;32m' # Зелений
R = '\033[1;31m' # Червоний
B = '\033[1;34m' # Синій (
Y = '\033[1;33m' # Жовтий
P = '\033[1;35m' # Фіолетовий
O = '\033[38;5;208m' # Помаранчевий
W = '\033[0m'
#BlackInternet,Соцеальный

def show_logo():
    print("\033[H\033[J", end="") 
    print(f"""{R}
          
 ▄██████▄     ▄████████    ▄████████    ▄████████ ███▄▄▄▄      ▄████████  ▄█   ▄█    █▄     ▄████████       ▄██████▄     ▄████████  ▄█  ███▄▄▄▄       ███     
███    ███   ███    ███   ███    ███   ███    ███ ███▀▀▀██▄   ███    ███ ███  ███    ███   ███    ███      ███    ███   ███    ███ ███  ███▀▀▀██▄ ▀█████████▄ 
███    ███   ███    █▀    ███    █▀    ███    █▀  ███   ███   ███    █▀  ███▌ ███    ███   ███    █▀       ███    ███   ███    █▀  ███▌ ███   ███    ▀███▀▀██ 
███    ███  ▄███▄▄▄      ▄███▄▄▄      ▄███▄▄▄     ███   ███   ███        ███▌ ███    ███  ▄███▄▄▄          ███    ███   ███        ███▌ ███   ███     ███   ▀ 
███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀     ▀▀███▀▀▀     ███   ███ ▀███████████ ███▌ ███    ███ ▀▀███▀▀▀          ███    ███ ▀███████████ ███▌ ███   ███     ███     
███    ███   ███          ███          ███    █▄  ███   ███          ███ ███  ███    ███   ███    █▄       ███    ███          ███ ███  ███   ███     ███     
███    ███   ███          ███          ███    ███ ███   ███    ▄█    ███ ███  ███    ███   ███    ███      ███    ███    ▄█    ███ ███  ███   ███     ███     
 ▀██████▀    ███          ███          ██████████  ▀█   █▀   ▄████████▀  █▀    ▀██████▀    ██████████       ▀██████▀   ▄████████▀  █▀    ▀█   █▀     ▄████▀   
                                                                                                                                                                    
      
{W}""")

def show_banner():
    show_logo()


def run_scan(module_name, target):
    print(f"\n{Y}[*] Ініціалізація модуля {module_name}...")
    time.sleep(1) 
    print(f"{G}[+] Сканування об'єкта '{target}' успішно розпочато!{W}\n")
    
    venv_python = os.path.expanduser("~/maigret_osint/venv/bin/python")
    
    if module_name == "MAIGRET":
        os.system(f"{venv_python} -m maigret {target} -a")
        
    elif module_name == "SHERLOCK":
        sherlock_bin = os.path.expanduser("~/maigret_osint/venv/bin/sherlock")
        os.system(f"{sherlock_bin} {target} --timeout 5")
        
    elif module_name == "SOCIAL_ANALYZER":
        os.system(f"{venv_python} -m social-analyzer --cli --mode 'fast' --username '{target}' --websites 'all' --filter 'good'")
        
    elif module_name == "VECTOR":
        print(f"{Y}[*] Розрахунок вектора цифрового сліду для '{target}'...{W}")
        time.sleep(2)
        print(f"{G}[+] Векторний аналіз завершено. Зв'язки зафіксовано в блокноті.{W}")

# 3. УПРАВЛЯЮЧИЙ ІНТЕРФЕЙС (ГОЛОВНЕ МЕНЮ)
# 3. УПРАВЛЯЮЧИЙ ІНТЕРФЕЙС (ГОЛОВНЕ МЕНЮ)
def main_menu():
    # Спочатку ціль порожня, ми запитаємо її після вибору тулки
    target = ""

    while True:
        show_logo()
        
        # Відображаємо статус активної цілі
        current_target = target if target else "НЕ ВКАЗАНА"
        
        print(f"{R}                                   ╔═════════════════════════════════════════════════════════════════════════════════════════════╗{W}")
        print(f"{R}                                   ║{W}                                 Создатель:  ℂ𝕠ц𝕖𝕒льℍ𝕠𝕔ь                                     {R}║{W}")
        print(f"{R}                                   ╠═════════════════════════════════════════════════════════════════════════════════════════════╣{W}")
        print(f"{R}                                   ║{W}                      🎯 АКТИВНА ЦІЛЬ ДЛЯ АТАК НА ВВОД: {O}{current_target:<34}{W}   {R}║{W}")
        print(f"{R}                                   ╠═════════════════════════════════════════════════════════════════════════════════════════════╣{W}")
        print(f"{R}                                   ║             {W}  [{O}1{W}] Maigret Scan       [{O}3{W}] Vector-Analysis   [{O}5{W}] Change Target                {R}║{W}")
        print(f"{R}                                   ║             {W}  [{O}2{W}] Sherlock Scan      [{O}4{W}] Social-Analyzer    [{O}0{W}] Exit System                 {R}║{W}")
        print(f"{R}                                   ╚═════════════════════════════════════════════════════════════════════════════════════════════╝{W}")

        choice = input(f"{G}\n[>] Виберіть дію: {W}").strip()

        # СУВОРА ВАЛІДАЦІЯ КНОПОК МЕНЮ
        if choice in ["1", "2", "3", "4"]:
            if not target:
                target = input(f"\n{O}[+] введите ник для поиска: {W}").strip()
                if not target:
                    print(f"\n{R}[-] Помилка: Ввід не може бути порожнім!{W}")
                    time.sleep(1.5)
                    continue

            if choice == "1":
                run_scan("MAIGRET", target)
            elif choice == "2":
                run_scan("SHERLOCK", target)
            elif choice == "3":
                run_scan("VECTOR", target)
            elif choice == "4":
                run_scan("SOCIAL_ANALYZER", target)

            input(f"\n{Y}[ Натисніть Enter для повернення в меню ]{W}")

        elif choice == "5":
            new_target = input(f"\n{G}[+] Введіть НОВИЙ нікнейм: {W}").strip()
            if new_target:
                target = new_target
            else:
                print(f"\n{R}[-] Помилка: Ввід не може бути порожнім!{W}")
                time.sleep(1.5)

        elif choice == "0":
            print(f"\n{R}[*] Сесію завершено. Блокнот закрито. Вихід...{W}\n")
            break
            
        else:
            print(f"\n{R}[-] Невірний вибір. Спробуйте ще раз.{W}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{R}[*] Процес примусово зупинено оператором.{W}\n")
        sys.exit(0)
