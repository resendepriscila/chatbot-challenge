FROM python:3.10
RUN mkdir src

COPY requirements.txt src
COPY app src/app
COPY main.py src
COPY .env src

WORKDIR src
RUN pip install --no-cache-dir -r requirements.txt

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en

EXPOSE 3000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]