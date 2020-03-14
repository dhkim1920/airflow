from datetime import timedelta

from airflow.operators.bash_operator import BashOperator
from airflow.models import DAG
from datetime import datetime


def create_bash_task(task_index):
    return BashOperator(
        task_id='bash_task' + str(task_index),
        bash_command='echo 1',
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
          catchup=False,
          )

run_tasks = []
for index in range(0, 3):
    run_tasks.append(create_bash_task(index))

for run_task_index in range(len(run_tasks)):
    if run_task_index not in [0]:
        run_tasks[run_task_index - 1] >> run_tasks[run_task_index]
