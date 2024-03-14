numbers = []
while(True):
    print("Unesi broj ili Done za kraj:" )
    unos = input()
    if unos.lower() == 'done':
        break
    try:
        number = float(unos)
        numbers.append(number)
    except ValueError:
        print("Molimo unesite broj ili Done za kraj")

if len(numbers) == 0:
    print("Niste unijeli niti jedan broj ")    
else:
    print("Brojeva uneseno: " ,len(numbers))
    print("Srednja vrijednost: ",sum(numbers) / len(numbers))
    print("Minimalna vrijednost: ", min(numbers))
    print("Maximalna vrijednost: ", max(numbers))
    numbers.sort()
    print("Sortirana lista:", numbers)
