import random
import time

#exemple d un trafic resau dans ce dictionnaire 
trafic_simulation = [
    {"ip": "192.168.0.10", "pays": "France", "volume_mo": 5, "port": 443},
    {"ip": "203.0.113.5", "pays": "États-Unis", "volume_mo": 12, "port": 80},
    {"ip": "45.76.190.1", "pays": "Russie", "volume_mo": 50, "port": 22},
    {"ip": "203.0.113.5", "pays": "États-Unis", "volume_mo": 8, "port": 443},
    {"ip": "45.76.190.1", "pays": "Russie", "volume_mo": 75, "port": 22},
    {"ip": "45.76.190.1", "pays": "Russie", "volume_mo": 90, "port": 22},
    {"ip": "10.0.0.5", "pays": "France", "volume_mo": 2, "port": 443},
]

# Seuils de détection 
volume_max_par_ip = 100  #
ips_suspectes = set()
trafic_par_ip = {}

print("Analyse en cours...\n")

for flux in trafic_simulation:
    ip = flux["ip"]
    pays = flux["pays"]
    volume = flux["volume_mo"]
    port = flux["port"]

    # Cumul du trafic
    if ip not in trafic_par_ip:
        trafic_par_ip[ip] = 0
    trafic_par_ip[ip] += volume

    # Détection
    if trafic_par_ip[ip] > volume_max_par_ip and pays != "France":
        if ip not in ips_suspectes:
            print(f"[ALERTE] Activité suspecte détectée !")
            print(f" - IP étrangère : {ip} ({pays})")
            print(f" - Trafic total : {trafic_par_ip[ip]} Mo")
            print(f" - Port ciblé : {port}\n")
            ips_suspectes.add(ip)

    time.sleep(0.5)

print("Analyse terminée.")
