def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="saif",power="lazer")
print_kwargs(name="asif")
print_kwargs(name="saif",power="lazer",enemy="DR.hamid")
