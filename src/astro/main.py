"""A simple script to stay in touch with the space."""

import datetime
import shutil
from pathlib import Path

import requests
from bs4 import BeautifulSoup


def main() -> None:
    """Downloads the NASA picture of the day and shows it with gwenview."""
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    url = "https://apod.nasa.gov/"
    path = Path("/home/pavel/Pictures/nasa") / Path(f"{date}.jpg")
    path_pod = Path("/home/pavel/Pictures/nasa/picture_of_the_day.jpg")

    response = requests.get(url, timeout=15)
    soup = BeautifulSoup(response.text, "html.parser")
    img = soup.find("img")
    src = img.attrs["src"]
    alt = img.attrs["alt"]

    print(alt)
    response = requests.get(f"{url}{src}", stream=True, timeout=15)
    with open(path, "wb") as f:
        for chunk in response:
            f.write(chunk)
    shutil.copyfile(path, path_pod)
        

if __name__ == "__main__":
    main()
