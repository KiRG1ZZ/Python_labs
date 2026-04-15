import wave
import numpy as np
import matplotlib.pyplot as plt
import time


start_time = time.time()


# Ввод имени файла
while True:
    filename = input("Введите имя wav-файла: ")

    try:
        wav_file = wave.open(filename, "rb")
        break
    except FileNotFoundError:
        print("Файл не найден. Попробуйте еще раз.")
        print()
    except wave.Error:
        print("Это не wav-файл или файл поврежден.")
        print("Попробуйте еще раз.")
        print()

# Читаем параметры файла
channels = wav_file.getnchannels()
framerate = wav_file.getframerate()
n_frames = wav_file.getnframes()
sample_width = wav_file.getsampwidth()

# Читаем звук
frames = wav_file.readframes(n_frames)
wav_file.close()

print("Файл открыт успешно.")
print("Количество каналов:", channels)
print("Частота дискретизации:", framerate, "Гц")
print("Количество отсчетов:", n_frames)
print("Глубина кодирования:", sample_width * 8, "бит")
print()

# Переводим звук в числа
if sample_width == 1:
    signal = np.frombuffer(frames, dtype=np.uint8)
    signal = signal.astype(np.int16) - 128
elif sample_width == 2:
    signal = np.frombuffer(frames, dtype=np.int16)
elif sample_width == 4:
    signal = np.frombuffer(frames, dtype=np.int32)
else:
    print("Такой формат файла программа не поддерживает.")
    input("Нажмите Enter для выхода...")
    exit()

# Если каналов несколько, берем только первый
if channels > 1:
    signal = signal[::channels]
    print("Файл не mono, поэтому взят только первый канал.")
    print()

# Если файл пустой
if len(signal) == 0:
    print("В файле нет звуковых данных.")
    input("Нажмите Enter для выхода...")
    exit()

# Ввод количества отсчетов
while True:
    n_text = input("Введите количество отсчетов для точечного графика: ")

    try:
        n = int(n_text)
    except ValueError:
        print("Нужно ввести целое положительное число.")
        print()
        continue

    if n <= 0:
        print("Число должно быть больше нуля.")
        print()
        continue

    if n > len(signal):
        print("Слишком большое число.")
        print("Будут взяты все доступные отсчеты.")
        n = len(signal)

    break

# Берем часть сигнала
part_signal = signal[:n]

# Делаем ось времени
time_axis = np.arange(len(signal)) / framerate

# 1. Точечный график
plt.figure(figsize=(10, 5))
plt.scatter(np.arange(n), part_signal, s=10)
plt.title("Точечный график дискретных отсчетов сигнала")
plt.xlabel("Номер отсчета")
plt.ylabel("Амплитуда, у.е.")
plt.grid(True)

# 2. Осциллограмма
plt.figure(figsize=(10, 5))
plt.plot(time_axis, signal)
plt.title("Осциллограмма сигнала")
plt.xlabel("Время, с")
plt.ylabel("Амплитуда, у.е.")
plt.grid(True)

# 3. Время-частотный спектр
plt.figure(figsize=(10, 5))
plt.specgram(signal.astype(float), Fs=framerate)
plt.title("Время-частотный спектр")
plt.xlabel("Время, с")
plt.ylabel("Частота, Гц")
plt.colorbar(label="Интенсивность спектра")

# 4. Гистограмма
plt.figure(figsize=(10, 5))
plt.hist(signal, bins=50)
plt.title("Гистограмма отсчетов звукового сигнала")
plt.xlabel("Амплитуда, у.е.")
plt.ylabel("Количество отсчетов")
plt.grid(True)

plt.tight_layout()
plt.show()

print()
print("Программа завершена.")
print("Время выполнения программы:", time.time() - start_time, "сек.")

input("Нажмите Enter для выхода...")