def run():
    my_list = [1, "Hello", True, 5, 6]
    my_dict = {"firstname": "Jose", "lastname": "Lobato"}

    super_list = [
        {"firstname": "Jose", "lastname": "Lobato"},
        {"firstname": "Miguel", "lastname": "Fajardo"},
        {"firstname": "Carlos", "lastname": "Hernandez"},
        {"firstname": "Roberto", "lastname": "Enriquez"},
        {"firstname": "Luis", "lastname": "Fernandez"}
    ]

    super_dict = {
        "natural_nums" : [1,2,3,4,5],
        "integer_nums" : [-1,-2,1,2],
        "floating_nums" : [1.1,4.5,6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

if __name__ == '__main__':
    run()