from lamp import Lamp
from dmx_controller import DMXController
from gui import DMXGUI

def main():
    # Lampen definieren
    lamp1 = Lamp("RGB Spot 1", 0, 3)
    lamp2 = Lamp("RGB Spot 2", 8, 3)

    # DMX Controller starten
    controller = DMXController("COM5")  # ← HIER Port anpassen
    controller.start()

    # GUI starten
    app = DMXGUI([lamp1, lamp2], controller)

    try:
        app.mainloop()
    finally:
        print("[INFO] GUI beendet – DMX-Thread wird gestoppt.")
        controller.stop()

if __name__ == "__main__":
    main()
