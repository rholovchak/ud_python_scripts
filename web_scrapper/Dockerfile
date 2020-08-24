FROM python:3.8.5-alpine3.12

WORKDIR /project
ADD . /project
RUN pip install bs4 flask

CMD ["python","rest_task.py"]
