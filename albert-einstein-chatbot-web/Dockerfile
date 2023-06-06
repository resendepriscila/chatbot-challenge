FROM python:3.10

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . chatbot
WORKDIR /chatbot

EXPOSE 8000

ENTRYPOINT ["python", "chatbot/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]