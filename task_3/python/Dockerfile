FROM python:3.11 AS builder

WORKDIR /src/
LABEL author='Solomatin Pavel Nickolaevich'
LABEL group='IKBO-01-20'

ENV PYTHONPATH '${PYTHONPATH}/src/'
ENV PSQL_PORT 5432

USER root

COPY src .
ADD requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

RUN chown -R daemon:daemon /src

ONBUILD RUN echo "Сборка и запуск произведены. Автор: Соломатин Павел Николаевич"

FROM builder AS runner

RUN mkdir /src/static
RUN wget https://www.mirea.ru/upload/medialibrary/80f/MIREA_Gerb_Colour.png -O /src/static/mirea_gerb.png

VOLUME /images
ADD 'https://www.mirea.ru/upload/medialibrary/80f/MIREA_Gerb_Colour.png' /images/MIREA_Gerb_Colour.png
EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["main.py"]
