Cost_price=int(input("Enter the  value of Cost_price: "))
Selling_price=int(input("Enter the  value of Selling_price: "))


# def  calculate_profit(Cost_price,Selling_price):
#     Profit = (Selling_price - Cost_price) / Cost_price *100
#     return Profit
# print ("The profit is : ",calculate_profit(Cost_price,Selling_price),"%")





if Selling_price> Cost_price:
    profit=Selling_price-Cost_price
    print("It's a profit of : ",profit)
else:
    loss=Cost_price-Selling_price
    print("It's a Loss of : ",loss)    