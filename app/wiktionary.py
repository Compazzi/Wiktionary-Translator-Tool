import requests, re
from bs4 import BeautifulSoup

def get_wiktionary_data(language, page):
    phrase = "Wiktionary does not yet have"

    url = f"https://{language}.wiktionary.org/wiki/{page}/translations"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    try:
        if f"{phrase}" in soup.find('b').text:
            url = f"https://{language}.wiktionary.org/wiki/{page}"
    except:
        pass

    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    navHead = soup.find_all(attrs={'class': 'NavHead'})
    navContent = soup.find_all(attrs={'class': 'translations'})

    # HEADER - it's the context of the entry. H is the filtered list of navHead that contains all the contexts for which there may be translation.
    H = []
    # CONTENT - it's the content, the trnaslations of the entry. C is the filtred list of navContent.
    C = []
    # ESCAPE - Those are topics that should be ignored by the program.
    E = ["descendants", "declension", "cognates", "derived term", "terms derived", "synonym", "antonym", "hyponym", "positive forms", "superlative forms", "comparative forms", "conjugation"]
    
    # Topic filter
    for title in navHead:
        if not any(e in title.text.lower() for e in E):
            try:
                if not 'pseudo' in title.parent.attrs['class']:
                        H.append(title.text)
            except:
                    H.append(title.text)

    # Replaces consecutive blank lines with a single one.
    for t in navContent:
        text = t.get_text()
        text = re.sub(r'\n+', '\n', text)
        C.append(text)

    return H, C
