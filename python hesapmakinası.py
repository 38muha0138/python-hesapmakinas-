from types import resolve_bases


print("Hesap Makinası Sistemi @MRPİRATE")
ilkgirileceksayı=input("ilk sayı : ")
yapılacakişlem=input("yapılacak işlem : ")
ikincisayı=input("ikinci sayınızı giriniz : ")
if yapılacakişlem=="+" :
    print("sonuç ",ilkgirileceksayı+ikincisayı)
elif yapılacakişlem=="-" :
    print("sonuç ", ilkgirileceksayı-ikincisayı)   
elif yapılacakişlem=="*" :
    print("sonuç ",ilkgirileceksayı*ikincisayı)
elif yapılacakişlem=="**":
    print("sonuç ",ilkgirileceksayı**ikincisayı)
elif yapılacakişlem=="/":
    print(ilkgirileceksayı/ikincisayı)
else :
    print("Lütfen Geçerli Bir İşlem yapınız ")