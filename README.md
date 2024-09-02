# Enigma
Um pacote minimalista em Python

Para instalar, você pode usar uma de duas maneiras.

A primeira maneira é clonar o repositório e fazer uma instalação local:

    git clone https://github.com/RicardolCarvalho/enigma.git
    cd enigma
    pip install .

A segunda maneira é instalar direto do repositório:

    pip install git+https://github.com/RicardolCarvalho/enigma.git

Após instalar, o programa `enigma` deve estar instalado. Então, executando o comando:

    enigma

seu programa deveria imprimir as strings `Mensagem cifrada: xtjxvxtdnt rx xvbzntap btycxuzxtgmbzcxtrxcbotdbtzbcdn`
                                        `Mensagem decifrada: o bolo de chocolate fica pronto quatro horas da tarde`
                                        `Mensagem criptada com Enigma: x rlalifjsqsxaxthaicsarauywlk xiurthdlnfxvezctfzwmcim`
                                        `Mensagem decriptada com Enigma: o bolo de chocolate fica pronto quatro horas da tarde`


Se você quiser usar o pacote em um script, você pode importar o pacote e usar as funções `enigma.cifra` e `enigma.decifra`:
    
    ```python
    import enigma

    mensagem = 'o bolo de chocolate fica pronto quatro horas da tarde'
    mensagem_cifrada = enigma.cifra(mensagem)
    print(f'Mensagem cifrada: {mensagem_cifrada}')

    mensagem_decifrada = enigma.decifra(mensagem_cifrada)
    print(f'Mensagem decifrada: {mensagem_decifrada}')

    mensagem_criptada = enigma.cifra_enigma(mensagem)
    print(f'Mensagem criptada com Enigma: {mensagem_criptada}')

    mensagem_decriptada = enigma.decifra_enigma(mensagem_criptada)
    print(f'Mensagem decriptada com Enigma: {mensagem_decriptada}')
    ```