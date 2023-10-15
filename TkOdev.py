from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Product Class, Table Product Class
class Product():
    def __init__(self, id, productName, productType, productReleaseDate, productPrice, productBrand, productPriceRange, productOS, productAvailable):
        self.ID = id # +
        self.productName = productName # +
        self.productType = productType # +
        self.productPrice = productPrice # +
        self.productReleaseDate = productReleaseDate
        self.productBrand = productBrand # +
        self.productPriceRange = productPriceRange
        self.productOS = productOS # +
        self.productAvailable = productAvailable

    def __str__(self):
        return (f"ID: {self.ID}\nName: {self.productName}\nType: {self.productType}\nPrice: {self.productPrice}\n"
                f"Realese Date: {self.productReleaseDate}\nBrand: {self.productBrand}\nRange: {self.productPriceRange}\n"
                f"OS: {self.productOS}\nAvailable: {self.productAvailable}")

    def FixProductForMyProductFile(self):
        return f"{self.ID},{self.productName},{self.productType},{self.productPrice},{self.productReleaseDate},{self.productBrand},{self.productPriceRange},{self.productOS},{self.productAvailable}"
    def getProperties(self):
        return [self.ID, self.productName, self.productBrand, self.productPrice, self.productType, self.productOS]

class TableProduct():
    def __init__(self, id, productName, productBrand, productPrice, productType, productOS):
        self.ID = id
        self.productName = productName
        self.productBrand = productBrand
        self.productPrice = productPrice
        self.productType = productType
        self.productOS = productOS

    def getProperties(self):
        return f"{self.ID}", f"{self.productName}", f"{self.productBrand}", f"{self.productPrice}", f"{self.productType}", f"{self.productOS}"




# MyProduct.txt Codes
productList = list()
myContent: str
lastId: int
# open('MyProduct.txt', mode='w') as createTextFile:
#    createTextFile.close()




# Some Helper Defines
def getLastId():
    with open('MyProduct.txt', mode='r') as getLastIdFromTxt:
        myContent = getLastIdFromTxt.read()
    count = 0
    if myContent != 0:
        for _count, line in enumerate(myContent.split('\n')):
            count += 1
        getLastIdFromTxt.close()
        return count
    else:
        getLastIdFromTxt.close()
        return 0

def fixTheString(text = str()):
    text = text.replace('Ü', 'U').replace('ü', 'u').replace("ı", "i").replace("İ", "I").replace("Ğ", "G").replace("ğ", "g").replace("Ş", "S").replace("ş", "s").replace("Ö", "O").replace("ö", "o").replace("Ç", "C").replace("ç", "c")
    return text

lastId = getLastId()

def ClearAllTable():
    for line in productTable.get_children():
        productTable.delete(line)

def GetUserFromTextFile():
    if len(productList) == 0:
        myProductContent: str
        with open('MyProduct.txt', mode='r') as getProducts:
            myProductContent = getProducts.read()
            for line in myProductContent.split('\n'):
                properties = list()
                for property in line.split(','):
                    properties.append(property)
                product = Product(properties[0], properties[1], properties[2], properties[3], properties[4],
                                  properties[5], properties[6], properties[7], properties[8])
                productList.append(product)
            getProducts.close()
            return productList
    else:
        productList.clear()

def GetValuesForTable(productList):
    for product in productList:
        properties = product.getProperties()
        table_product = TableProduct(properties[0],properties[1],properties[2],properties[3],properties[4],properties[5])
        productTable.insert("", END, values=table_product.getProperties())

def AddProductManager():
    global lastId
    try:
        if(nameEntry.get() == "" or productTypeEntry.get()  == "" or productPriceEntry.get() == "" or productBrandCombobox.get() == "" or productPriceRangeCombobox.get() == "" or productOSCombobox.get() == ""):
            messagebox.showwarning("DEĞERLERİ DÜZGÜN GİRİNİZ", "Lütfen, Değerleri Düzgün Giriniz")
        else:
            newProduct = Product(lastId, fixTheString(nameEntry.get()), fixTheString(productTypeEntry.get()), fixTheString(productPriceEntry.get()), fixTheString(productReleaseDateEntry.get()), fixTheString(productBrandCombobox.get()), fixTheString(productPriceRangeCombobox.get()), fixTheString(productOSCombobox.get()), fixTheString(productAvailableCombobox.get()))
            with open("MyProduct.txt", mode='a') as ProductAdd:
                addedText = f"\n{newProduct.FixProductForMyProductFile()}"
                ProductAdd.write(addedText)
    except:
        messagebox.showerror("HATA!", "Sistemde Bir Hata Var!")
    finally:
        lastId = getLastId()
        ProductAdd.close()




# Tkinter Codes
root = Tk()
app_heigth = 660
app_width = 1200
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()
x = int((screen_width / 2) - (app_width / 2))
y = int((screen_height / 2) - (app_heigth / 2))
root.geometry(f"{app_width}x{app_heigth}+{x}+{y}")
root.state('zoomed')
root.title('Vatan Bilgisayar - Product Management System')

# Element Variables
#backgroundColor = '#04364A'
backgroundColor = '#222831'
buttonColor = '#393E46'
buttonHoverColor = '#00ADB5'

# Variables
productName = StringVar() # +
productType = StringVar() # +
productPrice = StringVar() # +
productReleaseDate = StringVar()
productBrand = StringVar() # +
productPriceRange = StringVar()
productOS = StringVar() # +
productAvailable = StringVar()



# defines
def on_enter(e):
    e.widget['background'] = buttonHoverColor

def on_leave(e):
    e.widget['background'] = buttonColor


def AddProduct():
    AddProductManager()
    GetAllProduct()

def GetAllProduct():
    #(len(productTable.get_children()))
    try:
        if len(productTable.get_children()) != 0:
            ClearAllTable()
            #time.sleep(0.2)
            GetValuesForTable(GetUserFromTextFile())
        else:
            GetValuesForTable(GetUserFromTextFile())
    except:
        GetValuesForTable(GetUserFromTextFile())

def ClearAll():
    productName.set("")
    productType.set("")
    productPrice.set("")
    productReleaseDate.set("")
    productBrand.set("")
    productPriceRange.set("")
    productOS.set("")
    productAvailable.set("")





# Entries Frame
entries_frame = Frame(root, bg=backgroundColor)
entries_frame.pack(side=LEFT, fill=Y)
title = Label(entries_frame, text='VATAN BİLGİSAYAR', font=('Courier', 22, 'bold'), bg=backgroundColor, fg='white')
title.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
# title -> sticky('we') ile ortaladık

nameLbl = Label(entries_frame, text='Name: ', bg=backgroundColor, fg='white', font=('Calibri', 18))
nameEntry = Entry(entries_frame, textvariable=productName, font=('Calibri', 18))
nameLbl.grid(row=1, column=0, sticky=W, padx=10, pady=10)
nameEntry.grid(row=1, column=1, sticky=W, padx=10, pady=10)

productReleaseDateLbl = Label(entries_frame, text='Release Date: ', bg=backgroundColor, fg='white', font=('Calibri', 18))
productReleaseDateEntry = Entry(entries_frame, textvariable=productReleaseDate, font=('Calibri', 18))
productReleaseDateLbl.grid(row=2, column=0, sticky=W, padx=10, pady=10)
productReleaseDateEntry.grid(row=2, column=1, sticky=W, padx=10, pady=10)

productPriceLbl = Label(entries_frame, text='Price: ', bg=backgroundColor, fg='white', font=('Calibri', 18))
productPriceEntry = Entry(entries_frame, textvariable=productPrice, font=('Calibri', 18))
productPriceLbl.grid(row=3, column=0, sticky=W, padx=10, pady=10)
productPriceEntry.grid(row=3, column=1, sticky=W, padx=10, pady=10)


productOSLbl = Label(entries_frame, text='OS: ', bg=backgroundColor, fg='white', font=('Calibri', 18))
productOSCombobox = ttk.Combobox(entries_frame, textvariable=productOS, font=('Calibri', 18), state='readonly', width=18)
productOSCombobox['values'] = ('Freedos', 'Linux', 'Windows', 'macOS')
productOSLbl.grid(row=4, column=0, sticky=W, padx=10, pady=10)
productOSCombobox.grid(row=4, column=1, sticky=W, padx=10, pady=10)

productTypeLbl = Label(entries_frame, text='Type: ', bg=backgroundColor, fg='white', font=('Calibri', 18))
productTypeEntry = ttk.Combobox(entries_frame, textvariable=productType, font=('Calibri', 18), state='readonly', width=18)
productTypeEntry['values'] = ('Dekstop', 'Laptop', 'Gaming Laptop', 'Premium Laptop')
productTypeLbl.grid(row=5, column=0, sticky=W, padx=10, pady=10)
productTypeEntry.grid(row=5, column=1, sticky=W, padx=10, pady=10)

productPriceRangeLbl = Label(entries_frame, text='Price Range: ', bg=backgroundColor, fg='white', font=('Calibri', 18))
productPriceRangeCombobox = ttk.Combobox(entries_frame, font=('Calibri', 18), state='readonly', textvariable=productPriceRange, width=18)
productPriceRangeCombobox['values'] = ("5000 - 9999 TL", "10000 - 14999 TL", "15000 - 19999 TL", "20000 TL - Üzeri")
productPriceRangeLbl.grid(row=6, column=0, sticky=W, padx=10, pady=10)
productPriceRangeCombobox.grid(row=6, column=1, sticky=W, padx=10, pady=10)

productBrandLbl = Label(entries_frame, text='Brand: ', bg=backgroundColor, fg='white', font=('Calibri', 18))
productBrandCombobox = ttk.Combobox(entries_frame, font=('Calibri', 18), state='readonly', textvariable=productBrand, width=18)
productBrandCombobox['values'] = ("ACER", "APPLE", "ASUS", "CASPER", "DELL", "GIGABAYT", "HOMETECH", "HP", "HUAWEI", "LENOVO", "MSI")
productBrandLbl.grid(row=7, column=0, sticky=W, padx=10, pady=10)
productBrandCombobox.grid(row=7, column=1, sticky=W, padx=10, pady=10)

productAvailableLbl = Label(entries_frame, text='Available: ', bg=backgroundColor, fg='white', font=('Calibri', 18))
productAvailableCombobox = ttk.Combobox(entries_frame, font=('Calibri', 18), state='readonly', textvariable=productAvailable, width=18)
productAvailableCombobox['values'] = ('Stokta Var', "Stokta Yok")
productAvailableLbl.grid(row=8, column=0, sticky=W, padx=10, pady=10)
productAvailableCombobox.grid(row=8, column=1, sticky=W, padx=10, pady=10)

# button frame
btn_frame = Frame(entries_frame, bg=backgroundColor)
btn_frame.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky=W)

addButton = Button(btn_frame, command=AddProduct, width=30, text='Add Product', bg=buttonColor, bd=0, font=('Calibri', 18, 'bold'), fg='white')
addButton.grid(row=0, column=0, columnspan=2, sticky=W, padx=7, pady=10)

getAllButton = Button(btn_frame, command=GetAllProduct, width=30, text='Get All Product', bg=buttonColor, bd=0, font=('Calibri', 18, 'bold'), fg='white')
getAllButton.grid(row=1, column=0, columnspan=2, sticky=W, padx=7, pady=10)

clearAllButton = Button(btn_frame, command=ClearAll, width=30, text='Clear All Entries', bg=buttonColor, bd=0, font=('Calibri', 18, 'bold'), fg='white')
clearAllButton.grid(row=2, column=0, columnspan=2, sticky=W, padx=7, pady=10)

createdBy = Label(btn_frame, font=('Calibri', 12, 'bold'), text='Created By', bg=backgroundColor, fg='white')
createdBy.grid(row=3, column=0, columnspan=2, sticky='we')
createdByMe = Label(btn_frame, font=('Calibri', 20, 'bold'), text='Ahmet Aydoğan', bg=backgroundColor, fg='white')
createdByMe.grid(row=4, column=0, columnspan=2, sticky='we')

addButton.bind("<Enter>", on_enter)
addButton.bind("<Leave>", on_leave)
getAllButton.bind("<Enter>", on_enter)
getAllButton.bind("<Leave>", on_leave)
clearAllButton.bind("<Enter>", on_enter)
clearAllButton.bind("<Leave>", on_leave)


# Table Frame
table = Frame(root)
table.place(x=440, y=0, width=screen_width-440, height=screen_height)

# İngilizcem buradaki dökümantasyonları okumaya ve anlamaya yetmedi youtube üzerinden de çözemedim açıkcası
# Burayı youtube'dan çaldım
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18), rowheight=50)
style.configure('mystyle.Treeview.Heading', font=('Calibri', 18, 'bold'))

productTable = ttk.Treeview(table, style='mystyle.Treeview', columns=('ID', 'NAME', 'BRAND', 'PRICE', 'TYPE', 'OS'), show='headings')
productTable.heading('ID', text='ID')
productTable.column('ID', width=20)
productTable.heading('NAME', text='Name')
productTable.heading('BRAND', text='Brand')
productTable.heading('PRICE', text='Price')
productTable.heading('TYPE', text='Type')
productTable.heading('OS', text='OS')
productTable.pack(fill=X)

def getProductInfo(e):
    product = productTable.focus()
    #product = productTable.selection()[0]
    productId = int(productTable.item(product).get('values')[0])

    myProductContent: str
    with open('MyProduct.txt', mode='r') as getProducts:
        myProductContent = getProducts.read()
        for line in myProductContent.split('\n'):
            properties = list()
            for property in line.split(','):
                properties.append(property)
            for prop in properties[0]:
                if int(prop[0]) == productId:
                    productName.set(properties[1])
                    productReleaseDate.set(properties[3])
                    productPrice.set(properties[4])
                    productOS.set(properties[7])
                    productType.set(properties[2])
                    productPriceRange.set(properties[6])
                    productBrand.set(properties[5])
                    productAvailable.set(properties[8])
        getProducts.close()
productTable.bind("<Double-1>", getProductInfo)

if __name__ == '__main__':
    GetAllProduct()

root.mainloop()