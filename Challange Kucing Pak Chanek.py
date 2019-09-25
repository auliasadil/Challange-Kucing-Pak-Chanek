#Dibuat oleh Muhammad Aulia Adil
#Kelas DDP1-H, lab di Hari Senin

import math
import turtle

print('CHALLANGE KUCING PAK CHANEK')

#untuk mempermudah pengangkaan. Ini untuk harga-harga tiap warna frekuensi.
merah = 2
hijau = 3
biru = 5

#Tinggal ikutin soalnya
print('Titik pusat menara 1:')
x1 = eval(input('x1: '))
y1 = eval(input('y1: '))
radius1 = eval(input('Radius cakupan menara 1 (meter): '))
print('Titik pusat menara 2: ')
x2 = eval(input('x2: '))
y2 = eval(input('y2: '))
radius2 = eval(input('Radius cakupan menara 2 (meter): '))
print('Titik pusat menara 3: ')
x3 = eval(input('x3: '))
y3 = eval(input('y3: '))
radius3 = eval(input('Radius cakupan menara 3 (meter): '))

#STEP 1 : Cari jarak titik pusat antar lingkaran

#Antara lingkaran 1 dengan lingkaran 2
length1 = math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)
length1 = math.sqrt(length1)
#Antara lingkaran 1 dengan lingkaran 3
length2 = math.pow(x1 - x3, 2) + math.pow(y1 - y3, 2)
length2 = math.sqrt(length2)
#Antara lingkaran 2 dengan lingkaran 3
length3 = math.pow(x3 - x2, 2) + math.pow(y3 - y2, 2)
length3 = math.sqrt(length3)

#STEP 2 : Cari radius tiap-tiap lingkaran 
circle1 = math.pi * math.pow(radius1, 2)
circle2 = math.pi * math.pow(radius2, 2)
circle3 = math.pi * math.pow(radius3, 2)

#STEP 3 : Memakai dictionary untuk memudahkan pemetaan warna dan harga
#Ini semaunya merah karena anggapan dasarnya semua lingkaran tidak beririsan
warna = {radius1:'merah', radius2:'merah', radius3:'merah'}
harga = {radius1: merah, radius2: merah, radius3: merah}

#STEP 4 : Memperkirakan kemungkinan seandainya lingkran-lingkaran tersebut beririsan
#Pemikiran begini: jika jumlah jari-jari dari dua lingkaran itu lebih besar daripada jarak titik pusat kedua lingkaran tersebut,
#maka kedua lingkaran tersebut pastilah beririsan

#Ini untuk mempermudah kondisi 1
smallest = min(radius1, radius2, radius3)
biggest = max(radius1, radius2, radius3)
middle = (radius1 + radius2 + radius3) - (smallest + biggest)

#KONDISI 1 : Jika semua lingkaran beririsan
if radius1 + radius2 > length1 and radius1 + radius3 > length2 and radius2 + radius3 > length3:
    #Jika semua lingkaran tersebut memiliki jari-jari yang sama besar, maka lingkaran 1 dan lingkaran 2 akan berubah warna
    if radius1 == radius2 == radius3:
        warna[radius1] = 'biru'
        harga[radius1] = biru
        warna[radius2] = 'hijau'
        harga[radius2] = hijau
    #Jika ketiga lingkaran tersebut berbeda jari-jarinya,
    #maka yang paling kecil akan menjadi biru, kedua paling besar menjadi hijau, dan yang terbesar tetap merah
    warna[smallest] = 'biru'
    harga[smallest] = biru
    warna[middle] = 'hijau'
    harga[middle] = hijau
    #Jika lingkaran 1 diapit 2 lingkaran lain
elif radius1 + radius2 > length1 and radius1 + radius3 > length2:
    if radius1 == radius2 == radius3:
        warna[radius1] = 'hijau'
        harga[radius1] = hijau
    elif math.pow(radius1, 2) > math.pow(radius2, 2) + math.pow(radius3, 2):
        warna[radius2] = 'hijau'
        harga[radius2] = hijau
        warna[radius3] = 'hijau'
        harga[radius3] = hijau
    elif math.pow(radius1, 2) < math.pow(radius2, 2) + math.pow(radius3, 2):
        warna[radius1] = 'hijau'
        harga[radius1] = hijau
    else:
        warna[smallest] = 'biru'
        harga[smallest] = biru
        warna[middle] = 'hijau'
        harga[middle] = hijau
    #Jika lingkaran 2 diapit lingkaran lain 
elif radius1 + radius2 > length1 and radius2 + radius3 > length3:
    if radius1 == radius2 == radius3:
        warna[radius2] = 'hijau'
        harga[radius2] = hijau
    elif math.pow(radius2, 2) > math.pow(radius1, 2) + math.pow(radius3, 2):
        warna[radius1] = 'hijau'
        harga[radius1] = hijau
        warna[radius3] = 'hijau'
        harga[radius3] = hijau
    elif math.pow(radius2, 2) < math.pow(radius1, 2) + math.pow(radius3, 2):
        warna[radius2] = 'hijau'
        harga[radius2] = hijau
    else:
        warna[smallest] = 'biru'
        harga[smallest] = biru
        warna[middle] = 'hijau'
        harga[middle] = hijau
    #Jika lingkaran 3 diapit lingkaran lain 
elif radius2 + radius3 > length3 and radius1 + radius3 > length2:
    if radius1 == radius2 == radius3:
        warna[radius3] = 'hijau'
        harga[radius3] = hijau
    elif math.pow(radius3, 2) > math.pow(radius1, 2) + math.pow(radius2, 2):
        warna[radius1] = 'hijau'
        harga[radius1] = hijau
        warna[radius2] = 'hijau'
        harga[radius2] = hijau
    elif math.pow(radius3, 2) < math.pow(radius1, 2) + math.pow(radius2, 2):
        warna[radius3] = 'hijau'
        harga[radius3] = hijau
    else:
        warna[smallest] = 'biru'
        harga[smallest] = biru
        warna[middle] = 'hijau'
        harga[middle] = hijau
    #Jika hanya lingkaran 1 dan 2 yang beririsan
elif radius1 + radius2 > length1:
    warna[min(radius1, radius2)] = 'hijau'
    harga[min(radius1, radius2)] = hijau
    #Jika hanya lingkaran 1 dan 3 yang beririsan 
elif radius1 + radius3 > length2:
    warna[min(radius1, radius3)] = 'hijau'
    harga[min(radius1, radius3)] = hijau
    #Jika hanya lingakaran 2 dan 3 yang beririsan 
elif radius2 + radius3 > length3:
    warna[min(radius2, radius3)] = 'hijau'
    harga[min(radius1, radius3)] = hijau

#STEP 5 : Memberikan OUTPUT

#Ini untuk menghitung harga dari luas dan warna lingkaran tersebut
cost = circle1 * harga[radius1] + circle2 * harga[radius2] + circle3 * harga[radius3]
cost = int(cost)

#Ini memberikan menampilkan OUTPUT-nya
print('menara 1:', warna[radius1])
print('menara 2:', warna[radius2])
print('menara 3:', warna[radius3])
print('biaya: Rp%dM' % cost)

#Ini challange selanjutnya yaitu menggambarnya dengan turtle, tapi menurutku lebih susah challange di atas

#ini biar cepet makanya turtle.speed nya 0
turtle.speed(0)
#kalo 'merah' dijadiin 'red' dan seterusnya 
if warna[radius1] == 'merah':
    warna1 = 'red'
if warna[radius1] == 'hijau':
    warna1 = 'green'
if warna[radius1] == 'biru':
    warna1 = 'blue'
if warna[radius2] == 'merah':
    warna2 = 'red'
if warna[radius2] == 'hijau':
    warna2 = 'green'
if warna[radius2] == 'biru':
    warna2 = 'blue'
if warna[radius3] == 'merah':
    warna3 = 'red'
if warna[radius3] == 'hijau':
    warna3 = 'green'
if warna[radius3] == 'biru':
    warna3 = 'blue'

#Ini sebenernya tinggal pake turtle.goto() tapi waktu itu belom tau jadi pake cara ini
#Saya sarankan pake goto aja karena ini ribet

jarak1 = math.pow(x1, 2) + math.pow(y1, 2)
jarak1 = math.sqrt(jarak1)

jarak2 = math.pow(x2, 2) + math.pow(y2, 2)
jarak2 = math.sqrt(jarak2)

jarak3= math.pow(x3, 2) + math.pow(y3, 2)
jarak3= math.sqrt(jarak3)

cek_sudut1 = (x1 != 0 or y1 != 0)
if cek_sudut1:
    if x1 != 0:
        sudut1 = math.atan(y1/x1)
        sudut1 = math.degrees(sudut1)
    elif y1 < 0:
        sudut1 = -90
    else:
        sudut1 = 90
    if x1 < 0 and y1 < 0:
        sudut1 = sudut1 + 180
    elif x1 < 0:
        sudut1 = sudut1 + 180

cek_sudut2 = (x2 != 0 or y2 != 0)
if cek_sudut2:
    if x2 != 0:
        sudut2 = math.atan(y2/x2)
        sudut2 = math.degrees(sudut2)
    elif y2 < 0:
        sudut2 = -90
    else:
        sudut2 = 90
    if x2 < 0 and y2 < 0:
        sudut2 = sudut2 + 180
    elif x2 < 0:
        sudut2 = sudut2 + 180

cek_sudut3 = (x3 != 0 or y3 != 0)
if cek_sudut3:
    if x3 != 0:
        sudut3 = math.atan(y3/x3)
        sudut3 = math.degrees(sudut3)
    elif y3 < 0:
        sudut3 = -90
    else:
        sudut3 = 90
    if x3 < 0 and y3 < 0:
        sudut3 = sudut3 + 180
    elif x3 < 0:
        sudut3 = sudut3 + 180

turtle.penup()
if cek_sudut1:
    turtle.left(sudut1)
    turtle.forward(jarak1)
    turtle.right(sudut1)
turtle.forward(radius1)
turtle.left(90)
turtle.pendown()
turtle.color(warna1)
turtle.begin_fill()
turtle.circle(radius1)
turtle.end_fill()
turtle.left(90)
turtle.forward(radius1)
turtle.right(180)
turtle.penup()
turtle.home()

if cek_sudut2:
    turtle.left(sudut2)
    turtle.forward(jarak2)
    turtle.right(sudut2)
turtle.forward(radius2)
turtle.left(90)
turtle.pendown()
turtle.color(warna2)
turtle.begin_fill()
turtle.circle(radius2)
turtle.end_fill()
turtle.left(90)
turtle.forward(radius2)
turtle.right(180)
turtle.penup()
turtle.home()

if cek_sudut3:
    turtle.left(sudut3)
    turtle.forward(jarak3)
    turtle.right(sudut3)
turtle.forward(radius3)
turtle.left(90)
turtle.pendown()
turtle.color(warna3)
turtle.begin_fill()
turtle.circle(radius3)
turtle.end_fill()
turtle.left(90)
turtle.forward(radius3)
turtle.right(180)
turtle.penup()
turtle.home()

turtle.ht()


