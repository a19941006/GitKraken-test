"""乾洗店客戶管理系統

資料庫：
customer_info: [name, phone_number, address, balance]
services: [上衣 長襯 短襯 POLO T恤 針織 長褲 短褲 短裙 長裙 摺裙 
小洋裝 洋裝	女外套單層 牛外	外套 夾克(薄) 外套 夾克 外套 夾克(厚) 
大外套 背心	男西裝 女西裝 羽絨 長大衣 薄床組 床組 床組 毛毯 窗簾
椅套 棉被 整燙]
price: 


服務品項：[上衣 長襯 短襯 POLO T恤 針織 長褲 短褲 短裙 長裙 摺裙 
小洋裝 洋裝	女外套單層 牛外	外套 夾克(薄) 外套 夾克 外套 夾克(厚) 
大外套 背心	男西裝 女西裝 羽絨 長大衣 薄床組 床組 床組 毛毯 窗簾
椅套 棉被 整燙]
送洗訂單：[]


流程：
1. 輸入電話或其他資訊查找客戶(Search):
    show customer_info, current_balance
    show selection:
    1-1. show historical_orders
        1-1-1. add order
            1-1-1-1. 表格添加數量, 浮動金額, 備註

        1-1-2. edit order
        1-1-3. remove order
        
    1-2. edit customer_info
    1-3. remove customer(限制條件)

2. 新客戶資料登入(input_new_data):
    2-1. input data to customer_info

3. 服務設定(Edit Service):
    show services
    3-1. add new services
    3-2. edit services
        show all services
        3-2-1. change price
        3-2-2. change service name
    3-3. remove services



會員資料新增
會員資料修改
會員資料刪除

新增訂單
修改訂單
刪除訂單

"""


import mysql.connector

# button naming
button_search = "查找客戶"
button_add_customer = "新客戶資料登錄"
button_settings = "服務設定"
button_quit = "離開並關閉"
button_error = "!錯誤輸入!"


'''MySQL'''
# connet to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="5642023808",
  database="DryCleanCRM"
)




# 1. search: 輸入電話或其他資訊查找客戶
def search():
    pass

# 2. add_customer
def add_customer():
    customer_name = input("客戶名稱(必填) >>>")
    phone_number = input("電話(必填) >>>")
    secondary_phone_number = input("備用電話 >>>")
    address = input("地址 >>>")
    
    # input to sqldb (INSERT插入資料)
    mycursor = mydb.cursor()
    sql = "INSERT INTO customer_info (phone_number, customer_name, secondary_phone_number, address) VALUES (%s, %s, %s, %s)"
    val = (f"{phone_number:s}", f"{customer_name:s}", f"{secondary_phone_number}", f"{address}")
    mycursor.execute(sql, val)
    mydb.commit()

    # show all 展示表的資料
    # mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * from customer_info WHERE phone_number={phone_number:s}")
    myresult = mycursor.fetchall()
    for x in myresult:
        pass
    pass
        

    
# 3. 設定2
def settings():
    pass




# main
quit = False
while not quit:
    print(f'1.{button_search:s} 2.{button_add_customer:s} 3.{button_settings:s} 4.{button_quit:s}')
    choice = int(input('請輸入 >>> '))
    if choice == 1:
        search()
    elif choice == 2:
        add_customer()
    elif choice == 3:
        settings()
    elif choice == 4:
        quit = True
    else:
        print(f'{button_error:s}')






