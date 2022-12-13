def my_function(firstname, lastname, age):
    my_dictionary = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
    }
    return my_dictionary

write_yours = my_function(firstname="Mert", lastname="Vural", age=22)
print(write_yours)