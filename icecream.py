from Restaurant import Restaurant
class Icecreamstand(Restaurant):
    """This Shows the flavours of icecream"""
    def __init__(self,restaurant_name,cusine_type):
        super().__init__(restaurant_name,cusine_type)
        self.flavour = ["butterscotch","chocolate","vanilla","strawberry"]

    def list_of_flavours(self):
        print("\nlist of flavours")
        for list in self.flavour:
            print(f"\n{list} ice-cream")
print("__"*40)
my_icecream = Icecreamstand("shanghai club","indian")
my_icecream.describe_restaurant()
my_icecream.open_restaurant()
my_icecream.list_of_flavours()


