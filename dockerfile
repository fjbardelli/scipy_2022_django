
# REVIEW Comandos para hacer el Deploy
# STUB docker build -t sypy2022 .
# STUB docker tag sypy2022 fjbardelli/sypy2022
# STUB docker push  fjbardelli/sypy2022
FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=0
ENV DEBIAN_FRONTEND=noninteractive
RUN pip install --upgrade pip
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
EXPOSE 8000
CMD ["python", "manage.py", "runserver",  "0.0.0.0:8000"]