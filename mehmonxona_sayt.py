


user = [
    {'username':'admin', 'password': 'admin1234'}
]
def anketa():
    ism = input("ismingizni kiriting:")
    familiya = input("familyangizni kiriting:")
    tel_raqam = int(input("telefon raqam kiriting:"))
    manzil = input("turar joyingizni kiriting:")
    email = input("e-mailingizni kiriting:")
    print("tabriklaymiz siz ro'yxatdan o'tdingiz!🥳🥳🥳 \n☎ biz siz bilan bog'lanamiz.")


def naqd_tolov(x):
    while True:
        print("Naqd pul orqali to'lov turini tanladingiz")
        vaqt = int(input("Nechi kun qolmoqchisiz>>> "))
        xaridor_puli = int(input("Sizda qancha pulingiz bor? "))
        if vaqt*x <= xaridor_puli:
            print(f"Tabriklaymiz siz xona bron qildingiz! \nqaytimi: {xaridor_puli-vaqt*x}")
            break
        else:
            print(f"Sizda yetarli pul miqdori yo'q ekan. \nYetmayotgan summma miqdori: {vaqt*x-xaridor_puli}")
            break

def karta_tolov(x):
    while True:
        
        vaqt = int(input("Nechi kun qolmoqchisiz>>> "))
        xaridor_puli = int(input("Sizda qancha pulingiz bor? "))
        if vaqt*x <= xaridor_puli:
            print(f"Tabriklaymiz siz xona bron qildingiz! \nqaytimi: {xaridor_puli-vaqt*x}")
            break
        else:
            print(f"Sizda yetarli pul miqdori yo'q ekan. \nYetmayotgan summma miqdori: {vaqt*x-xaridor_puli}")
            break

def karta_raqam():
    raqam = input("Karta raqamingizni oxirgi 4 ta raqamini kiriting \nSizga 2 ta imkoniyat beriladi karta raqam kiritish uchun \nKiriting: ")
    
    while True:
        if  len(raqam) == 4:
            print("To'g'ri raqam.\nTabriklaymiz siz xona band qildingiz!!!")
            break
        else:
            xato = input("XATO! Siz 4 ta raqam kiritishingiz kerak. \nYana urunib ko'ring: ")
            if len(xato) == 4:
                print("To'g'ri raqam.\nTabriklaymiz siz xona band qildingiz!!!")
                break
            return raqam


def menu():
    ishora = True
    while True:
        if ishora:
            print("\n\n\nMehmonxona saytiga xush kelibsiz!😊😊😊")
            tanlov = input("""⬇ Kerakli bo'limni tanlang ⬇
1. 🔷 Xona bron qilish 
2. 🔷 Mehmonxona haqida ma'lumot olish
3. 🔷 Admin kabinetiga kirish
4. 🔷 Dasturni to'xtatish...
Kiriting: """)
            ishora = False
        else:
            tanlov = input("Xato, 1 va 4 oralig'idagi son kiriting: ")

        if tanlov.isdigit() and int(tanlov) in range(1,5):
            return int(tanlov)

def xona_bron_qilish():
    
    while True:
        
            tanlov = input("""Qanday xonani band qilmoqchisiz:
    1. Lux xonalar
    2. Standart xonalar
    3. Ortga...
    Kiriting: """)
            
        
           
            if tanlov == '1':
                tanlov1 = input("""1. Lux xonalar haqida ma'lumot olish
    2. Lux xonalar narxlari bilan tanishish
    3. Ortga...
    Kiriting: """)
                if tanlov1 == '1':
                    print("""MA'LUMOT
    LUX HOSTEL yotoqxonasining infratuzilmasi va xizmatlari
    Mehmonlar quyidagi xizmatlardan foydalanishlari mumkin: avtoulovlar uchun to'xtash joyi, chiroyli bog ', shinam bar, tezkor Internetga kirish.
        
    Chet ellik mehmonlar uchun rus va ingliz tillarini biladigan xodimlar ishlaydi.
        
    Xonalar haqida
    LUX HOSTEL quyidagi toifadagi 5 xonani taklif qiladi: to'rt kishilik, uch kishilik xona, ikki kishilik xona, yotoqxona xonasi.
        
    Mehmonxonada konditsioner, tekis  
    ekranli televizor mavjud.""")
                    continue
                
                elif tanlov1 == '2':
                    tanlov2 = input("""Sizga necha xonali xona kerak:
    1. 1 xonali - 250$ 1 kunga
    2. 2 xonali - 500$ 1 kunga
    3. 3 xonali - 800$ 1 kunga
    4. bekor qilish.
    Kiriting:""")
                    if tanlov2 == '1':
                        anketa()
                        tolov2 = input("To'lov turini tanlang: \n1.Naqd pul orqali to'lov \n2. Karta orqali to'lov \nKiriting: ")
                        if tolov2 == '1':
                            naqd_tolov(x=250)
                            break
    
                        elif tolov2 == '2':
                            print("Karta orqali to'lov turini tanladingiz")
                            karta_tolov(x=250)
                            karta_raqam()
                            break
                    elif tanlov2 == '2':
                        anketa()
                        tolov2 = input("To'lov turini tanlang: \n1.Naqd pul orqali to'lov \n2. Karta orqali to'lov \nKiriting: ")
                        if tolov2 == '1':
                            naqd_tolov(x=500)
                            break
                        
                        elif tolov2 == '2':
                            print("Karta orqali to'lov turini tanladingiz")
                            karta_tolov(x=500)
                            karta_raqam()
                            break
                            

                    elif tanlov2 == '3':
                        anketa()
                        tolov2 = input("To'lov turini tanlang: \n1.Naqd pul orqali to'lov \n2. Karta orqali to'lov \nKiriting: ")
                        if tolov2 == '1':
                            naqd_tolov(x=800)
                            break

                        elif tolov2 == '2':
                            print("Karta orqali to'lov turini tanladingiz")
                            karta_tolov(x=800)
                            karta_raqam()
                            break
                            
                    elif tanlov2 == '4':
                        break
                elif tanlov1 == '3':
                    break
            if tanlov == '2':
                tanlov3 = input("""    1.Standart xonalar haqida ma'lumot.
    2.standart xonalar narxlari
    3.ortga..
    Kiriting: """)
                if tanlov3 == '1':
                    print("""STD (standart)- standart xona... Odatda, bu eng ko'p arzon xona mehmonxonada. Bu xonada bitta katta ikki kishilik to'shak yoki 2 kishilik yotoq va asosiy qulayliklar (televizor, telefon, dush bilan jihozlangan xususiy hojatxona, minibar) mavjud. Ushbu xonani ko'pincha dam oluvchilar tanlaydilar.""")
                    continue
                elif tanlov3 == '2':
                    tanlov4 = input("""Sizga nechi xonali xona kerak
    1. 1 xonali - 70$ 1 kunga
    2. 2 xonali - 110$ 1 kunga
    3. 3 xonali - 180$ 1 kunga
    4. bekor qilish.
    Kiriting: """)
                    if tanlov4 == '1':
                        anketa()
                        tolov2 = input("To'lov turini tanlang: \n1.Naqd pul orqali to'lov \n2. Karta orqali to'lov \nKiriting: ")
                        if tolov2 == '1':
                            naqd_tolov(x=70)
                            break

                        elif tolov2 == '2':
                            print("Karta orqali to'lov turini tanladingiz")
                            karta_tolov(x=70)
                            karta_raqam()
                            break
                            
                    elif tanlov4 == '2':
                        anketa()
                        tolov2 = input("To'lov turini tanlang: \n1.Naqd pul orqali to'lov \n2. Karta orqali to'lov \nKiriting: ")
                        if tolov2 == '1':
                            naqd_tolov(x=110)
                            break

                        elif tolov2 == '2':
                            print("Karta orqali to'lov turini tanladingiz")
                            karta_tolov(x=110)
                            karta_raqam()
                            break
                    elif tanlov4 == '3':
                        anketa()
                        tolov2 = input("To'lov turini tanlang: \n1.Naqd pul orqali to'lov \n2. Karta orqali to'lov \nKiriting: ")
                        if tolov2 == '1':
                            naqd_tolov(x=180)
                            break

                        elif tolov2 == '2':
                            print("Karta orqali to'lov turini tanladingiz")
                            karta_tolov(x=180)
                            karta_raqam()
                            break
                            
                    elif tanlov4 == '4':
                        break
                if tanlov3 == '3':
                    continue
            if tanlov == '3':
                break



def mehmonxona_haqida():

    while True:
        tanlov = input("""1. Hilton Mehmonxonasi
Hilton Mehmonxonasi! 
Tashkent City hududida barpo etilgan mehmonxona binosi 21 qavatga ega. Bu xalqaro ishbilarmonlik markazida faoliyat yuritadigan oltita mehmonxonaning birinchisi. 
Mehmonxonadagi 258 ta xonalari standart, lyuks hamda fransuz, ingliz, arab va mumtoz uslubda barpo etilgan 8 ta prezident xonalaridan iborat. Prezident lyuks xonalarining maydoni 250 kv. m bo‘lib, mehmon kutish zali, tushlik zonasi va oshxonani o‘z ichiga oladi.
Hilton Tashkent City`da tadbirlar o‘tkazish uchun beshta ko‘p tarmoqli anjumanlar zali hamda yozgi ayvonga chiqishli banket zali mavjud. Ularning umumiy maydoni 2450 kv. m ni tashkil etadi. Barcha anjumanlar zallari birinchi va ikkinchi qavatlarda joylashgan bo‘lib, tabiiy yoritish imkoniyatlariga ega.

Hilton Tashkent City tarkibida dunyoning turli mintaqalari oshxonalari bo‘lgan bir qancha restoranlar mavjud bo‘lib, ulardan biri 21-qavatda joylashgan.
   Hilton mehmonxona brendi (AQSH) bu yil o‘zining 100 yilligini nishonladi. Kompaniya butun dunyoda 585 ta mehmonxonaga ega.

«Hilton» – dunyo yorlig‘iga aylangan eng mashhur tarmoqlardan biri. «Hilton mehmonxonasi» iborasi uzoq vaqtdan beri farovonlik, hashamat va boy hayot bilan sinonim bo‘lib kelgan.
«Hilton» tarmog‘i o‘z mijozlari uchun «Hilton Honnors» sodiqlik dasturini ishlab chiqqan. Unga ko‘ra, mijozlar turar joy uchun ballarni to‘plashi mumkin.

Hilton Hotels & Resors nomli zamonaviy va progressiv mehmonxonalar mehmonnavozlik borasida shubhasiz yetakchi hisoblanadi. Bir asrlik tajribaga ega Hilton mehmonxonaning eng yaxshi an'analarini davom ettirib, mehmonlarga xizmat ko‘rsatishni innovatsion yondashuv bilan boyitib bormoqda. Olti qit'ada 585ta mehmonxonaga ega Hilton Hotels & Resors dunyoning eng mashhur joylarida o‘z mehmonxonalarini joylashtirgan.
2. ortga...
Kiriting: """)
        if tanlov == '2':
            break


def admin_bolimi():
    username = input("foydalanuvchi nomi: ")
    password = input("foydalanuvchi kodi: ")
    for users in user:
        if users['username'] == username and users['password'] == password:
            print("tabriklaymiz! Kirildi.")
            print("""bugun bizda 110 nafar inson bizning mehmonxonamizdan foydalanmoqda.
35 inson lux xonadan, 75 nafar standart xonadan foydalanmoqda.""")
        else:
            print("Kod yoki Login Xato!")
            break


while True:


    tanlov = menu()
    if tanlov == 1:
        xona_bron_qilish()
    elif tanlov == 2:
        mehmonxona_haqida()
    elif tanlov == 3:
        admin_bolimi()
    elif tanlov == 4:
        break



