# لیست مهمانان دعوت شده و تعداد مجاز هر خانواده
guests = {
    "Ahmadi": 2,
    "Bagheri": 4,
    "Mortazavi": 5,
    "Hosseini": 3,
    "Mahmoodi": 4,
}

while True:
    s = input()
    if s == "End":
        break
    name, count = s.split()
    count = int(count)
    if name not in guests:
        print("Motasefane Shoma Davat Nistid!")
    elif count > guests[name]:
        print("Tedade Afrade Davat Shode Kamtar Ast!")
    elif name in guests and count <= guests[name]:
        print("Khosh Amadid!")
