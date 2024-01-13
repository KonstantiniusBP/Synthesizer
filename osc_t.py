import pygame
import array
import math
import time

# Инициализация Pygame и mixer
pygame.init()
pygame.mixer.init()

# Настройки
BPM = 100
quarter_note_duration = 60.0 / BPM
volume = 0.5

# Генерация треугольной волны
def generate_triangle_wave(frequency, duration, volume):
    sample_rate = 44100
    num_samples = int(sample_rate * duration)
    samples = array.array('h', [0] * num_samples)

    for i in range(num_samples):
        t = float(i) / sample_rate
        value = int(volume * 32767.0 * (1 - 4 * abs(round(t * frequency) - t * frequency)))
        samples[i] = value

    return samples

# Воспроизведение гаммы
def play_c_major_scale():
    do_major_scale_freqs = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]

    for freq in do_major_scale_freqs:
        samples = generate_triangle_wave(freq, quarter_note_duration, volume)
        pygame.mixer.Sound(samples.tobytes()).play()
        time.sleep(quarter_note_duration)

# Воспроизведение гаммы До-мажор
play_c_major_scale()

# Завершение программы
pygame.quit()
