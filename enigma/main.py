import numpy as np
import enigma

def main():
    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    tupla = enigma.gerar_matrizes_de_permutacao(len(alfabeto))
    mensagem = "o bolo de chocolate fica pronto quatro horas da tarde"

    # Testando cifra simples
    cifrada = enigma.cifrar(mensagem, tupla[0])
    print(f"Mensagem cifrada: {cifrada}")
    decifrada = enigma.de_cifrar(cifrada, tupla[0])
    print(f"Mensagem decifrada: {decifrada}")

    # Testando cifra Enigma
    criptada_enigma = enigma.encriptar_enigma(mensagem, tupla[0], tupla[1])
    print(f"Mensagem criptada com Enigma: {criptada_enigma}")
    decriptada_enigma = enigma.decriptar_enigma(criptada_enigma, tupla[0], tupla[1])
    print(f"Mensagem decriptada com Enigma: {decriptada_enigma}")

if __name__ == "__main__":
    main()