import sys
import heapq
from collections import Counter
import math
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1) 

# Базовый класс для кодировщика
class Encoder:
    # Методы кодирования и декодирования, оставлены нереализованными
    def encode(self, text):
        pass
    
    def decode(self, encoded_text):
        pass

# Класс для кодирования текста методом Хаффмана
class HuffmanEncoder(Encoder):
    def __init__(self):
        super().__init__()
        self.compression_coef = None  # Коэффициент сжатия
        self.huffman_dict = {}  # Словарь кодирования Хаффмана
    
    # Метод кодирования текста
    def encode(self, text):
        # Подсчет частот символов в тексте
        freq = Counter(text)
        # Построение дерева Хаффмана
        # (включает в себя построение кодов и формирование словаря кодирования)
        heap = [[weight, [char, ""]] for char, weight in freq.items()]
        heapq.heapify(heap)
        while len(heap) > 1:
            lo = heapq.heappop(heap)
            hi = heapq.heappop(heap)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        codes = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
        self.huffman_dict = {char: code for char, code in codes}
        # Кодирование текста с использованием Хаффмана
        encoded_text = ''.join(self.huffman_dict[char] for char in text)
        # Рассчет коэффициента сжатия
        self.setCompressionCoef(text)
        return encoded_text
    
    # Метод декодирования текста
    def decode(self, encoded_text):
        decoded_text = ''
        current_code = ''
        # Декодирование текста с использованием словаря кодирования Хаффмана
        for bit in encoded_text:
            current_code += bit
            for char, code in self.huffman_dict.items():
                if code == current_code:
                    decoded_text += char
                    current_code = ''
                    break
        return decoded_text
    
    # Метод для вычисления коэффициента сжатия
    def setCompressionCoef(self, text):
        total_chars = len(text)
        huffman_encoded_length = sum(len(self.huffman_dict[char]) for char in text)
        original_length = total_chars * 8
        self.compression_coef = original_length / huffman_encoded_length
    
    # Метод для получения коэффициента сжатия
    def getCompressionCoef(self):
        return self.compression_coef

    # Метод кодирования текста методом Лемпеля-Зива
    def lz77_encode(self, text, window_size=1024):
        encoded_text = []
        window = ""
        i = 0
        while i < len(text):
            length = 0
            offset = 0
            while i - offset >= 0 and length < window_size:
                substring = text[i:i + length + 1]
                if substring in window:
                    offset = window.rindex(substring)
                    length += 1
                else:
                    break
            if length > 0:
                encoded_text.append((length, i - offset))
                window += text[i:i + length]
                i += length
            else:
                encoded_text.append((0, 0))
                window += text[i]
                i += 1
            if len(window) > window_size:
                window = window[-window_size:]
        return encoded_text


test_string = "Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991."

# Создание объекта кодировщика Хаффмана
huffman_encoder = HuffmanEncoder()

# Кодирование текста методом Хаффмана
encoded_text = huffman_encoder.encode(test_string)
# Декодирование закодированного текста
decoded_text = huffman_encoder.decode(encoded_text)
# Получение коэффициента сжатия
compression_coef = huffman_encoder.getCompressionCoef()

# Вывод результатов
print("Исходный текст:", test_string)
print("Закодированный текст с использованием Хаффмана:", encoded_text)
print("Раскодированный текст с использованием Хаффмана:", decoded_text)
print("Коэффициент сжатия методом Хаффмана:", compression_coef)

# Кодирование текста методом Лемпеля-Зива
lz77_encoded_text = huffman_encoder.lz77_encode(test_string)
print("Закодированный текст методом Лемпеля-Зива:", lz77_encoded_text)
