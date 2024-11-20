from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator

with DAG(
        dag_id='example_kubernetes_pod_operator',
        schedule_interval=None,
        start_date=None,
    ) as dag:

    k = KubernetesPodOperator(
        namespace='default',
        image="ubuntu:18.04",
        cmds=["bash", "-cx"],
        arguments=["echo", "hello world"],
        labels={"foo": "bar"},
        name="example-pod",
        task_id="run-example-pod",
        get_logs=True,
        is_delete_operator_pod=False,
    )
