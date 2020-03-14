from datetime import timedelta

from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models.variable import Variable
from datetime import datetime


def variables_test(**kwargs):
    print("create variable")
    Variable.set("test_1_key", "test_1_value")

    print("get variable")
    print(Variable.get("test_1_key"))

    print("update variable")
    Variable.set("test_1_key", "test_1_value_update")

    print("create json variable")
    Variable.set("test_json_key", '{"key": "value", "key2":"value2"}')

    print("get json variable")
    print(Variable.get("test_json_key", deserialize_json=True)['key'])
    print(Variable.get("test_json_key", deserialize_json=True)['key2'])


default_dag_args = {
    'owner': 'test',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'email': ['test@test.com'],
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG('wf_variables',
          start_date=datetime(2020, 2, 18),
          default_args=default_dag_args,
          schedule_interval=None,
          catchup=False
          )

python_task = PythonOperator(
        task_id='python_task',
        python_callable=variables_test,
        provide_context=True,
        dag=dag
    )

python_task