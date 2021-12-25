#Lớp thương mại điện tử Chất lượng cao (K21411C)
#Nhóm 4
#Thành viên:
#Đinh Ngọc Trà My - K214111325
#Lê Bảo Minh - K214110840
#Nguyễn Thị Trúc Quỳnh - K214110848
#Lê Nhật Thanh - K214110851
#Bài tập cuối kỳ môn Tư duy lập trình - CHƯƠNG TRÌNH HỖ TRỢ TÌM KIẾM THÔNG TIN VACCINE.

print("******  Chào mừng bạn đến với chatbot tìm hiểu về vaccine Covid-19  ******")
print("Loại 1: Moderna          Loại 2: Pfizer          Loại 3: Astrazeneca          Loại 4: Sinopharm")
print("Loại 5: Sinovac          Loại 6: Janssen         Loại 7: Novavax              Loại 8: Sputnik V")
Vaccine = ["Moderna", "Pfizer", "Astrazeneca", "Sinopharm", "Sinovac", "Janssen", "Novavax", "Sputnik V"]
hieu_qua = [94.1, 81.8, 70.4, 79.3, 49.6, 66.9, 89.3, 91]

def luachon():
    while True:
        m = str(input('Nhập stop để dừng. Nhập infor để kiếm thông tin vaccine. Nhập compare để so sánh hiệu quả: '))
        m = m.upper()  
        if m == 'STOP': 
            print('Cảm ơn bạn đã đến với chatbot. Chúc bạn có một ngày vui vẻ và chào tạm biệt!')
            break
        elif m == 'COMPARE':  # so sánh
            ss()
            continue
        elif m == 'INFOR':  # thông tin 
            thongtin()
            continue
        else:
            print('Nhập sai lệnh, vui lòng khai báo lại')  
            continue
    return
def thongtin():
    try:
        t = int(input("Bạn muốn tìm thông tin vaccine nào (Nhập số thứ tự từ 1 đến 8): "))
        if 1>t or t>8:
            raise Exception
    except:
        print("Bạn đã nhập sai")
        return
    if t == 1:
        print("Xuất xứ: Mỹ ")
        print("Nơi sản xuất: Moderna TX, Inc.")
        print("Số mũi tiêm: 2 (cách nhau 28 ngày)")
        print("Phần trăm hiệu quả: 94,1%")
        print("Chỉ định: Người trên 18 tuổi")
        print("Liều nhắc lại: Để đảm bảo được sức khỏe và tính hiệu quả của vắc xin thì liều nhắc lại nên tiêm cách liều thứ nhất từ 4-5 tuần.")
        print("Dạng bào chế: dung dịch tiêm")
        print("Cách tiêm: tiêm vào phần bắp tay")
    elif t == 2:
        print("Xuất xứ: Mỹ")
        print("Nơi sản xuất: Pfizer, Inc. và BioNTech")
        print("Số mũi tiêm: 2 (cách nhau 21 ngày)")
        print("Phần trăm hiệu quả: 81,8% - 95%")
        print("Chỉ định: Người trên 18 tuổi")
        print("Liều nhắc lại: phác đồ dự kiến với 2 lần tiêm cách nhau 3-4 tuần, để đạt được miễn dịch tối đa nên tiêm đúng lịch")
        print("Dạng bào chế: dung dịch tiêm")
        print("Cách tiêm: tiêm vào phần bắp tay")
    elif t == 3:
        print("Xuất xứ: Anh")
        print("Nơi sản xuất: Đại học Oxford và Hãng dược – AstraZeneca")
        print("Số mũi tiêm: 2 (cách nhau 28 ngày)")
        print("Phần trăm hiệu quả: 70,4% - 82,4%")
        print("Chỉ định: Người trên 18 tuổi")
        print("Dạng bào chế: dung dịch tiêm")
        print("Cách tiêm: tiêm vào phần bắp tay")
    elif t == 4:
        print("Xuất xứ: Trung Quốc ")
        print("Nơi sản xuất: Beijing Institute of Biological Products Co., Ltd")
        print("Số mũi tiêm: 2 (cách nhau 28 ngày)")
        print("Phần trăm hiệu quả: 79,3%")
        print("Chỉ định: Người trên 18 tuổi")
        print("Dạng bào chế: dung dịch tiêm")
        print("Cách tiêm: tiêm vào phần bắp tay")
    elif t == 5:
        print("Xuất xứ: Trung Quốc ")
        print("Nơi sản xuất: Công ty Sinovac Biotech")
        print("Số mũi tiêm: 2 mũi, cách nhau 2→ 4 tuần")
        print("Phần trăm hiệu quả: 49,6% - 50,7%")
        print("Chỉ định: Người trên 18 tuổi")
        print("Dạng bào chế: dung dịch tiêm")
        print("Cách tiêm: tiêm vào phần bắp tay")
    elif t == 6:
        print("Xuất xứ: Anh ")
        print("Nơi sản xuất:Công ty Janssen Vaccines ở Leiden, Hà Lan,[19] và công ty mẹ Janssen Pharmaceuticals của Bỉ phát triển ")
        print("Số mũi tiêm: 1 mũi")
        print("Phần trăm hiệu quả: 66,9% ")
        print("Chỉ định: Người trên 18 tuổi")
        print("Dạng bào chế: dung dịch tiêm")
        print("Cách tiêm: tiêm vào phần bắp tay")
    elif t == 7:
        print("Xuất xứ: Mỹ  ")
        print("Nơi sản xuất: Cavovax, Ấn Độ ")
        print("Số mũi tiêm: 2 (cách nhau 21 ngày)")
        print("Phần trăm hiệu quả: 89.3% ")
        print("Chỉ định: Người trên 18 tuổi")
        print("Dạng bào chế: dung dịch tiêm")
        print("Cách tiêm: tiêm vào phần bắp tay")
    elif t == 8:
        print("Xuất xứ: Nga  ")
        print("Nơi sản xuất: Trung tâm Dịch tễ và Vi sinh học Quốc gia Gamalaya của Nga ")
        print("Số mũi tiêm: 2 (cách nhau 21 ngày)")
        print("Phần trăm hiệu quả: 91%-91,5%")
        print("Chỉ định: Người trên 18 tuổi")
        print("Dạng bào chế: dung dịch tiêm")
        print("Cách tiêm: tiêm vào phần bắp tay")

def ss():
    print('Bắt đầu')
    try:
        so=int(input("Nhập số vaccine bạn muốn dùng để so sánh (Từ 1 đến 8 ) : "))
        if 1>so or so>8:
            raise Exception
    except:
        print("Bạn đã nhập sai")
        return
    n = len(hieu_qua)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if hieu_qua[j] < hieu_qua[j+1] :
                hieu_qua[j], hieu_qua[j+1] = hieu_qua[j+1], hieu_qua[j]
                Vaccine[j], Vaccine[j+1] = Vaccine[j+1], Vaccine[j]
    top = hieu_qua[:so]
    print("Đây là thứ tự giảm dần về hiệu quả các loại Vaccine : ", Vaccine[:so])
    print("Hiệu quả lần lượt là: ", top)
luachon()
