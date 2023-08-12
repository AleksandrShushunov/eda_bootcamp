FROM python:3.10-slim-buster

RUN pip install dill
RUN pip install explainerdashboard
RUN pip install scikit-learn==1.2.2
RUN pip install pandas==1.5.3

COPY app2.py ./
COPY explainer.dill ./


EXPOSE 9050
CMD ["python", "./app2.py"]
