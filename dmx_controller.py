import threading
import time
import serial

class DMXController(threading.Thread):
    def __init__(self, port="COM5"):
        super().__init__(daemon=True)
        self.running = True
        self.universe = [0] * 512
        self.lock = threading.Lock()

        try:
            self.port = serial.Serial(
                port=port,
                baudrate=250000,
                bytesize=8,
                parity=serial.PARITY_NONE,
                stopbits=2,
                timeout=1
            )
        except serial.SerialException as e:
            print(f"[ERROR] Konnte Port nicht öffnen: {e}")
            self.port = None
            self.running = False

    def update_channel(self, channel, value):
        if 0 <= channel < 512:
            with self.lock:
                self.universe[channel] = value

    def run(self):
        if not self.port:
            print("[WARNUNG] Kein gültiger Port – Thread beendet sich.")
            return

        while self.running:
            with self.lock:
                self.send_dmx()
            time.sleep(0.025)

    def send_dmx(self):
        try:
            self.port.break_condition = True
            time.sleep(0.001)
            self.port.break_condition = False
            time.sleep(0.001)

            self.port.write(bytes([0] + self.universe))
        except serial.SerialException as e:
            print(f"[ERROR] Fehler beim Senden von DMX-Daten: {e}")

    def stop(self):
        self.running = False
        self.join(timeout=2)
        if self.port and self.port.is_open:
            self.port.close()
