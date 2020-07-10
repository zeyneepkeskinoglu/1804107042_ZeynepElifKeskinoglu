#soru1
z={1:"Ocak",2:"Şubat",3:"Mart",4:"Nisan",5:"Mayıs ",6:"Haziran",7:"Temmuz",8:"Ağustos",9:"Eylül",10:"Ekim",11:"Kasım",12:"Aralık"}
e=int(input("Gün giriniz:"))
y=int(input("Ay giriniz:"))
n=int(input("Yıl giriniz:"))
print(e,z[y],n)

#soru2
z=int(input("Sayı değerini giriniz:"))
e=1
for y in range (z,1,-1):
    print(y)
    e=e*y
print(e)
if 9 <= z <16:
    y= 2*(e)
    print(y)
else:
    if 9 > z >= 0:
        n = 3 * e
        print(n)
    else:
        if z <= -1 or 16 < z:
            print("İşlem yapılamıyor!!!")


#soru3
def z(e,y):
  n= []
  for p in range(0,3):
    l = 0
    for i in range(0,3):
      l += e[p][i]*y[p][i]
    n.append(l)
  print(n)
f = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
k= "zeynepkeskinogluaa"
e = [[1,2,-1],
     [2,5,2],
     [-1,-2,2]]
y= []
l=0
for i in range(0,3):
    i+=i
print(e,y)

#soru 4
z = []
for e in range(1, 42):
    if e > 1:
        for y in range(2, e):
            if e % y == 0:
                break
        else:
            z.append(e)
print(z)