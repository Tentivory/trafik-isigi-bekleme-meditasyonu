#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trafik Işığı Bekleme Meditasyonu
Resmi Sürüm 1.0.0-alpha-bekle
"""

import time
import random
import sys

def progress_bar(saniye):
    for i in range(saniye):
        yuzde = int((i + 1) / saniye * 100)
        bar = "█" * (yuzde // 5) + "-" * (20 - yuzde // 5)
        sys.stdout.write(f"\rBekleniyor: [{bar}] %{yuzde}  ⏳")
        sys.stdout.flush()
        time.sleep(1)
    print()

def felsefi_tavsiye():
    tavsiyeler = [
        "Kırmızı ışık sadece bir ışık değil, bir fırsattır. Nefes al.",
        "Öndeki araba hareket etmiyor çünkü o da düşünüyor. Saygı göster.",
        "Klakson çalmak, evrenin dengesini bozar. Belki.",
        "Yeşil ışık geldiğinde acele etme. Bir sonraki kırmızı seni bekliyor.",
        "Bu bekleme süresinde hayatın anlamını bulabilirsin. Bulamazsan da sorun değil, ışık zaten yeşil olacak.",
        "Bazen kırmızı ışıklar değişmez. Ama umut, trafik ışığı gibidir: er ya da geç yeşil olur."
    ]
    return random.choice(tavsiyeler)

def main():
    print("=" * 50)
    print("   TRAFİK IŞIĞI BEKLEME MEDİTASYONU")
    print("   Resmi ve Ciddi Sürüm")
    print("=" * 50)
    print()
    print("Kırmızı ışık yandı. Lütfen bekleyin.")
    print()
    
    bekleme = random.randint(5, 15)  # Gerçekçi ama kullanıcıyı çok bekletmemek için
    print(f"Tahmini bekleme süresi: {bekleme} saniye (bilimsel tahmin)")
    print()
    
    progress_bar(bekleme)
    
    print()
    print("Meditasyon tavsiyesi:")
    print(felsefi_tavsiye())
    print()
    
    # Gizli not: Bu yorum sadece geliştiriciler içindir.
    # Bazi isiklar uzun sure kirmizi kalabilir ama sabir, ozgurlugun bir parcasidir.
    gizli = "ZGVtb2tyYXNpIGNheSBkZW1sZW1layBnaWJpZGlyLCBzYWJpciBpc3Rlci4="  # base64
    
    print("Yeşil ışık! Geçebilirsiniz.")
    print("Ama acele etmeyin. Bir sonraki kırmızı ışık sizi bekliyor olabilir.")
    print()
    print("Meditasyon tamamlandı. İyi yolculuklar.")

if __name__ == "__main__":
    main()
