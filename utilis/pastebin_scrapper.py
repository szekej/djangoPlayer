import requests
from bs4 import BeautifulSoup

# from player.models import Video


def scrape_pastebin(pastebin_url):
    response = requests.get(pastebin_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        episode_divs = soup.find_all('div', style="font: normal normal 1em/1.2em monospace; margin:0; padding:0; "
                                                  "background:none; vertical-align:top;")

        episodes = []

        for div in episode_divs:
            # Pobierz tekst z diva
            text = div.get_text(strip=True)

            # Podziel tekst na linie
            lines = text.split('\n')

            # Sprawdź, czy linie zawierają numer odcinka i link
            if len(lines[0].split(' ')) == 2 and lines[0].split(' ')[0].lower() != "sezon":
                episode_number, episode_title = lines[0].split('. ')

                # Dodaj do listy
                episodes.append({'number': episode_number, 'title': episode_title})
                print(episodes)

        # Wyświetl wyniki
        for episode in episodes:
            print(f"Numer odcinka: {episode['number']}, Tytuł: {episode['title']}")

            # # Zapisz do bazy danych
            # video = Video(title=title, video_url=video_url, pastebin_url=pastebin_url)
            # video.save()

if __name__ == "__main__":
    pastebin_url = "https://pastebin.pl/view/0ce85bfa"  # Zastąp 'xxxxxx' właściwym identyfikatorem Pastebin
    scrape_pastebin(pastebin_url)