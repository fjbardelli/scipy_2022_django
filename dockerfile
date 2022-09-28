
# REVIEW Comandos para hacer el Deploy
# STUB docker build -t scipy2022 
# STUB docker tag scipy2022 fjbardelli/scipy2022
# STUB docker push  fjbardelli/scipy2022
FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=0
ENV DEBIAN_FRONTEND=noninteractive
# RUN apt update  && apt upgrade  -y && apt install nano mysqlclie 
RUN pip install --upgrade pip
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
EXPOSE 8000
CMD ["python", "manage.py", "runserver",  "0.0.0.0:8000"]