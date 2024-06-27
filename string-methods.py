message ="Hello There. My name is X"
"""message = message.upper() #karakter büyük harfe çevrilir
message = message.lower() #karakter küçüğe döner
message = message.title() #baş harfler büyür
message = message.capitalize() #tek baş büyür"""
message = message.strip() #boşluk yok olur"""
"""message = message.split(".")""" #ayrılırlar ve tırnak açılır
"""message = " " .join(message)""" #harf arası boşluk
"""message = "*" .join(message)""" #harf arası yıldız 
index = message.find("X")
print(index)
print(message)
isFound = message.startswith("H")
print(isFound) #H ile başlayan var mı diye sorulur t/f cevavı alınır (t)
isFound = message.startswith("K")
print(isFound) #false verdi
message = message.replace("X" , "Yaren") #x yerine yaren yazıldı
message = message.replace("y" , "k") #y yerine k yazdı
message = message.center(50, "*") #50 karakterlik boşluk açılır boşluklara * eklenir
print(message)

#print(message[2])
#print(message[1])

#dökumanlar da mevcut orada daha fazla metod var
