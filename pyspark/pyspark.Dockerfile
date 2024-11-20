FROM apache/spark-py:v3.4.0

ARG WRKDIR=/opt/spark/work-dir

USER root

RUN \
    groupadd -r spark && \
    useradd --no-log-init -r -g spark spark && \
    chown spark:spark -R $WRKDIR

RUN \
    mkdir /opt/spark/conf && \
    mkdir /home/spark && \
    chown spark:spark /opt/spark/conf && \
    chown spark:spark /home/spark

WORKDIR $WRKDIR

COPY spark-submit /opt/spark/bin/spark-submit
#COPY requirements.txt requirements.txt
#
#RUN pip install --index-url https://nexus.samokat.io/repository/nexus-pypi-group/simple -qr requirements.txt

RUN \
    chmod +x /opt/spark/bin/spark-submit

USER spark

WORKDIR $WRKDIR

COPY --chmod=755 . ./
