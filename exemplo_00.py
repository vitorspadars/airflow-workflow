

from time import sleep

def primeira_atividade():
    print('primeira atividade do airflow!')
    sleep(2)

def segunda_atividade():
    print('segunda atividade do airflow!')
    sleep(2)

def terceira_atividade():
    print('terceira atividade do airflow!')
    sleep(2)


def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    print('pipeline finalizou!')


if __name__ == '__main__':
    pipeline()