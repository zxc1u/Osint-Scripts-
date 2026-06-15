import os
import sys
import time
from scapy.all import sniff, UDP, IP

# СТИЛЬНІ КОЛЬОРИ ДЛЯ ТЕРМІНАЛА ARCH
G = '\033[1;32m' # Зелений (Перехоплення)
R = '\033[1;31m' # Червоний (Помилка)
Y = '\033[1;33m' # Жовтий (Очікування)
P = '\033[1;35m' # Фіолетовий (Логотип)
O = '\033[38;5;208m' # Помаранчевий (Ваш фірмовий колір для IP)
W = '\033[0m'    # Скидання кольору

os.system('clear')
print(f"""{R}
      
          ▄██████▄     ▄████████  ▄█  ███▄▄▄▄       ███             ▄███████▄     ███        ▄███████▄      
         ███    ███   ███    ███ ███  ███▀▀▀██▄ ▀█████████▄        ███    ███ ▀█████████▄   ███    ███      
         ███    ███   ███    █▀  ███▌ ███   ███    ▀███▀▀██        ███    ███    ▀███▀▀██   ███    ███      
         ███    ███   ███        ███▌ ███   ███     ███   ▀        ███    ███     ███   ▀   ███    ███      
         ███    ███ ▀███████████ ███▌ ███   ███     ███          ▀█████████▀      ███     ▀█████████▀       
         ███    ███          ███ ███  ███   ███     ███            ███            ███       ███             
         ███    ███    ▄█    ███ ███  ███   ███     ███            ███            ███       ███             
          ▀██████▀   ▄████████▀  █▀    ▀█   █▀     ▄████▀         ▄████▀         ▄████▀    ▄████▀           
                                    ╔═════════════════════════════════╗
                                    ║     Создатель:  ℂ𝕠ц𝕖𝕒льℍ𝕠𝕔ь     ║
                                    ╚═════════════════════════════════╝
 {W}""")

print(f"\n{Y}[*] Перехватчик STUN-пакетов успешно запущен в текущем терминале.{W}")
print(f"{Y}[!] Ожидаю звонки Telegram. Лог пишется на экран и в файл...{W}\n")

captured_ips = set()

def packet_callback(packet):
    if packet.haslayer(UDP) and packet.haslayer(IP):
        payload = bytes(packet[UDP].payload)
        src_ip = packet[IP].src
        
        # Пошук сигнатури STUN-запитів (Binding Request \ Binding Success)
        if b'\x00\x01' in payload or b'\x01\x01' in payload:
            
            # Фільтруємо внутрішні локальні адреси домашнього роутера
            is_local = any(src_ip.startswith(prefix) for prefix in ("192.168.", "127.", "10.", "172."))
            
            if src_ip not in captured_ips and not is_local:
                captured_ips.add(src_ip)
                
                # ТЕПЕР СКРИПТ ВИВОДИТЬ ІНФОРМАЦІЮ В ТЕРМІНАЛ В РЕАЛЬНОМУ ЧАСІ:
                print(f"{G}[+] УСПЕШНЫЙ ПЕРЕХВАТ! Удаленный IP звонка: {O}{src_ip}{W}")
                
                # АВТОМАТИЧНИЙ ДОЗАПИС ЗНАЙДЕНОЇ АДРЕСИ У ВАШ ФАЙЛ БЛОКНОТА:
                with open("incoming_messages_dossier.txt", "a", encoding="utf-8") as file:
                    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
                    file.write(f"[{current_time}] ПЕРЕХВАТ ТРАФИКА ДЗВІНКА -> IP: {src_ip}\n")

try:
    # Запуск прослуховування мережевої карти на UDP-протоколі
    sniff(filter="udp", prn=packet_callback, store=0)
    
except KeyboardInterrupt:
    print(f"\n\n{R}[*] Сессия перехвата остановлена оператором. Блокнот сохранен.{W}\n")
    sys.exit(0)
    
except PermissionError:
    # Захист від запуску без root-прав, який ви додали на скріншоті
    print(f"\n{R}[-] КРИТИЧЕСКАЯ ОШИБКА: Для снайпинга интерфейса нужны root-права!{W}")
    print(f"{Y}[!] Запустите команду строго через: sudo ...{W}\n")
    sys.exit(1)
