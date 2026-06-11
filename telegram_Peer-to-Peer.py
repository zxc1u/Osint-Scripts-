import os
import sys
import requests
import time
from scapy.all import sniff, UDP, IP

# СТИЛЬНЫЕ ЦВЕТА ДЛЯ ТЕРМИНАЛА ARCH
G = '\033[1;32m' # Зеленый (Перехват)
R = '\033[1;31m' # Красный (Ошибка)
Y = '\033[1;33m' # Желтый (Ожидание)
P = '\033[1;35m' # Фиолетовый
W = '\033[0m'    # Сброс цвета

os.system('clear')
print(f"""{P}
 ██████╗ ███████╗██╗███╗   ██╗████████╗    ██████╗ ██████╗ ██████╗ 
██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝    ██╔══██╗██╔══██╗██╔══██╗
██║   ██║███████╗██║██╔██╗ ██║   ██║       ██████╔╝██████╔╝██████╔╝
██║   ██║╚════██║██║██║╚██╗██║   ██║       ██╔═══╝ ██╔═══╝ ██╔═══╝ 
╚██████╔╝███████║██║██║ ╚████║   ██║       ██║     ██║     ██║     
 ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝       ╚═╝     ╚═╝     ╚═╝     
                                                                   
[ CONTRCULTURE TELEGRAM REAL-TIME VOIP SNIFFER ]
==================================================
[ by @Zxc1u , black internet ]{W}""")

print(f"\n{Y}[*] Перехватчик STUN-пакетов успешно запущен в текущем терминале.{W}")
print(f"{Y}[!] Ожидаю звонки Telegram. Лог пишется на экран и в файл...{W}\n")

captured_ips = set()

# Малая команда для моментального пробива GEO-IP по открытым базам данных
def get_ip_geo(ip_address):
    try:
        response = requests.get(f"http://ip-api.com{ip_address}", timeout=3)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "success":
                country = data.get("country", "Неизвестно")
                city = data.get("city", "Неизвестно")
                isp = data.get("isp", "Неизвестно")
                if "telegram" in isp.lower() or "digital ocean" in isp.lower():
                    return f"⚙️ СЕРВЕР ИНФРАСТРУКТУРЫ TELEGRAM ({country})"
                return f"🌍 {country}, {city} | 🏢 Провайдер: {isp}"
        return "⚙️ Служебный IP / Нет данных в GEO-базе"
    except Exception:
        return "❌ Ошибка подключения к серверу шлюза GEO-IP"

def packet_callback(packet):
    if packet.haslayer(UDP) and packet.haslayer(IP):
        payload = bytes(packet[UDP].payload)
        src_ip = packet[IP].src
        
        # Поиск сигнатуры STUN-запросов (Binding Request \ Binding Success)
        if b'\x00\x01' in payload or b'\x01\x01' in payload:
            
            # Фильтруем внутренние локальные адреса домашнего роутера (192.168.x.x, 127.0.0.1, 10.x.x.x, 172.x.x.x)
            is_local = any(src_ip.startswith(prefix) for prefix in ("192.168.", "127.", "10.", "172."))
            
            if src_ip not in captured_ips and not is_local:
                captured_ips.add(src_ip)
                
                # Автоматический запуск GEO-анализа для перехваченного инпута
                geo_info = get_ip_geo(src_ip)
                
                print(f"{G}[🎯 INTERCEPTED]: {src_ip} -> {geo_info}{W}")
                
                # Моментально дописываем улик в текстовый листок блокнота
                with open("network_dossier.txt", "a", encoding="utf-8") as f:
                    f.write(f"[+] [{time.strftime('%H:%M:%S')}] Перехвачен сетевой IP: {src_ip} ({geo_info})\n")

try:
    # Запуск прослушивания сетевой карты на UDP-протоколе в текущем окне
    sniff(filter="udp", prn=packet_callback, store=0)
except KeyboardInterrupt:
    print(f"\n{R}[*] Сессия перехвата остановлена оператором. Блокнот сохранен.{W}\n")
    sys.exit(0)
except PermissionError:
    print(f"\n{R}[─] КРИТИЧЕСКАЯ ОШИБКА: Для снайпинга интерфейса нужны root-права!{W}")
    print(f"{Y}[💡] Запустите команду строго через: sudo ...{W}\n")
    sys.exit(1)
