import utils


def main():
    print('Eitcha, que massa!')

    nome = input('Qual o seu nome? ').strip()

    print(f'{nome}, tenha um bom dia!')
    utils.que_horas_sao()


if __name__ == '__main__':
    main()
