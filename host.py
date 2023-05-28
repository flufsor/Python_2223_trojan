import json
import os
import platform
import socket


class Host:
    """This class is used to represent the current host"""
    def __init__(self) -> None:
        self.hostname = socket.gethostname().lower().split('.')[0]
        self.details = {
            "architecture": platform.machine(),
            "cpu_cores": os.cpu_count(),
            "os": self.get_os(),
            "python_version": platform.python_version(),
        }
        self.configuration = self.get_configuration()
        self.data = self.get_previous_data()

    def get_configuration(self) -> dict:
        """Returns the configuration for the current host"""
        host_config_file = os.path.join(os.getcwd(), "repo", "config.json")
        with open(host_config_file) as host_config_file:
            data = json.load(host_config_file)
            if self.hostname in data:
                return data[self.hostname]
            else:
                return data["default"]

    def get_previous_data(self) -> dict:
        """Returns the previous data for the current host"""
        host_data_file = os.path.join(os.getcwd(), "repo", "data", f"{self.hostname}.json")
        if os.path.exists(host_data_file):
            with open(host_data_file) as host_data_file:
                return json.load(host_data_file)["data"]
        else:
            return {}

    def get_os(self) -> str:
        """Returns the current host operating system"""
        operating_system = platform.system()
        if operating_system == "Windows":
            return "Windows"
        elif operating_system == "Linux":
            return "Linux"
        elif operating_system == "Darwin":
            return "MacOS"
        else:
            return "Unknown"
