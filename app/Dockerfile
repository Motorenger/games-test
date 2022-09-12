# 
FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 
WORKDIR /app

# 
COPY ./requirements.txt .

# 
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

# 
COPY . .
