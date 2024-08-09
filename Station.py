import network

class Station:
    def __init__(self, ssid, password):
        if not ssid:
            raise ValueError("SSID must be provided")
        if not password:
            raise ValueError("Password must be provided")
        
        self.ssid = ssid
        self.password = password
        self.wlan = network.WLAN(network.STA_IF)

    def connect(self):
        """
        Connect to the WiFi network with the specified SSID and password.
        Returns True if the connection was successful, otherwise False.
        """
        try:
            self.wlan.active(True)
            self.wlan.connect(self.ssid, self.password)
            while not self.wlan.isconnected():
                pass
            print("Connected to WiFi network")
            return True
        except Exception as e:
            print(f"Error connecting to WiFi network: {e}")
            return False

    def disconnect(self):
        """
        Disconnect from the WiFi network if currently connected.
        Returns True if the disconnection was successful, otherwise False.
        """
        try:
            if self.wlan.isconnected():
                self.wlan.disconnect()
                print("Disconnected from WiFi network")
                return True
            else:
                print("Not currently connected to WiFi network")
                return True
        except Exception as e:
            print(f"Error disconnecting from WiFi network: {e}")
            return False

    def info(self):
        """
        Return information about the current WiFi connection.
        """
        if self.wlan.isconnected():
            return {
                "ssid": self.ssid,
                "password": self.password,
                "ip_address": self.wlan.ifconfig()[0],
                "subnet_mask": self.wlan.ifconfig()[1],
                "gateway": self.wlan.ifconfig()[2],
                "dns": self.wlan.ifconfig()[3]
            }
        else:
            return {
                "ssid": None,
                "password": None,
                "ip_address": None,
                "subnet_mask": None,
                "gateway": None,
                "dns": None
            }