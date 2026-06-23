import requests
from datetime import datetime

URL = "http://127.0.0.1:50464"


def check_application(url):
    try:
        response = requests.get(url, timeout=5)

        print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")

        if response.status_code == 200:
            print("APPLICATION STATUS: UP")
            print(f"HTTP Status Code: {response.status_code}")

        else:
            print("APPLICATION STATUS: DOWN")
            print(f"HTTP Status Code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print("\nAPPLICATION STATUS: DOWN")
        print(f"Error: {e}")


if __name__ == "__main__":
    check_application(URL)