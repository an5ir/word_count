from collections import Counter
import logging
from typing import List, Tuple

import re
import urllib.error
from urllib.request import urlopen

from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


def extract_text_from_url(url: str) -> str:
    """Extract text within the html page for a given url.
    :param url: URl to extract text from.
    :return: textual content of a html page.
    """
    logger.info(f"Extracting text from '{url}'")
    text = ''
    try:
        with urlopen(url) as response:
            html = response.read()
    except urllib.error.HTTPError as e:
        logger.warning(e.code)
    except urllib.error.URLError as e:
        logger.warning(e.args)
    except ValueError as e:
        logger.warning(e)
    else:
        soup = BeautifulSoup(html, features="html.parser")
        # remove script and style elements
        for script in soup(["script", "style"]):
            script.extract()
        text = soup.get_text()
    finally:
        return text


def generate_word_count(text: str) -> List[Tuple]:
    """Calculates the number of word occurrences of a given text.
    :param text: String containing words.
    :return: A list of tuples with the first value of the tuple being a particular word and the second value being
        the number of time the word occurs within the text.
    """
    logger.info('generating word count')
    res = re.findall(r'[a-zA-Z_]+', text)
    word_counter = Counter(res).most_common()
    return word_counter
