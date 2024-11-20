#!/bin/bash

docker build -t samodurov/airflow:latest -f Dockerfile . && \
docker push samodurov/airflow:latest && \
docker build -t samodurov/pyspark:latest -f pyspark/pyspark.Dockerfile pyspark && \
docker push samodurov/pyspark:latest && \
kubectl apply -f ./k8s/role.yaml && \
kubectl apply -f ./k8s/rolebinding.yaml
