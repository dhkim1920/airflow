from datetime import timedelta

from airflow.operators.bash_operator import BashOperator
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator


def init(**kwargs):
    kwargs['ti'].xcom_push(key="test_key", value="test_value")


def create_python_task():
    return PythonOperator(
        task_id='python_task',
        python_callable=init,
        provide_context=True,
        dag=dag
    )


def create_bash_task():
    return BashOperator(
        task_id='bash_task',
        bash_command='echo "ti.xcom_pull(task_id="python_task", key="test_key")"',
        dag=dag
    )


default_dag_args = {
    'owner': 'test',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'email': ['test@test.com'],
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG('wf_create_dynamic_task',
          start_date=datetime(2020, 2, 18),
          default_args=default_dag_args,
          schedule_interval=None,
          catchup=False
          )

run_tasks = [create_python_task(), create_bash_task()]

for run_task_index in range(len(run_tasks)):
    if run_task_index not in [0]:
        run_tasks[run_task_index - 1] >> run_tasks[run_task_index]
