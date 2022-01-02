from pymongo import MongoClient

if __name__=="__main__":
    con=MongoClient("localhost",27017)
    #เชื่อต่อเซิฟเวอร์

    db=con.get_database("DSIdb")
    #ระบุฐานข้อมูล

    obj=db.ไพลิน
    #ระบุข้อมูล

    result=obj.find()
    #เรียกข้อมูลมาเก็บไว้ในตัวแปร (ทั้งหมด)

    result=obj.find({" จำนวนเงิน ":"600.00"})
    #เรียกข้อมูลมาเก็บไว้ในตัวแปร (แบบมีเงื่อนไข)

    for f in result:
        print(f)
    #เรียกดูข้อมูล (ผ่านตัวแปร)
