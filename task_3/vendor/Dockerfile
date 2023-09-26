FROM python:3.9 as builder
LABEL maintainer="iv.cherepanov@yandex.ru"
WORKDIR /code/second_part

COPY requirements.txt /code/second_part/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/second_part/requirements.txt
COPY .. /code/second_part

# Указание автора в LABEL
LABEL author="Cherepanov Ivan Vladimirovich"
LABEL group="IKBO-01-20"
ENV PYTHONPATH "${PYTHONPATH}:/code/"

ONBUILD RUN echo "Сборка и запуск произведены. Автор: {Черепанов Иван Владимирович}"

# Stage 2: Запуск приложения
FROM builder as runner

# Скачивание файла с гербом
RUN wget https://www.mirea.ru/upload/medialibrary/80f/MIREA_Gerb_Colour.png -O /code/second_part/mirea_gerb.png

#RUN chmod -R 777 /code/my_volume
EXPOSE 8012
CMD [ "python", "main.py" ]