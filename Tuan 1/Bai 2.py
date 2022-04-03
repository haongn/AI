import math      
import random

def bai2():
    print('Nhap 1 so nguyen, in ra hinh vuong bang dau * co kich thuoc tuong ung')
    valid_input = False
    while not valid_input:
        l = input('Nhap vao do dai (so nguyen lon hon 0): ')
        if not l.isdigit():
            print('Nhap khong hop le, vui long nhap lai')
        else:
            l = int(l)
            if l == 0:
                print('Nhap khong hop le, vui long nhap lai')
            else:
                valid_input = True

    for i in range(0, l):
        for j in range(0, l):
            print('*', end=' ')
        print()



bai2()
