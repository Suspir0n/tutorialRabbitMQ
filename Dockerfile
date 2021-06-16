FROM python:3
ADD requeriments.txt /app/requeriments.txt
WORKDIR /app/
RUN pip install -r requeriments.txt
ENTRYPOINT ["python"]
ENV FLASK_APP=app.py
CMD ["-m" , "flask", "run", "--host=0.0.0.0"]