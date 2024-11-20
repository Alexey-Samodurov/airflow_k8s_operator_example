from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator

with DAG(
        dag_id='pyspark_k8s_dag',
        schedule_interval=None,
        start_date=None,
    ) as dag:

    k = KubernetesPodOperator(
        namespace='default',
        image="samodurov/pyspark:latest",
        cmds=["/opt/spark/bin/spark-submit"],
        arguments=[
            "--master", "k8s://https://kubernetes.default.svc:443",
            "--name", "pyspark-app",
            "--deploy-mode", "cluster",
            "--conf", "spark.executor.memory=1g",
            "--conf", "spark.driver.memory=1g",
            "--conf", "spark.executor.instances=1",
            "--conf", "spark.kubernetes.executor.request.cores=0.5",
            "--conf", "spark.kubernetes.executor.limit.cores=0.5",
            "--conf", "spark.kubernetes.driver.request.cores=0.5",
            "--conf", "spark.kubernetes.driver.limit.cores=0.5",
            # "--conf", "spark.executor.cores=1",
            # "--conf", "spark.driver.cores=1",
            "--conf", "spark.kubernetes.driver.container.image=samodurov/pyspark:latest",
            "--conf", "spark.kubernetes.executor.container.image=samodurov/pyspark:latest",
            "--conf", "spark.kubernetes.container.image.pullPolicy=Always",
            "--conf", "spark.kubernetes.namespace=default",
            "local:///opt/spark/examples/src/main/python/pi.py"
        ],
        labels={"foo": "bar"},
        name="pyspark-app",
        task_id="run_pyspark_app",
        image_pull_policy="Always",
        get_logs=True,
        is_delete_operator_pod=False,
    )
