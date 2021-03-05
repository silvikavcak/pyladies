stastny = input("Si stastny?")
bohaty = input("Si bohaty?")

if stastny == "ano":
    if bohaty == "ano":
        print("gratulire")
    else:
        print("Ta setri vecej, ne...")
else:
    if bohaty == "ano":
        print("pozri si dve bodky")
    else:
        print("No nic, daj si horalku.")