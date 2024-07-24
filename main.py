import machine
import time
import i2c_lcd

# Konfigurasi I2C
i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8))  # Ganti dengan pin yang sesuai
lcd = i2c_lcd.I2cLcd(i2c, 0x27, 2, 16)  # Alamat I2C LCD (0x27) dan ukuran LCD (2 baris, 16 kolom)

def tampilkan_pesan(pesan1, pesan2):
    lcd.clear()  # Membersihkan layar
    lcd.putstr(pesan1)  # Menampilkan pesan pertama pada baris pertama
    lcd.move_to(0, 1)  # Pindah ke baris kedua
    lcd.putstr(pesan2)  # Menampilkan pesan kedua pada baris kedua

while True:
    tampilkan_pesan("Hello, World!", "ESP32 LCD")
    time.sleep(2)  # Delay 2 detik
    tampilkan_pesan("MicroPython", "on LCD 16x2")
    time.sleep(2)  # Delay 2 detik

