#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import locale
locale.setlocale(locale.LC_ALL, "")

# ANSI escape sequence for bold text
BOLD = "\033[1m"
# ANSI escape sequence to reset text formatting
RESET = "\033[0m"

# Column indices in the CSV file for specific data fields
REGION_INDEX = 12       # Index of the region column
SEGMENT_INDEX = 7       # Index of the segment column
CATEGORY_INDEX = 15     # Index of the category column
SALES_INDEX = 18        # Index of the sales column
PROFIT_INDEX = 21       # Index of the profit column


class Order:
    def __init__(self, region, segment, category, sales, profit):
        self.region = region
        self.segment = segment
        self.category = category
        self.sales = sales
        self.profit = profit

def OpenFile():
    NAMEOFFILE = 'StoreOrders-Proj2.csv'
    fileIn = open(NAMEOFFILE)
    fileIn.readline()
    return fileIn

def ReadLine(line):
    line = line.strip()
    cells = line.split(",")
    curRegion = cells[REGION_INDEX]
    curSegment = cells[SEGMENT_INDEX]
    curCategory = cells[CATEGORY_INDEX]
    curSales = float(cells[SALES_INDEX])
    curProfit = float(cells[PROFIT_INDEX])
    curOrder = Order(curRegion, curSegment, curCategory, curSales, curProfit)
    return curOrder

def BuildLists(dataOrders):
    regionList = []
    segmentList = []
    categoryList = []
    for curOrder in dataOrders:
        if curOrder.region not in regionList:
            regionList.append(curOrder.region)
        if curOrder.segment not in segmentList:
            segmentList.append(curOrder.segment)
        if curOrder.category not in categoryList:
            categoryList.append(curOrder.category)
    return regionList, segmentList, categoryList

def CalcTotalRegionSales(regList, orderList):
    regSales = []
    for region in regList:
        regSales.append(0)
        curIndex = len(regSales) - 1
        for order in orderList:
            if order.region == region:
                regSales[curIndex] += order.sales
    return regSales

def CalcTotalRegionProfit(regList, orderList):
    regProfit = []
    for region in regList:
        regProfit.append(0)
        curIndex = len(regProfit) - 1
        for order in orderList:
            if order.region == region:
                regProfit[curIndex] += order.profit
    return regProfit

def CalcTotalCategorySales(catList, orderList):
    catSales = []
    for category in catList:
        catSales.append(0)
        curIndex = len(catSales) - 1
        for order in orderList:
            if order.category == category:
                catSales[curIndex] += order.sales
    return catSales

def CalcTotalCategoryProfit(catList, orderList):
    catProfit = []
    for category in catList:
        catProfit.append(0)
        curIndex = len(catProfit) - 1
        for order in orderList:
            if order.category == category:
                catProfit[curIndex] += order.profit
    return catProfit

def CalcTotalSegmentSales(segList, orderList):
    segSales = []
    for segment in segList:
        segSales.append(0)
        curIndex = len(segSales) - 1
        for order in orderList:
            if order.segment == segment:
                segSales[curIndex] += order.sales
    return segSales

def CalcTotalSegmentProfit(segList, orderList):
    segProfit = []
    for segment in segList:
        segProfit.append(0)
        curIndex = len(segProfit) - 1
        for order in orderList:
            if order.segment == segment:
                segProfit[curIndex] += order.profit
    return segProfit

orderList = []
fileIn = OpenFile()

for line in fileIn:
    orderList.append(ReadLine(line))

regLst, segLst, catLst = BuildLists(orderList)
regSalesList = CalcTotalRegionSales(regLst, orderList)
regProfitList = CalcTotalRegionProfit(regLst, orderList)
segSalesList = CalcTotalSegmentSales(segLst, orderList)
segProfitList = CalcTotalSegmentProfit(segLst, orderList)
catSalesList = CalcTotalCategorySales(catLst, orderList)
catProfitList = CalcTotalCategoryProfit(catLst, orderList)

def MenuChoice(userChoice=None):
    while userChoice is not None:
        print(f"\n{BOLD}****************** MENU ******************{RESET}")
        print("Please, enter a number 1-7 to select an option from the list below:\n")
        print(f"{BOLD}1. Region Sales{RESET}")
        print(f"{BOLD}2. Region Profit{RESET}")
        print(f"{BOLD}3. Segment Sales{RESET}")
        print(f"{BOLD}4. Segment Category{RESET}")
        print(f"{BOLD}5. Category Sales{RESET}")
        print(f"{BOLD}6. Category Category{RESET}")
        print(f"{BOLD}7. Exit{RESET}\n")
        
        choice = input("Enter your choice from our menu 1-7: ")


        if choice == '1':
            print('\nRegion Sales')
            for index in range(len(regLst)):
                print(f'{regLst[index]:<20} {locale.currency(regSalesList[index], grouping=True):>20}')
        elif choice == '2':
            print('\nRegion Profit')
            for index in range(len(regLst)):
                print(f'{regLst[index]:<20} {locale.currency(regProfitList[index], grouping=True):>20}')
        elif choice == '3':
            print('\nSegment Sales')
            for index in range(len(segLst)):
                print(f'{segLst[index]:<20} {locale.currency(segSalesList[index], grouping=True):>20}')
        elif choice == '4':
            print('\nSegment Profit')
            for index in range(len(segLst)):
                print(f'{segLst[index]:<20} {locale.currency(segProfitList[index], grouping=True):>20}')
        elif choice == '5':
            print('\nCategory Sales')
            for index in range(len(catLst)):
                print(f'{catLst[index]:<20} {locale.currency(catSalesList[index], grouping=True):>20}')
        elif choice == '6':
            print('\nCategory Profit')
            for index in range(len(catLst)):
                print(f'{catLst[index]:<20} {locale.currency(catProfitList[index], grouping=True):>20}')
        elif choice == '7':
            return print('\nApplication closed')
        else:
            print('\nPlease, enter a valid menu choice 1-7\n')

MenuChoice(0)


# In[ ]:




