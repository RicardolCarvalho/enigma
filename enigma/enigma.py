import numpy as np
from typing import Tuple

alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

def gerar_matrizes_de_permutacao(N: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Gera duas matrizes de permutação de tamanho N x N.
    """
    P = np.eye(N)
    R = np.eye(N)

    P = np.random.permutation(P)
    R = np.random.permutation(R)
    return (P, R)

def encriptar_enigma(msg: str, P: np.ndarray, E: np.ndarray) -> str:
    """
    Aplica a cifra Enigma em uma mensagem usando as matrizes de permutação P e E.
    """
    matriz_mensagem = para_one_hot(msg)
    encriptador = P
    matriz_encriptada = np.zeros_like(matriz_mensagem)

    for i in range(matriz_mensagem.shape[1]):
        matriz_encriptada[:, i] = encriptador @ matriz_mensagem[:, i]
        encriptador = E @ encriptador

    return para_string(matriz_encriptada)

def decriptar_enigma(msg: str, P: np.ndarray, E: np.ndarray) -> str:
    """
    Recupera uma mensagem cifrada usando as matrizes de permutação inversas P e E.
    """
    matriz_mensagem_encriptada = para_one_hot(msg)
    decriptador = np.linalg.inv(P)
    matriz_decriptada = np.zeros_like(matriz_mensagem_encriptada)

    for i in range(matriz_mensagem_encriptada.shape[1]):
        matriz_decriptada[:, i] = decriptador @ matriz_mensagem_encriptada[:, i]
        decriptador = decriptador @ np.linalg.inv(E)

    return para_string(matriz_decriptada)

def para_one_hot(mensagem: str) -> np.ndarray:
    """
    Converte uma mensagem em sua representação one-hot encoding.
    """
    N = len(alfabeto)
    T = len(mensagem)
    matriz_mensagem = np.zeros((N, T), dtype=int)

    for i, letra in enumerate(mensagem):
        idx = alfabeto.index(letra)
        matriz_mensagem[idx, i] = 1

    return matriz_mensagem

def para_string(M: np.ndarray) -> str:
    """
    Converte uma matriz one-hot encoding de volta para uma string.
    """
    mensagem = ""

    for i in range(M.shape[1]):
        idx = np.argmax(M[:, i])
        mensagem += alfabeto[idx]

    return mensagem

def cifrar(msg: str, P: np.ndarray) -> str:
    """
    Aplica uma cifra simples em uma mensagem usando a matriz de permutação P.
    """
    matriz_mensagem = para_one_hot(msg)
    matriz_cifrada = P @ matriz_mensagem
    return para_string(matriz_cifrada)

def de_cifrar(msg: str, P: np.ndarray) -> str:
    """
    Recupera uma mensagem cifrada usando a matriz inversa de P.
    """
    matriz_mensagem = para_one_hot(msg)
    matriz_decifrada = np.linalg.inv(P) @ matriz_mensagem
    return para_string(matriz_decifrada)