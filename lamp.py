class Lamp:
    def __init__(self, name, start_channel, num_channels):
        self.name = name
        self.start_channel = start_channel
        self.num_channels = num_channels
        self.values = [0] * num_channels

    def set_channel_value(self, index, value):
        if 0 <= index < self.num_channels:
            self.values[index] = value

    def get_dmx_values(self):
        return self.values
