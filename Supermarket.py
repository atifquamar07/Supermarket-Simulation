def show_menu():

    print('========================================================')
    print('                      MY BAZAAR                         ')
    print('========================================================')
    print('Hello! Welcome to my grocery store! \nFollowing are the products available in the shop:')
    print('                                                        ')
    print('--------------------------------------------------------')
    print('  CODE   |  DESCRIPTION  |  CATEGORY    |  COST (Rs)    ')
    print('--------------------------------------------------------')
    print('   0     |   Tshirt      |  Apparels    |    500        ')
    print('   1     |   Trousers    |  Apparels    |    600        ')
    print('   2     |   Scarf       |  Apparels    |    200        ')
    print('   3     |   Smartphone  |  Electronics |    20,000     ')
    print('   4     |   iPad        |  Electronics |    30,000     ')
    print('   5     |   Laptop      |  Electronics |    50,000     ')
    print('   6     |   Eggs        |  Eatables    |    5          ')
    print('   7     |   Chocolate   |  Eatables    |    10         ')
    print('   8     |   Juice       |  Eatables    |    100        ')
    print('   9     |   Milk        |  Eatables    |    45         ')

quantities=[0,0,0,0,0,0,0,0,0,0]

def get_regular_input():

    order=input("Enter the item codes (space-separated): ")
    ordlist=map(int,order.split())
    orderlist=list(ordlist)
    a=orderlist.count(0)
    b=orderlist.count(1)
    c=orderlist.count(2)
    d=orderlist.count(3)
    e=orderlist.count(4)
    f=orderlist.count(5)
    g=orderlist.count(6)
    h=orderlist.count(7)
    i=orderlist.count(8)
    j=orderlist.count(9)
    for z in orderlist:
        if (z<0 or z>9):
            print("Please enter valid code number ")
    quantities=[]
    quantities.append(a)
    quantities.append(b)
    quantities.append(c)
    quantities.append(d)
    quantities.append(e)
    quantities.append(f)
    quantities.append(g)
    quantities.append(h)
    quantities.append(i)
    quantities.append(j)


    return(quantities)


def get_bulk_input():
 
    b_order= input("ENTER CODE AND QUANTITY (leave blank to stop): ")
    b_ordlist=map(int,b_order.split())
    b_orderlist=list(b_ordlist)
    
    if b_order=='':
        print("Your order has beeen finalised")
        return(quantities)

    if (len(b_orderlist)!=(2)):
        print("Invalid code or quantity. Please try again.")
        return(get_bulk_input())

    else:
        
        if (b_orderlist[1]<0):
            print("Invalid Quantity, Please try again.")
            return(get_bulk_input())

        if (b_orderlist[0]==0):
            print("You added", b_orderlist[1], "Tshirts")
            quantities[0]+=(b_orderlist[1])
            return(get_bulk_input())

        if (b_orderlist[0]==1):
            print("You added", b_orderlist[1], "Trousers")
            quantities[1]+=(b_orderlist[1])
            return(get_bulk_input())

        if (b_orderlist[0]==2):
            print("You added", b_orderlist[1], "Scarfs")
            quantities[2]+=(b_orderlist[1])
            return(get_bulk_input())

        if (b_orderlist[0]==3):
            print("You added", b_orderlist[1], "Smartphones")
            quantities[3]+=(b_orderlist[1])
            return(get_bulk_input())

        if (b_orderlist[0]==4):
            print("You added", b_orderlist[1], "iPads")
            quantities[4]+=(b_orderlist[1])
            return(get_bulk_input())

        if (b_orderlist[0]==5):
            print("You added", b_orderlist[1], "Laptops")
            quantities[5]+=(b_orderlist[1])
            return(get_bulk_input())

        if (b_orderlist[0]==6):
            print("You added", b_orderlist[1], "Eggs")
            quantities[6]+=(b_orderlist[1])
            return(get_bulk_input())

        if (b_orderlist[0]==7):
            print("You added", b_orderlist[1], "Chocolates")
            quantities[7]+=(b_orderlist[1])
            return(get_bulk_input())

        if (b_orderlist[0]==8):
            print("You added", b_orderlist[1], "Juices")
            quantities[8]+=(b_orderlist[1])
            return(get_bulk_input())

        if (b_orderlist[0]==9):
            print("You added", b_orderlist[1], "Milk")
            quantities[9]+=(b_orderlist[1])
            return(get_bulk_input())

        if (b_orderlist[0]!= (0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9)):
            print("Invalid Code, Please try again.")
            return(get_bulk_input())

    return(quantities)


def print_order_details(quantities):
    

    if quantities[0]>0:
        print("Tshirt x ", quantities[0],"= Rs 500 *", quantities[0],"= Rs ", quantities[0]*500)
    if quantities[1]>0:
        print("Trousers x ", quantities[1],"= Rs 600 *", quantities[1],"= Rs ", quantities[1]*600)
    if quantities[2]>0:
        print("Scarf x ", quantities[2],"= Rs 250 *", quantities[2],"= Rs ", quantities[2]*250)
    if quantities[3]>0:
        print("Smartphone x ", quantities[3],"= Rs 20,000 *", quantities[3],"= Rs ", quantities[3]*20000)
    if quantities[4]>0:
        print("iPad x ", quantities[4],"= Rs 30,000 *", quantities[4],"= Rs ", quantities[4]*30000)
    if quantities[5]>0:
        print("Laptop x ", quantities[5],"= Rs 50,000 *", quantities[5],"= Rs ", quantities[5]*50000)
    if quantities[6]>0:
        print("Eggs x ", quantities[6],"= Rs 5 *", quantities[6],"= Rs ", quantities[6]*5)
    if quantities[7]>0:
        print("Chocolate x ", quantities[7],"= Rs 10 *", quantities[7],"= Rs ", quantities[7]*10)
    if quantities[8]>0:
        print("Juice x ", quantities[8],"= Rs 100 *", quantities[8],"= Rs ", quantities[8]*100)
    if quantities[9]>0:
        print("Milk x ", quantities[9],"= Rs 45 *", quantities[9],"= Rs ", quantities[9]*45)


def calculate_category_wise_cost(quantities):
    

    apparels_cost=(quantities[0]*500)+(quantities[1]*600)+(quantities[2]*250)
    electronics_cost=(quantities[3]*20000)+(quantities[4]*30000)+(quantities[5]*50000)
    eatables_cost=(quantities[6]*5)+(quantities[7]*10)+(quantities[8]*100)+(quantities[9]*45)

    print("Apparels = Rs ", apparels_cost)
    print("Electronics = Rs ", electronics_cost)
    print("Eatables = Rs ", eatables_cost)

    tup=(apparels_cost,electronics_cost,eatables_cost)

    return(tup)


def get_discount(cost, discount_rate):

    return (int(cost)-(cost/discount_rate))


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):

    if (apparels_cost>=2000):
        print("[APPARELS] Rs ", apparels_cost, "- Rs ", (apparels_cost)/10 , "= Rs ",get_discount(apparels_cost, 10))
        
        d_apparels_cost=get_discount(apparels_cost, 10)
        
    else:
            print("[APPARELS] Rs ", apparels_cost)

            d_apparels_cost=apparels_cost
            
            
    if (electronics_cost>=25000):
        print("[ELECTRONICS] Rs ", electronics_cost, "- Rs ", electronics_cost/10 , "= Rs ",get_discount(electronics_cost, 10))

        d_electronics_cost=get_discount(electronics_cost, 10)

    else:
            print("[ELECTRONICS] Rs ", electronics_cost)

            d_electronics_cost=electronics_cost
            
    if (eatables_cost>=500):
        print("[EATABLES] Rs ", eatables_cost, "- Rs ", eatables_cost/10 , "= Rs ",get_discount(eatables_cost, 10))

        d_eatables_cost=get_discount(eatables_cost, 10)
        
    else:
            print("[EATABLES] Rs ", eatables_cost)

            d_eatables_cost=eatables_cost
        
    
    print('                                                         ')
    
    print("TOTAL DISCOUNT = Rs ", (apparels_cost + electronics_cost + eatables_cost )-(d_apparels_cost)-(d_electronics_cost)-(d_eatables_cost))
    print("TOTAL COST = Rs ",( d_apparels_cost)+( d_electronics_cost)+(d_eatables_cost))
    return(int(d_apparels_cost),int(d_electronics_cost),int(d_eatables_cost))


def get_tax(cost, tax):

    return int(cost*tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):

    print("[APPARELS] Rs ", apparels_cost, "* 0.10 = Rs ", get_tax(apparels_cost, 0.10))
    print("[ELECTRONICS] Rs ", electronics_cost, "* 0.10 = Rs ", get_tax(electronics_cost, 0.15))
    print("[EATABLES] Rs ", eatables_cost, "* 0.10 = Rs ", get_tax(eatables_cost, 0.05))

    total_tax=(get_tax(apparels_cost, 0.10))+(get_tax(electronics_cost, 0.15))+(get_tax(eatables_cost, 0.05))
    print("TOTAL TAX = ", ((get_tax(apparels_cost, 0.10))+(get_tax(electronics_cost, 0.15))+(get_tax(eatables_cost, 0.05))))
    
    total_cost=apparels_cost+electronics_cost+eatables_cost+((get_tax(apparels_cost, 0.10)+(get_tax(electronics_cost, 0.15))+((get_tax(eatables_cost, 0.05)))))
    
    print("TOTAL COST = ", total_cost)

    return(total_cost,total_tax)
                                                                                                        


def apply_coupon_code(total_cost):

    if (total_cost>50000):
        coupon=input("Enter coupon code (else leave blank): ")
        if coupon=="CHILL50":
            d_coup=total_cost*0.5
            if d_coup>=10000:
                print("[CHILL50] min(10000, Rs ", total_cost, "* 0.50) = Rs = 10000")
                print("TOTAL COUPON DISCOUNT = Rs 10000")
                print("TOTAL COST =", total_cost-10000)
                print("Thank you for visiting!")
                return(total_cost-10000,10000)
                
            else:
                print("[CHILL50] min(10000, Rs ", total_cost, "* 0.50) = Rs = ",d_coup)
                print("TOTAL COUPON DISCOUNT = Rs ", d_coup)
                print("TOTAL COST =", total_cost-d_coup)
                print("Thank you for visiting!")
                return(total_cost-d_coup,d_coup)
                
        elif (coupon==''):
            print("No coupon code applied: ")
            print("TOTAL COUPON DISCOUNT = Rs 0")
            print("TOTAL COST =", total_cost)
            print("Thank you for visiting!")
            return(total_cost,0)

        elif coupon=="HELLE25":
            print("[HELLE25] min(5000, Rs ", total_cost, "* 0.25) = Rs = 5000")
            print("TOTAL COUPON DISCOUNT = Rs 5000")
            print("TOTAL COST =", total_cost-5000)
            print("Thank you for visiting!")
            return(total_cost-5000,5000)
            

        elif (coupon!="CHILL50"):
             print("Invalid coupon code. Try again.")
             return(apply_coupon_code(total_cost))
    
    if (total_cost>25000):
        coupon=input("Enter coupon code (else leave blank): ")
        if coupon=="HELLE25":
            d_coup=total_cost*0.25
            if d_coup>=5000:
                print("[HELLE25] min(5000, Rs ", total_cost, "* 0.25) = Rs = 5000")
                print("TOTAL COUPON DISCOUNT = Rs 5000")
                print("TOTAL COST =", total_cost-5000)
                print("Thank you for visiting!")
                return(total_cost-5000,5000)
                
            else:
                print("[HELLE25] min(5000, Rs ", total_cost, "* 0.25) = Rs = ",d_coup)
                print("TOTAL COUPON DISCOUNT = Rs ", d_coup)
                print("TOTAL COST =", total_cost-d_coup)
                print("Thank you for visiting!")
                return(total_cost-d_coup,d_coup)
                
        elif (coupon==''):
            print("No coupon code applied: ")
            print("TOTAL COUPON DISCOUNT = Rs 0")
            print("TOTAL COST =", total_cost)
            print("Thank you for visiting!")
            return(total_cost,0)
            

        elif (coupon!="HELLE25"):
             print("Invalid coupon code. Try again.")
             return(apply_coupon_code(total_cost))
    
def take_input():

    alpha=input("Would you like to buy in bulk? (y or Y / n or N): ")

    return (alpha)



def main():

    print(show_menu())


    def initialize():

        
        x=take_input()


        if ((x!='y') and (x!='N') and (x!='n') and (x!='Y')):

            print("Invalid input. Please enter the appropriate code: ")
            print(initialize())

        elif x==('n' or 'N'):

            print('--------------------------------------------------------')
            print('ENTER ITEMS YOU WISH TO BUY: ')                                              
            print('--------------------------------------------------------')

            p=get_regular_input()

            print('--------------------------------------------------------')
            print('ORDER DETAILS')
            print('--------------------------------------------------------')
                    
            print_order_details(p)

            print('---------------------------------------------------------')
            print('CATEGORY-WISE COST')
            print('---------------------------------------------------------')
                    
            a,b,c=calculate_category_wise_cost(p)

            print('--------------------------------------------------------')
            print('DISCOUNTS ')                                              
            print('--------------------------------------------------------')

                    
            e,f,g=calculate_discounted_prices(a,b,c)

            print('--------------------------------------------------------')
            print('TAX ')                                              
            print('--------------------------------------------------------')
                    
            tc,tt=calculate_tax(e,f,g)

            if tc>=25000:

                print('--------------------------------------------------------')
                print('COUPON CODE ')                                              
                print('--------------------------------------------------------')
                        
                apply_coupon_code(tc)

            else:

                print("Thank you for visiting!")
                

        elif x==('y' or 'Y'):

            print('--------------------------------------------------------')
            print('ENTER ITEMS AND QUANTITIES: ')                                              
            print('--------------------------------------------------------')

            p=get_bulk_input()

            print('--------------------------------------------------------')
            print('ORDER DETAILS')
            print('--------------------------------------------------------')
                    
            print_order_details(p)

            print('---------------------------------------------------------')
            print('CATEGORY-WISE COST')
            print('---------------------------------------------------------')
                    
            a,b,c=calculate_category_wise_cost(p)

            print('--------------------------------------------------------')
            print('DISCOUNTS ')                                              
            print('--------------------------------------------------------')

            e,f,g=calculate_discounted_prices(a,b,c)

            print('--------------------------------------------------------')
            print('TAX ')                                              
            print('--------------------------------------------------------')

            tc,tt=calculate_tax(e,f,g)

            if tc>=25000:

                print('--------------------------------------------------------')
                print('COUPON CODE ')                                              
                print('--------------------------------------------------------')
                        
                apply_coupon_code(tc)

            else:

                print("Thank you for visiting!")
                    
            


    initialize()
            
            
if __name__ == '__main__':
	main()



