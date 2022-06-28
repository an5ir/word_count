from flask import render_template, flash, redirect

from app import app
from app.forms import UrlForm
from app.src.extract_data import extract_text_from_url, generate_word_count


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def url_form():
    form = UrlForm()
    url = None
    word_counter=None
    if form.validate_on_submit():
        url_str = form.url.data
        text = extract_text_from_url(url_str)
        word_counter = generate_word_count(text)
        url = {'url': url_str}
    return render_template('url_form.html',
                           title='Home',
                           url=url,
                           form=form,
                           word_count=word_counter
                           )


@app.route('/health')
def health():
    return 'healthy'