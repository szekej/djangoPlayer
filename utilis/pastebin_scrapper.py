import os
import profile

import django
import requests
from bs4 import BeautifulSoup

# Ustawienie zmiennej środowiskowej dla Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject1.settings")
django.setup()

from player.models import Video


def scrape_pastebin(pastebin_url):
    response = requests.get(pastebin_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        episode_divs = soup.find_all('div', style="font: normal normal 1em/1.2em monospace; margin:0; padding:0; "
                                                  "background:none; vertical-align:top;")

        episode_title = ''
        episode_number = ''
        episode_link = ''
        for div in episode_divs:
            text = div.get_text(strip=True)
            lines = text.split('\n')
            for element in lines:
                if element and "SEZON" not in element:
                    try:
                        parts = element.split('. ', 1)
                        if len(parts) == 2 and parts[0].isdigit():
                            episode_title = parts[1]
                            episode_number = parts[0]
                        if element.startswith('http'):  # Jeśli element to link
                            episode_link = element
                    except Exception as e:
                        print(f"Error: {e}")
            # # Zapisz do bazy danych
            if episode_title and episode_number and episode_link:
                # Sprawdź, czy istnieje już rekord z takim tytułem i numerem odcinka
                video, created = Video.objects.get_or_create(title=episode_title, defaults={'video_url': episode_link})

                if not created:
                    # Rekord już istnieje, zaktualizuj jego video_url
                    video.video_url = episode_link
                    video.save()
                    print("Record updated in the database.")
                else:
                    print("New record saved to the database.")


if __name__ == "__main__":
    pastebin_url = "https://pastebin.pl/view/0ce85bfa"
    scrape_pastebin(pastebin_url)
