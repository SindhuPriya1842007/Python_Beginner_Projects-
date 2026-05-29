class Coffee:
    # initializing coffee names and prices
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
class Order:
    # initializing order with empty list
    def __init__(self):
        self.items = []            #In items list , we store both name and price , how ? Because we are passing the complete object 
    def add_items(self,coffee):   # Here we are passing Coffee Object 
        self.items.append(coffee)    #append(coffee) which means [name,price],[name,price],... and if we store only strings we 
                                     #dont have a method like ".name"
        print(f"Added {coffee.name} to ur order ")
    # calculate total price
    def total(self):
        return sum(item.price for item in self.items)
    # Show Order Summary
    def show_order(self):
        if not self.items:
            print("No items in order")
            return 
        print("\nYour Order: ")
        for i,item in enumerate(self.items,1):
            print(f"{i}.{item.name} - ${item.price}")
        print(f"Total: ${self.total()}\n")
    #Handle checkout process
    def checkout(self):
        if not self.items:
            print("Your cart is Empty")
            return 
        self.show_order()
        confirm = input("Proceed to checkout ? (yes/no) ").strip().lower()
        if confirm == 'yes' :
            print("Order confirmed ! Thank You")
            self.items.clear()
        else :
            print("Order cancelled")
    #Display menu and handle user input
def main():
    menu = [Coffee('Expresso',2.5) , Coffee('Latte',3.5),Coffee('Cappucino',3.0),
           Coffee('Americano',2.0)]
    order = Order()
    #User interaction
    while True :
        print("\n<--- COFFEE MENU --->" )
        for i,coffee in enumerate(menu,1):
            print(f"{i}.{coffee.name} - ${coffee.price}")
        print("5. View Order")
        print("6. Checkout")
        print("7. Exit")
        choice = input("Choose an option: ")
        if choice in ['1','2','3','4']:
            order.add_items(menu[int(choice)-1])
        elif choice == '5':
            order.show_order()
        elif choice =='6':
                order.checkout()
        elif choice == '7' :
            print("Thanks For Visiting. GoodBye!")
            break
        else:
            print("Invalid choice. Try again")
if __name__ =="__main__":
    main()
        
