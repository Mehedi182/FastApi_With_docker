FROM python:3.8
#RUN mkdir -p /code
#WORKDIR /code

COPY requirements.txt /
RUN pip install --requirement /requirements.txt

COPY ./app /app

EXPOSE 8000
CMD ["uvicorn", "app.main:app",  "--reload"]