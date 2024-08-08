import network as net
import time

class AccessPoint:
    def __init__(self, ssid, password, hidden=False):
        if not ssid or len(ssid) > 32:
            raise ValueError("SSID must be between 1 and 32 characters long")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        
        self.ssid = ssid
        self.password = password
        self.hidden = hidden
        self.ap = net.WLAN(net.AP_IF)

    def start(self):
        """
        Start the Access Point with the specified SSID and password.
        Returns True if the AP started successfully, otherwise False.
        """
        try:
            self.ap.active(True)
            self.ap.config(ssid=self.ssid, password=self.password, hidden=self.hidden)
            time.sleep(1)
            if self.ap.active():
                print("Access Point started successfully")
                return True
            else:
                print("Failed to start Access Point")
                return False
        except Exception as e:
            print(f"Error starting Access Point: {e}")
            return False

    def stop(self):
        """
        Stop the Access Point if it's currently active.
        Returns True if the AP was stopped successfully, otherwise False.
        """
        try:
            if self.ap.active():
                self.ap.active(False)
                print("Access Point stopped successfully")
                return True
            else:
                print("Access Point is already stopped")
                return True
        except Exception as e:
            print(f"Error stopping Access Point: {e}")
            return False

    def info(self):
        """
        Return information about the current Access Point configuration.
        """
        if self.ap.active():
            return {
                "ssid": self.ssid,
                "password": self.password,
                "hidden": self.hidden,
                "ip": self.ap.ifconfig()[0],
            }
        else:
            print("Access Point is not active")
            return None

    def change_config(self, ssid=None, password=None, hidden=None):
        if self.ap.active():
            raise RuntimeError("Cannot change configuration while AP is active. Stop the AP first.")
        
        if ssid:
            if len(ssid) > 32:
                raise ValueError("SSID must be between 1 and 32 characters long")
            self.ssid = ssid

        if password:
            if len(password) < 8:
                raise ValueError("Password must be at least 8 characters long")
            self.password = password

        if hidden is not None:
            self.hidden = hidden

        print("Configuration updated successfully")
