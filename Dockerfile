FROM python:slim

RUN useradd word_count

WORKDIR /home/word_count

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY runner.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP runner.py

RUN chown -R word_count:word_count ./
USER word_count

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]