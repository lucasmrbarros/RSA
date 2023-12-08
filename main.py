import hash
import rsa

public_key, private_key = rsa.key_pair()

print('Public Key', public_key)
print('Private key', private_key)

menu = True

while menu == True:
    print('1 - Cifração')
    print('2 - Decifração')
    print('3 - Assinatura de Mensagem')
    print('4 - Verificação de Autenticade')
    print('5 -  Sair')

    option = int(input())

    if option == 1:
        print('Plaintext? ')
        message = input()
        cypherd = rsa.encrypt(message, public_key)
        print(cypherd)

    elif option == 2:
        print(rsa.decrypt(cypherd, private_key))

    elif option == 3:
        print('Mensagem? ')
        message = input()

        message = message.encode()
        print(hash.sign(message, private_key))

    elif option == 4:
        print('Mensagem?')
        message = input()

        message = message.encode()

        print('Assinatura?')
        signature = int(input())

        print(hash.check(message, signature, public_key))

    elif option == 5:
        print('Execução Finalizada')
        menu = False

    else:
        print('Opção inválida')