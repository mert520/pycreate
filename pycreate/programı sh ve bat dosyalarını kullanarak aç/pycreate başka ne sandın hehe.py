import os

print("Python dosyası oluşturucu")

klasor = input("Dosyanın oluşturulacağı klasör yolu: ")
dosya_adi = input("Dosya adı: ")

if not dosya_adi.endswith(".py"):
    dosya_adi += ".py"

yol = os.path.join(klasor, dosya_adi)

if os.path.exists(yol):
    print("Bu dosya zaten var!")
else:
    open(yol, "w").close()
    print("Dosya oluşturuldu:", yol)

input("Çıkmak için Enter'a bas...")