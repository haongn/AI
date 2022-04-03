def bai8():
    print('Nhap vao 3 canh cua 1 tam giac, tinh dien tich cua tam giac ')
    valid_triangle = False
    while not valid_triangle:
        valid_input = False
        while not valid_input:
            a = input('a = ')
            try:
                a = float(a)
                if a <= 0:
                    print('Nhap khong hop le, vui long nhap lai')
                else:
                    valid_input = True
            except ValueError:
                print('Nhap khong hop le, vui long nhap lai')

        valid_input = False
        while not valid_input:
            b = input('b = ')
            try:
                b = float(b)
                if b <= 0:
                    print('Nhap khong hop le, vui long nhap lai')
                else:
                    valid_input = True
            except ValueError:
                print('Nhap khong hop le, vui long nhap lai')


        valid_input = False
        while not valid_input:
            c = input('c = ')
            try:
                c = float(c)
                if c <= 0:
                    print('Nhap khong hop le, vui long nhap lai')
                else:
                    valid_input = True
            except ValueError:
                print('Nhap khong hop le, vui long nhap lai')
        if (a + b <= c) or (b + c <= a) or (c + a <= b):
            print('Cac so da nhap khong phai la do dai mot tam giac')
        else:
            valid_triangle = True
    p = (a + b + c)/2
    S = math.sqrt(p*(p - a)*(p - b)*(p - c))
    print('Dien tich cua tam giac la', S)