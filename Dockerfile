FROM python:3.9

WORKDIR /cloud_ass

COPY  . .
Run python -m pip install --upgrade pip 
RUN pip install nltk
CMD ["python", "python.py"]
