"""
##### ERP GUI 庫存管理系統（View） ###
"""
import time
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messageBox
from tkcalendar import DateEntry
import erp_sqlite


class Product(object):
    list1 = ["id","品項", "品牌", "產品價格", "進貨量", "儲藏條件", "所在地", "進貨人員", "進貨日期"]

    coffee_items = ["A品項", "B品項", "C品項"]

    coffee_manufacturer=["A品牌","B品牌","C品牌"]

    locationValue_items=["A倉庫","B倉庫","C倉庫"]

    def __init__(self,item,brand,price,purchase,store,location,member,date):
        self.productItem = item             # 品項
        self.productBrand = brand           # 品牌
        self.productPrice = price           # 價格
        self.productPurchase = purchase     # 進貨量
        self.productStore = store           # 儲藏條件
        self.productLocation = location     # 所在地
        self.productMember = member         # 進貨人員
        self.productDate = date             # 進貨日期

    def info(self):
        list1 = [self.productItem,self.productBrand,self.productPrice,self.productPurchase,
                 self.productStore,self.productLocation,self.productMember,self.productDate]
        return list1

win = tk.Tk()
win.wm_title("coffee庫存管理系統")
win.resizable(width=False, height=False) # 步驟4：設定主視窗可以被調整大小
win.minsize(width=650, height=480)      #  最小尺寸
win.maxsize(width=650, height=480)      #  最大尺寸
win.configure(bg="#c9d6df")

def tree_viewupdate():
    # 清空
    x = tree.get_children()
    for item in x:
        tree.delete(item)

    # SQL抓取 匯入資料
    for row in erp_sqlite.erpsql_SELECT():
        list1 = row
        tree.insert("", tk.END, values=list1)  # 插入資料

# button command
def addData():
    global newProduct
    newProduct = Product(item=itemChooseValue.get(),brand=brandChooseValue.get(),price=priceEntryInt.get(),
                         purchase=purchaseValue.get(),store=storeValue.get(),location=locationValue.get(),
                         member=memberChooseValue.get(),date=timeLabelValue.get())
    result = messageBox.askquestion("再次確認", "是否確定訂貨?")  # 詢問問題
    if result == "yes":

        # tree.insert("", tk.END, values=newProduct.info())

        erp_sqlite.erpsql_INSERT(newProduct.info())
        tree_viewupdate()
    else:
        None

def changeData():
    global changeProduct
    # global temp
    changeProduct = Product(item=itemChooseValue.get(), brand=brandChooseValue.get(), price=priceEntryInt.get(),
                         purchase=purchaseValue.get(), store=storeValue.get(), location=locationValue.get(),
                            member=memberChooseValue.get(),date=timeLabelValue.get())

    result = messageBox.askquestion("再次確認", "是否確定修改?")  # 詢問問題
    if result == "yes":

        item = tree.item(tree.selection())
        record = item["values"]
        erp_sqlite.erpsql_UPDATE(changeProduct.info(),record[0])
        tree_viewupdate()
    else:
        None

def delectData():
    result = messageBox.askquestion("再次確認", "是否確定刪除?")  # 詢問問題
    if result == "yes":
        #多選刪除
        for selectedItem in tree.selection():
            item = tree.item(selectedItem)
            record = item["values"]
            erp_sqlite.erpsql_DELETE(record[0])
        tree_viewupdate()
    else:
        None

def openCal():
    # 時間表
    global btn
    win2 = tk.Tk()
    win2.wm_title("進貨日期選擇")
    cal = DateEntry(win2, selectmode='day')    # 要用DateEntry才可以strftime

    cal.pack(pady=5)

    def grad_date():
        global timeLabelValue
        time.gmtime()
        dt = cal.get_date()
        str1=dt.strftime("%Y-%m-%d")
        timeLabelValue.set(str1)
        win2.destroy()
    btn = tk.Button(win2, text="選擇", command=grad_date).pack()
    win2.mainloop()


# label
label1 =tk.Label(win,bg="#c9d6df",text="品項:").place(x=20,y=40)
label2 =tk.Label(win,bg="#c9d6df",text="品牌:").place(x=170,y=40)
label3 =tk.Label(win,bg="#c9d6df",text="進貨量:").place(x=20,y=100)
label4 =tk.Label(win,bg="#c9d6df",text="價格:").place(x=320,y=40)
label5 =tk.Label(win,bg="#c9d6df",text="儲藏條件:").place(x=200,y=100)
label6 =tk.Label(win,bg="#c9d6df",text="所在地:").place(x=410,y=100)
label7 =tk.Label(win,bg="#c9d6df",text="進貨人員:").place(x=435,y=40)
timeLabelValue = tk.StringVar()
timeLabelValue.set(time.strftime("%Y-%m-%d"))
timeLabel=tk.Label(win,bg="#c9d6df",text="",textvariable=timeLabelValue).place(x=120,y=180)

# combobox

itemChooseValue = tk.StringVar()
itemChooseValue.set(Product.coffee_items[0])
itemChoose = ttk.Combobox(win, width=8, textvariable=itemChooseValue)
itemChoose["values"] = (Product.coffee_items)   # 下拉式選單內容
itemChoose.place(x=60,y=40,width=100)                                                     # 放置位置
brandChooseValue = tk.StringVar()
brandChooseValue.set(Product.coffee_manufacturer[0])
brandChoose = ttk.Combobox(win, width=8, textvariable=brandChooseValue)
brandChoose["values"] = (Product.coffee_manufacturer)   # 下拉式選單內容
brandChoose.place(x=210,y=40)
memberChooseValue = tk.StringVar()
memberChooseValue.set("A")
memberChoose = ttk.Combobox(win, width=8, textvariable=memberChooseValue)
memberChoose["values"] = ("A","B","C")   # 下拉式選單內容
memberChoose.place(x=510,y=40)


# entry
priceEntryInt = tk.IntVar()
priceEntry=tk.Entry(win,width=8,textvariable=priceEntryInt)        # 新增輸入框Entry
priceEntry.place(x=350, y=40)

# spinbox
purchaseValue = tk.StringVar(value=0)      # 初始值為0
purchaseSpin = ttk.Spinbox(win,values = (0, 50, 100, 150, 200, 250, 300),width=8,textvariable=purchaseValue,wrap=True)        # 按完會再重複
purchaseSpin.place(x=70,y=100)

# radiobutton
storeValue = tk.StringVar()       # 元件的變數 String字串
storeValue.set("常溫")
tk.Radiobutton(win, bg="#c9d6df",text="常溫",variable=storeValue, value="常溫").place(x=270,y=100)
tk.Radiobutton(win, bg="#c9d6df",text="冷藏",variable=storeValue, value="冷藏").place(x=270,y=120)
tk.Radiobutton(win, bg="#c9d6df",text="冷凍",variable=storeValue, value="冷凍").place(x=270,y=140)

locationValue = tk.StringVar()       # 元件的變數 String字串
locationValue.set(Product.locationValue_items[0])
tk.Radiobutton(win, bg="#c9d6df",text=Product.locationValue_items[0],variable=locationValue, value=Product.locationValue_items[0]).place(x=470,y=100)
tk.Radiobutton(win, bg="#c9d6df",text=Product.locationValue_items[1],variable=locationValue, value=Product.locationValue_items[1]).place(x=470,y=120)
tk.Radiobutton(win, bg="#c9d6df",text=Product.locationValue_items[2],variable=locationValue, value=Product.locationValue_items[2]).place(x=470,y=140)

# btn
btn1=tk.Button(win,text="新增產品",command=addData).place(x=340,y=200)
btn2=tk.Button(win,text="修改產品",command=changeData).place(x=420,y=200)
btn3=tk.Button(win,text="刪除產品",command=delectData).place(x=500,y=200)
btn4=tk.Button(win,text="進貨日期",command=openCal).place(x=20,y=180)

# tree
columns = Product.list1      # 欄位名稱
tree = ttk.Treeview(win,columns=columns, show="headings")
tree.place(x=20,y=250,width=595,height=200)

for i in columns:
    tree.heading(i, text=i)             # 欄位文字設定
    tree.column(i, minwidth=0, width=60)
tree.column(0,width=30)
tree.column(7,width=30)
tree.column(8,width=80)

# 插入資料 MySQL
for row in erp_sqlite.erpsql_SELECT():
    list1=row
    tree.insert("", tk.END, values=list1)      # 插入資料

def itemSelected(event):
    for selectedItem in tree.selection():
        item = tree.item(selectedItem)
        record = item["values"]
        id= record[0]
        itemChooseValue.set(record[1])
        brandChooseValue.set(record[2])
        priceEntryInt.set(record[3])
        purchaseValue.set(record[4])
        storeValue.set(record[5])
        locationValue.set(record[6])
        memberChooseValue.set(record[7])
        timeLabelValue.set(record[8])



tree.bind("<<TreeviewSelect>>", itemSelected) # 綁定事件 選取時

# Scrollbar
vsb = ttk.Scrollbar(win, orient="vertical", command=tree.yview)
vsb.place(x=615,y=250, height=200)

tree.configure(yscrollcommand=vsb.set)

win.mainloop()