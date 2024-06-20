# 
FROM python:3.9

# 
WORKDIR /docker-compose

# 
COPY ./requirements.txt /docker-compose/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /docker-compose/requirements.txt

# 
COPY ./app /docker-compose/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]