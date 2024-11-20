FROM apache/airflow:2.9.2-python3.11

USER root

COPY --chown=airflow:root ./dags/ $AIRFLOW_HOME/dags/

COPY requirements.txt requirements.txt

RUN pip3 install -qr requirements.txt

USER airflow
