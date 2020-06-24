def make_sandwich(*items):
    """print the list of toppings"""
    print(f"\n item on sandwich = {items}")

print("\n____________customer order__________")
make_sandwich("bread","chocolate")
make_sandwich("onion","tomato","cucumber")
make_sandwich("paneer","cheese","tomato","onion")
name = ["chocolate","veg","Paneer"]
print("\n__________order completed_____________")
for each_sandwich in name:
     print(f"\t \n {each_sandwich} sandwich")
