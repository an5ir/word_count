import pytest
import mock
import codecs
import os
from os.path import join


from app.src.extract_data import extract_text_from_url, generate_word_count


@mock.patch('app.src.extract_data.urlopen')
def test_extract_text_from_url_exceptions(urlopen, caplog):
    from urllib.error import URLError, HTTPError
    urlopen.side_effect = [URLError('urlError'), ValueError('valueError'), HTTPError('httpError', 500, 'httpError', 'httpError', '')]

    text=extract_text_from_url('url')
    assert text==''
    assert 'urlError' in caplog.text
    urlopen.assert_called_with('url')

    caplog.clear()
    text = extract_text_from_url('url')
    assert text == ''
    assert 'valueError' in caplog.text

    caplog.clear()
    text = extract_text_from_url('url')
    assert text == ''
    assert '500' in caplog.text


@mock.patch('app.src.extract_data.urlopen')
def test_extract_text_from_url_read(urlopen):
    path = os.path.dirname(os.path.abspath(__file__))
    html = codecs.open(join(path, "test.html"), 'r').read()
    class MockRead():
        def read(self):
            return html
    urlopen.return_value.__enter__.return_value = MockRead()
    text = extract_text_from_url('')
    assert all([val in text for val in ['Title', 'header', 'some paragraph']])
    assert all([val not in text for val in ['lightblue', 'x = 5']])


def test_generate_word_count():
    text = 'a\na a the! the hi.  '
    expected_word_count = [('a', 3), ('the', 2), ('hi',1)]
    word_count = generate_word_count(text)
    assert expected_word_count == word_count
