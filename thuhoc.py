def songuyento(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
so = int(input("nhap so: "))
if so > 0 and songuyento(so):
    print(f"{so} la so nguyen to.")
else:
    print(f"{so} ko phai so nguyen to.")
# bai nay la check xem co phai so nguyen to khong
