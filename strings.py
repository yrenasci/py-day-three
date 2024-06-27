"""name = "yaren" #beş karakterli bilgi
surname = "aşcı"
age = "22"   # age = 22 diye yazarsan print'e str(age) yazman gerekir

print("my name is " + name + " " + surname + " and\n I am " + age + " years old" )
#\n alt satıra geçer"""


name = "yaren"
surname = "aşcı"
age = 22

greeting = "My name is " + name + " " + surname + "and \nI am " + str(age) + " years old"
length = len(greeting) #karakter verdik
#ilk karakter 0, sondan sayarsak -1'den başlar. Boşluklar karakter olarak sayılır

#print(greeting)  #greeting=selamlama
print(greeting[0])
print(greeting[3])
print(greeting[2]) #boşluğa denk gelir
print(len(greeting)) #greeting ifadesi kaç karakterli olduğunu söyler
print(greeting[length-1]) #son karakteri verir

print(greeting[2:5]) #2'den başla 5'e kadar yaz
print(greeting[3:7])
print(greeting[3:]) #3'ten başla son karaktere kadar ilerle
print(greeting[:15]) #baştan itibaren al 15'e kadar git
print(greeting[2:40:2]) #2'den başla 40'a git ama 2şer git adım sayısı 2 olur
print(greeting[2:50:3])