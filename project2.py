sales_amount=[]
book={}


while(True):
    print("1.Add book")
    print("2.view all books")
    print("3.search book")
    print("4.update book")
    print("5.record sale")
    print("6.inventory analysis")
    print("7.sales analysis")
    print("8.book title analysis")
    print("9.number analysis")
    print("10.set and tuple practice")
    print("exit")
    choice=int(input("enter choice:"))
    if choice==1:
        print("Add book")
        book_id=int(input("enter book id:"))
        book_title=input("enter book title:").capitalize()
        author_name=input("enter author name:").capitalize()
        price=float(input("enter the price of the book:"))
        available_quantity=int(input("enter available quantity:"))
        print("book title",book_title)
        print("author name",author_name)
        
        books={
                "book_id":book_id,
                "book_title":book_title,
                "author_name":author_name,
                "price":price,
                "available_quantity":available_quantity
            
        }
        book[book_id]=books
        
        print(books)
    elif choice==2:
        print("view all books")
    
        print("view all books")
        print("keys:",book.keys())
        print("value:",book.values())
        print("items:",book.items())
    elif choice==3:
        print("search book")
        book_id=int(input("enter book id:"))
        if book_id in book:
            print(book.get(book_id))
        else:
            print("books not found!")
    elif choice==4:
        print("update book")
        book_id=int(input("enter book id:"))
        book_title=input("enter updates book title:").capitalize()
        author_name=input("enter  updates author name:").capitalize()
        price=float(input("enter  updates the price of the book:"))
        available_quantity=int(input("enter  updates available quantity:"))
        
        if book_id in book:
            book[book_id].update({
                "book_title":book_title,
                "author_name":author_name,
                "price":price,
                "available_quantity":available_quantity
            })
            print(book[book_id])
        else:
            print("book not found")
    elif choice==5:
        print("record sale")
        book_id=int(input("enter book id:"))
        quantity_sold=int(input("enter number of sold quantites:"))
        if book_id in book:
            sale_amount=price*quantity_sold
            print("sale_amount",sale_amount)
            sales_amount.append(sale_amount)
            print("book_title",book_title)
            print("quantity_sold",quantity_sold)
        #if book_id<0:
          #break
    elif choice==6:
        print("inventory analysis")
        price_list=[]
        for book_id in book:
            p=book[book_id]["price"]
            price_list.append(p)
        quantity_list=[]
        for book_id in book:
            q=book[book_id]["available_quantity"]
            quantity_list.append(q)
        print(price_list)
        print(quantity_list)
        price_list.sort()
        quantity_list.sort()
        print("price in asc order:",price_list)
        print("quantity in asc order:",quantity_list)
        price_list.sort(reverse=True)
        quantity_list.sort(reverse=True)
        print("price in dsc order:",price_list)
        print("quantity in dsc order:",quantity_list)
        highest=price_list[0]
        lowest=price_list[0]
        high_quantity=quantity_list[0]
        low_quantity=quantity_list[0]
        for price in price_list :
            if price>highest:
                highest=price
        
            if price<lowest:
                lowest=price
        for quantity in quantity_list:
            if quantity>high_quantity:
                high_quantity=quantity
       
            if quantity<low_quantity:
                low_quantity=quantity
               
       
        print("highest price:",highest)
        print("lowest price:",lowest)
        print("high_quantity",high_quantity)
        print("low_quantity",low_quantity)
        #now i only use price
        print("fisrt two:",price_list[0:2])
        print("last_two:",price_list[-2:])
        print("reverse:",price_list[::-1])
    elif choice==7:
        print("sales analysis")
        
        highest=sales_amount[0]
        lowest=sales_amount[0]
        for sale_amount in sales_amount:
            if sale_amount>highest:
                highest=sale_amount
            if sale_amount<lowest:
                lowest=sale_amount
        print("sales amount",sales_amount)
        print("highest sale amount:",highest)
        print("lowest sale amount:",lowest)
        if len(sales_amount)==0:
            print("no sales")
    elif choice==8:
        print("book title analysis")
        sel_tit=input("enter selected title:")
        if sel_tit in book:
            book[sel_tit]["book_title"]
        print("length of selescted title is:",len(sel_tit))
        print("first  ch:",sel_tit[0:1])
        print("last ch:",sel_tit[-1:])
        print("first 3 ch:",sel_tit[0:3])
        print("last 3 ch:",sel_tit[-3:])
        print("count a:",sel_tit.count("a"))
        print("find the position of a:",sel_tit.find("a"))
        sel_tit=sel_tit.replace(" ","-")

        print("replace:",sel_tit)
        sel_tit=sel_tit.capitalize()
        print("capitalize:",sel_tit)

    elif choice ==9:
        print("number analysis")
        
        num=int(input("enter a number:"))
        def even_odd(num):
            if num%2==0:
                print("number is even:",num)
            else:
                print("number is odd:",num)
                return num
        even_odd(num)
        def palindrome(num):
            original=str(num)
            reverse=original[::-1]
            if original==reverse:
                print("number is palindromic:",num)
            else:
                print("number is not palindromic")
                return palindrome
        palindrome(num)
        def factorial(num):
            fact=1
            if num==0:
                return 1
            for i in range(1,num+1):
                fact=i*fact
            print("factorial is:",fact)
        factorial(num)
        def prime_chk(num):
            if num<=1:
                print("not prime")
            for i in range(2,num):
                if num%i==0:
                    print("not prime")
                else:
                    print("prime")
                
            
        prime_chk(num)



    elif choice==10:
        print("set and tuple practice")
        set_1={"poetry_books","novels","history","math_book"}
        set_2={"math_book","urdu_book","eng_book","novels"}
        set_2.add("physics book")
        print("after addition:",set_2)
        set_1.remove("history")
        print("after remove:",set_1)
        set_1.pop()
        print("after pop:",set_1)
        combined=set_1.union(set_2)
        print("union:",combined)
        common=set_1.intersection(set_2)
        print("intersection:",common)
        price_list=tuple(price_list)
        print(price_list)
        price_list.index(44)
        print("present at index:",price_list)
    elif choice==11:
        print("exit")
       



















     
