import math
import random as rd


def bai2():
    print('Nhap 1 so nguyen, in ra hinh vuong bang dau * co kich thuoc tuong ung')
    valid_input = False
    while not valid_input:
        l = input('Nhap vao do dai (so nguyen lon hon 0): \n')
        if not l.isdigit():
            print('Nhap khong hop le, vui long nhap lai')
        else:
            l = int(l)
            if l == 0:
                print('Nhap khong hop le, vui long nhap lai')
            else:
                valid_input = True
    for i in range(0, l):
        for i in range(0, l):
            print('*', end=' ')
        print()





def bai29():
    print('Tinh giai thua cach')
    valid_input = False
    while not valid_input:
        n = input('Nhap vao so tu nhien n: \n')
        if not n.isdigit():
            print('Nhap khong hop le, vui long nhap lai')
        else:
            n = int(n)
            valid_input = True
    gt = 1
    start = 1 if (n % 2 == 1) else 2
    for i in range(start, n+1, 2):
        gt *= i
    print('Giai thua cach cua ', n, 'la', gt)


def bai44():
    print('Tinh sin(x) voi do chinh xac 0.00001')
    valid_input = False
    while not valid_input:
        x = input('x = ')
        try:
            x = float(x)
            valid_input = True
        except ValueError:
            print('Nhap khong hop le, vui long nhap lai')
    i = 1
    sum = 0
    addends = x
    while abs(addends) >= 0.00001:
        sum += addends
        addends = (-1)*addends*x*x/((i + 1)*(i + 2))
        i += 2
    print('sin(x) = ', sum)


def bai49():
    print('In ra phan tu thu n cua day truy hoi F1 = 1, F2 = 2, Fn = 5F(n-1) + 3F(n-2)')
    valid_input = False
    while not valid_input:
        n = input('Nhap vao so tu nhien n (n > 0): \n')
        if not n.isdigit():
            print('Nhap khong hop le, vui long nhap lai')
        else:
            n = int(n)
            if n == 0:
                print('Nhap khong hop le, vui long nhap lai')
            else:
                valid_input = True
    f1 = 1
    f2 = 2
    if n == 1:
        print('Phan tu can tim la ', f1)
        return
    for i in range(3, n + 1):
        temp = f1
        f1 = f2
        f2 = 5*f1 + 3*temp
    print('Phan tu can tim la ', f2)


def bai53():
    array = []
    print('Sinh ngau nhien mang n phan tu va thuc hien cac thao tac tren no')
    valid_input = False
    while not valid_input:
        n = input('Nhap vao so tu nhien n (n > 0): \n')
        if not n.isdigit():
            print('Nhap khong hop le, vui long nhap lai')
        else:
            n = int(n)
            if n == 0:
                print('Nhap khong hop le, vui long nhap lai')
            else:
                valid_input = True
    fl = input('Nhan 1 de nhap tu ban phim, nhan 2 de sinh ngau nhien ')
    valid_input = False
    while not valid_input:
        if fl == '1': # nhap tu ban phim
            valid_input = True
            for i in range(n):
                valid_input_temp = False
                while not valid_input_temp:
                    num_in = input('array[' + str(i) + '] = ')
                    try:
                        num_in = float(num_in)
                        valid_input_temp = True
                    except ValueError:
                        print('Nhap khong hop le, vui long nhap lai. ', end='')
                array.append(num_in)
        elif fl == '2': # khoi tao ngau nhien
            valid_input = True
            for i in range(n):
                array.append(rd.uniform(-100, 100))
        else: fl = input('Xin chi nhap 1 hoac 2 ')

    print('Mang', n, 'phan tu duoc khoi tao ngau nhien boi chuong trinh:')
    print(array)
    print('Phan tu lon nhat cua mang la', max(array))
    print('Phan tu nho nhat cua mang la', min(array))

    found = False
    for number in array:
        if number < 0 and str(number).endswith('6'):
            print('Phan tu am dau tien tan cung bang 6 la',number)
            found = True
            break
    if not found:
        print('Khong ton tai phan tu am co tan cung bang 6')

    min_pos = 999999
    for number in array:
        if 0 < number < min_pos:
            min_pos = number
    if min_pos == 999999:
        print('Day khong co phan tu duong')
    else:
        print('Vi tri cua phan tu duong nho nhat la',array.index(min_pos))

    print('Tong cua mang la', sum(array))
    print('Trung binh cong cua mang la', sum(array)/n)

    valid_input = False
    while not valid_input:
        x = input('Nhap 1 so de tim kiem: ')
        try:
            x = float(x)
        except ValueError:
            print('Nhap khong hop le, vui long nhap lai')
        else:
            valid_input = True
    try:
        print(x, 'nam o vi tri', array.index(x))
    except ValueError:
        print(x, 'khong co o trong mang')

    print('Sap xep mang theo thu tu tang dan')
    print(sorted(array))

    print('Sap xep mang theo thu tu giam dan')
    print(sorted(array, reverse=True))

    print('Day dao nguoc')
    print(array[::-1])

    print('Them 1 phan tu tai 1 vi tri')
    valid_input = False
    while not valid_input:
        x = input('Nhap phan tu de them: ')
        try:
            x = float(x)
        except ValueError:
            print('Nhap khong hop le, vui long nhap lai')
        else:
            valid_input = True

    valid_input = False
    while not valid_input:
        k = input('Nhap vao vi tri k de them (cac gia tri lon hon hoac bang n mac dinh chen x vao cuoi mang: \n')
        if not k.isdigit():
            print('Nhap khong hop le, vui long nhap lai')
        else:
            k = int(k)
            valid_input = True
    array.insert(k, x)
    print('Mang sau khi chen')
    print(array)

    print('Xoa phan tu tai mot vi tri')
    valid_input = False
    while not valid_input:
        k = input('Nhap vao vi tri k de xoa: \n')
        if not k.isdigit():
            print('Nhap khong hop le, vui long nhap lai')
        else:
            k = int(k)
            valid_input = True
    array = array[:k] + array[k+1:]
    print(array)

    l = 0
    s = 0
    for number in array:
        if number > 0:
            l += 1
            s += number
    print('So phan tu duong cua mang la', l)
    print('Tong cac phan tu duong cua mang la', s)

    symmetrix = True
    for i in range(n):
        if not array[i] == array[n - 1 - i]:
            symmetrix = False
            break
    if symmetrix:
        print('Mang doi xung')
    else:
        print('Mang khong doi xung')

    increasing = True
    for i in range(n - 1):
        if array[i] > array[i - 1]:
            increasing = False
            break
    if increasing:
        print('Mang duoc sap thu tu tang dan')
    else:
        print('Mang khong duoc sap thu tu tang dan')


class DIEM:
    x = y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y


class TAMGIAC:
    A = None
    B = None
    C = None
    AB = 0
    BC = 0
    CA = 0
    # binh phuong cac canh
    AB_sq = 0
    BC_sq = 0
    CA_sq = 0

    def Nhap(self):
        valid_triangle = False
        while not valid_triangle:
            print('Nhap diem A')
            valid_input = False
            while not valid_input:
                xA = input('xA = ')
                try:
                    xA = float(xA)
                    valid_input = True
                except ValueError:
                    print('Nhap khong hop le, vui long nhap lai')
                else:
                    valid_input = True
            valid_input = False

            while not valid_input:
                yA = input('yA = ')
                try:
                    yA = float(yA)
                    valid_input = True
                except ValueError:
                    print('Nhap khong hop le, vui long nhap lai')
                else:
                    valid_input = True
            self.A = DIEM(xA, yA)

            print('Nhap diem B')
            valid_input = False
            while not valid_input:
                xB = input('xB = ')
                try:
                    xB = float(xB)
                    valid_input = True
                except ValueError:
                    print('Nhap khong hop le, vui long nhap lai')
                else:
                    valid_input = True
            valid_input = False

            while not valid_input:
                yB = input('yB = ')
                try:
                    yB = float(yB)
                    valid_input = True
                except ValueError:
                    print('Nhap khong hop le, vui long nhap lai')
                else:
                    valid_input = True
            self.B = DIEM(xB, yB)

            print('Nhap diem C')
            valid_input = False
            while not valid_input:
                xC = input('xC = ')
                try:
                    xC = float(xC)
                    valid_input = True
                except ValueError:
                    print('Nhap khong hop le, vui long nhap lai')
                else:
                    valid_input = True
            valid_input = False

            while not valid_input:
                yC = input('yC = ')
                try:
                    yC = float(yC)
                    valid_input = True
                except ValueError:
                    print('Nhap khong hop le, vui long nhap lai')
                else:
                    valid_input = True
            self.C = DIEM(xC, yC)
            self.BC_sq = (self.B.x - self.C.x) * (self.B.x - self.C.x) + (self.B.y - self.C.y) * (self.B.y - self.C.y)
            self.AB_sq = (self.A.x - self.B.x) * (self.A.x - self.B.x) + (self.A.y - self.B.y) * (self.A.y - self.B.y)
            self.CA_sq = (self.C.x - self.A.x) * (self.C.x - self.A.x) + (self.C.y - self.A.y) * (self.C.y - self.A.y)
            self.BC = math.sqrt(self.BC_sq)
            self.CA = math.sqrt(self.CA_sq)
            self.AB = math.sqrt(self.AB_sq)
            h1 = self.B.x - self.A.x
            h2 = self.B.y - self.A.y
            G = 2 * (h1 * (self.C.y - self.B.y) - h2 * (self.C.x - self.B.x)) #  G == 0 thang hang
            if (G == 0) or (self.AB == 0) or (self.BC == 0) or (self.CA == 0):
                print('3 dinh da nhap khong phai la 3 dinh cua tam giac')
            else:
                valid_triangle = True

    def Xuat(self):
        print('In ra tam giac')
        print('A(' + str(self.A.x) + ', ' + str(self.A.y) + ')')
        print('B(' + str(self.B.x) + ', ' + str(self.B.y) + ')')
        print('C(' + str(self.C.x) + ', ' + str(self.C.y) + ')')

    def TinhDienTich(self):
        p = (self.AB + self.BC + self.CA)/2
        print('Dien tich cua tam giac la', math.sqrt(p*(p - self.AB)*(p - self.BC)*(p - self.CA)))

    def TinhChuVi(self):
        print('Chu vi cua tam giac la', self.AB + self.BC + self.CA)

    def TrongTam(self):
        xx = (self.A.x + self.B.x + self.C.x)/3
        yy = (self.A.y + self.B.y + self.C.y)/3
        print('Trong tam cua tam giac la (' + str(xx) + ', ' + str(yy) + ')')

    def DangTamGiac(self):
        if (self.AB_sq == self.CA_sq) and (self.AB_sq == self.BC_sq):
            print('Tam giac ABC deu')
        else:
            if self.AB_sq == self.CA_sq:
                if self.AB_sq + self.CA_sq == self.BC_sq:
                    print('Tam giac ABC vuong can tai A')
                else: print('Tam giac ABC can tai A')
            elif self.AB_sq == self.BC_sq:
                if self.AB_sq + self.BC_sq == self.CA_sq:
                    print('Tam giac ABC vuong can tai B')
                else: print('Tam giac ABC can tai B')
            elif self.CA_sq == self.BC_sq:
                if self.CA_sq + self.BC_sq == self.AB_sq:
                    print('Tam giac ABC vuong can tai C')
                else: print('Tam giac ABC can tai C')
            else: print('Tam giac ABC khong co gi dac biet')


def bai60():
    tg = TAMGIAC()
    tg.Nhap()
    tg.Xuat()
    tg.TinhDienTich()
    tg.TinhChuVi()
    tg.TrongTam()
    tg.DangTamGiac()


class complex():
    Re = 0
    Im = 0

    def __init__(self, Re, Im):
        self.Re = Re
        self.Im = Im

    def __str__(self):
        if self.Im > 0:
            if not self.Re == 0:
                return str(self.Re) + ' + ' + str(self.Im) + 'i'
            else:
                return str(self.Im) + 'i'
        elif self.Im < 0:
            if not self.Re == 0:
                return str(self.Re) + ' - ' + str(-self.Im) + 'i'
            else:
                return str(self.Im) + 'i'
        else:
            return str(self.Re)

    def __add__(self, other):
        return complex(self.Re + other.Re, self.Im + other.Im)

    def __sub__(self, other):
        return complex(self.Re - other.Re, self.Im - other.Im)

    def __mul__(self, other):
        if hasattr(other, 'Re') and hasattr(other, 'Im'):
            return complex(self.Re*other.Re - self.Im*other.Im, self.Re*other.Im + self.Im*other.Re)
        else:
            return complex(self.Re * other, self.Im * other)

    def __truediv__(self, other):
        if hasattr(other, 'Re') and hasattr(other, 'Im'):
            if other.Re == 0 and other.Im == 0:
                raise ValueError('Tried to divide by zero')
            else:
                return self*complex(other.Re, -other.Im)/(other.Re*other.Re + other.Im*other.Im)
        else:
            return complex(self.Re/other, self.Im/other)

    def poly(self, n):
        temp = self
        for i in range(1, n):
            temp = self*temp
        return temp


def bai61():
    a = complex(4, 9)
    b = complex(4, -5)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a/b)
    print(b.poly(3))


def recursive_combination(n, k):
    if n == k:
        return 1
    if k == 1:
        return n
    return recursive_combination(n - 1, k) + recursive_combination(n - 1, k - 1)


def bai68():
    print('Tinh so to hop C(n, k) bang phuong phap de quy')
    valid_input = False
    while not valid_input:
        n = input('Nhap vao so tu nhien n: \n')
        if not n.isdigit():
            print('Nhap khong hop le, vui long nhap lai')
        else:
            n = int(n)
            valid_input = True

    valid_input = False
    while not valid_input:
        k = input('Nhap vao so tu nhien k (k <= n): \n')
        if not k.isdigit():
            print('Nhap khong hop le, vui long nhap lai')
        else:
            k = int(k)
            if k > n:
                print('Nhap khong hop le, vui long nhap lai')
            else:
                valid_input = True
    print('So to hop chap', k, 'cua', n,'la', recursive_combination(n, k))


def is_equal_sum_row_and_sum_column(square_matrix, index):
    sum_row = sum(square_matrix[index])
    sum_column = 0
    for i in range(len(square_matrix)):
        sum_column += square_matrix[i][index]
    if sum_column == sum_row:
        return True
    return False


def bai71():
    with open('INPUT.TXT', 'r') as f:
        try:
            n = int(f.readline())
        except ValueError:
            print('Loi doc file xay ra o dong dau')
        matrix = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            row = f.readline()
            row = row.split('\t')
            for j in range(n):
                try:
                    matrix[i][j] = float(row[j])
                except ValueError:
                    print('Error reading file at row ' + str(i + 1) + ', column '+ str(j + 1))
    for i in range(n):
        if is_equal_sum_row_and_sum_column(matrix, i):
            print('Sum of row', i + 1, 'and column', i + 1, 'is equal')


while True:
    valid_input = False
    while not valid_input:
        num_ex = input('Nhap so cua bai de xem ket qua (2, 8, 29, 44, 49, 53, 60, 61, 68, 71)\n')
        valid_input = True
        if num_ex == '2':
            bai2()
        elif num_ex == '8':
            bai8()
        elif num_ex == '29':
            bai29()
        elif num_ex == '44':
            bai44()
        elif num_ex == '49':
            bai49()
        elif num_ex == '53':
            bai53()
        elif num_ex == '60':
            bai60()
        elif num_ex == '61':
            bai61()
        elif num_ex == '68':
            bai68()
        elif num_ex == '71':
            bai71()
        else:
            valid_input = False
            print('Hay nhap 1 trong cac so tren')
    continue_main_loop = input('Ban muon tiep tuc khong? (y/n)\n')
    if continue_main_loop == 'n':
        break