import os
import re

import django
import requests
from bs4 import BeautifulSoup

# Ustawienie zmiennej środowiskowej dla Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject1.settings")
django.setup()

from player.models import Video


def scrape_pastebin(url):
    response = requests.get(url)
    episodes_dict = {}

    if response.status_code == 200:
        soup_pastebin = BeautifulSoup(response.text, 'html.parser')
        episode_divs = soup_pastebin.find_all('div', style="font: normal normal 1em/1.2em monospace; margin:0; "
                                                           "padding:0; background:none; vertical-align:top;")

        ep_title = ''
        ep_number = ''
        ep_link = ''
        for div in episode_divs:
            text = div.get_text(strip=True)
            lines = text.split('\n')
            for element in lines:
                if element:
                    try:
                        parts = element.split('. ', 1)
                        if len(parts) == 2 and parts[0].isdigit():
                            ep_title = parts[1]
                            ep_number = parts[0]
                        if element.startswith('http'):  # if element is link
                            ep_link = element
                    except Exception as e:
                        print(f"Error: {e}")

            if ep_title and ep_number and ep_link:
                episodes_dict[ep_title] = [ep_number, ep_link]

    return episodes_dict


def scrape_wiki(url):
    response = requests.get(url)
    wiki_dict = {}

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        for row in soup.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) > 1:
                title = cells[1].get_text(strip=True)
                if '[' in title:
                    title = re.sub(r"\[.*?]", "", title)
                description = cells[2].get_text(strip=True)
                if '[' in description:
                    description = re.sub(r"\[.*?]", "", description)

                wiki_dict[title] = description

    return wiki_dict


if __name__ == "__main__":
    pastebin_url = "https://pastebin.pl/view/0ce85bfa"
    wiki_url = "https://pl.wikipedia.org/wiki/Lista_odcink%C3%B3w_serialu_%C5%9Awiat_wed%C5%82ug_Kiepskich"
    pastebin_dict = scrape_pastebin(pastebin_url)
    wikipedia_dict = scrape_wiki(wiki_url)

    for (key1, value1), (key2, value2) in zip(pastebin_dict.items(), wikipedia_dict.items()):
        if key1 == key2:
            episode_title = key1
            episode_number = value1[0]
            episode_link = value1[1]
            episode_desc = value2

            Video.objects.update_or_create(
                title=f"{episode_number}. {episode_title}",
                defaults={
                    'video_url': episode_link,
                    'description': episode_desc
                }
            )
