from datetime import datetime
import time
import serial

PORTA_SERIALE = "COM3"
BAUD_RATE = 9600
NOME_FILE = "dati_sensore.csv"

try:
  with open(NOME_FILE, "x", encoding="utf-8-sig") as f:
    f.write("Timestamp;Temperatura (°C);Luminosità(%)\n")
except FileExistsError:
  pass

print(f"Connessione a {PORTA_SERIALE} in corso...")
ser = serial.Serial(PORTA_SERIALE, BAUD_RATE, timeout=1)
time.sleep(2)  # Attende il reset di Arduino
print("In ascolto dei dati... Premi Ctrl+F2 per fermare.")

try:
  while True:
    linea = ser.readline().decode("utf-8-sig", errors="ignore").strip()


    if linea:
      parti = linea.split(";")

      if len(parti) == 2:
        temperatura = parti[0]
        luce = parti[1]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Temperatura registrata: {temperatura} °C | Luminosità: {luce}")

        with open(NOME_FILE, "a", encoding="utf-8-sig") as f:
          f.write(f"{timestamp};{temperatura};{luce}\n")

except KeyboardInterrupt:
  ser.close()
  print("\nRegistrazione interrotta e file salvato con successo!")
