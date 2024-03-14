def total_euro():
    zarada = int(radni_sati)*float(satnica)
    return zarada


print("Unesite broj radnih sati:")
radni_sati = input()
print("Unesite vasu satnicu:")
satnica = input()
print("Zaradili ste:", total_euro())