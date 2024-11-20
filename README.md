# Инструкция по запуску проекта airflow_k8s_operator_example

### Шаг 1: Установите Docker

1. Перейдите на [Docker официальный сайт](https://www.docker.com/products/docker-desktop) и скачайте Docker Desktop.
2. Установите Docker согласно инструкциям для вашей операционной системы.
3. Запустите Docker и убедитесь, что он работает:
   
```shell
docker --version
```

### Шаг 2: Установите Minikube

1. Перейдите на [Minikube официальный сайт](https://minikube.sigs.k8s.io/docs/start/) и следуйте инструкциям по установке Minikube для вашей операционной системы.
2. Запустите Minikube:

```shell
minikube start
```

3. Убедитесь, что Minikube запущен и работает:

```shell
minikube status
```

### Шаг 3: Добавьте Helm репозиторий с Airflow

1. Установите Helm, следуя [официальным инструкциям](https://helm.sh/docs/intro/install/).
2. Добавьте репозиторий Airflow:

```shell
helm repo add apache-airflow https://airflow.apache.org
helm repo update
```

### Шаг 4: Примените конфигурации ролей и привязок ролей

1. Выполните следующую команду для применения конфигураций ролей и привязок ролей в Kubernetes:

```shell
kubectl apply -f ./k8s/role.yaml && \
kubectl apply -f ./k8s/rolebinding.yaml
```

### Шаг 5: Установите Airflow с помощью Helm

1. Установите Airflow с помощью команды:

```shell
helm install airflow apache-airflow/airflow -f values.yaml
```
   
### Шаг 6: Удалите использованные компоненты:

```shell
minikube delete
```
