import datetime

print('Ai, fui importado!')
print(__name__)

def que_horas_sao():
    print(f'Hora agora: {datetime.datetime.now()}')


if __name__ == '__main__':
    que_horas_sao()
