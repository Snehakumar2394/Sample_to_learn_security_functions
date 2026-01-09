"""Simple sample app used for demonstrating GitHub security features."""
import requests


def fetch():
    resp = requests.get("https://example.com")
    print("Fetched example.com, status:", resp.status_code)


if __name__ == "__main__":
    fetch()
