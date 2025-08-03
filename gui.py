import customtkinter as ctk

class DMXGUI(ctk.CTk):
    def __init__(self, lamps, dmx_controller):
        super().__init__()
        self.title("DMX Controller")
        self.geometry("800x400")
        self.lamps = lamps
        self.dmx_controller = dmx_controller

        self.build_ui()

    def build_ui(self):
        for i, lamp in enumerate(self.lamps):
            frame = ctk.CTkFrame(self)
            frame.grid(row=0, column=i, padx=20, pady=20)

            label = ctk.CTkLabel(frame, text=lamp.name)
            label.pack(pady=10)

            for j in range(lamp.num_channels):
                slider = ctk.CTkSlider(
                    frame,
                    from_=0,
                    to=255,
                    orientation="vertical",
                    command=lambda val, l=lamp, ch=j: self.update_lamp(l, ch, int(float(val)))
                )
                slider.set(0)
                slider.pack(pady=5)

    def update_lamp(self, lamp, channel_index, value):
        lamp.set_channel_value(channel_index, value)
        if self.dmx_controller:
            start = lamp.start_channel
            for i, val in enumerate(lamp.get_dmx_values()):
                self.dmx_controller.update_channel(start + i, val)
