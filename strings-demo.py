name = "gündüz"
surname = "çorak"
age = 36
print("My name is {}" .format(name)) #{} direkt isim yazdı
"""print("My name is {} {}" .format(name, surname))"""
print("my name is {1} {0}" .format(name ,surname)) #sıra surnmae-name oldu 1-0 bu işe yarar
print("my name is {n} {s}" .format(n=name, s=surname)) #n ve s'lere değişken atandı
print("My name is {s} {n} and I'm {a} years old." .format(n=name, s=surname, a=age))


result = 200/ 700
"""print("the result is {r:1.3}" .format(r=result)) #noktadan sonrak "3" bilgisi virgülden sonraki kaç basamak olacağını söyler. 1 ise tam kısmı söyler."""
print("the result is {r:7.3}" .format(r=result))


print(f"my name is {name} {surname} and I'm {age} years old")