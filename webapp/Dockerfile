FROM infologistix/docker-selenium-python:alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "page.py"]
