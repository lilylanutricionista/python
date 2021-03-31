print("Hello Python")
message = "Hello Python"
print (message)


def format_position(lat, long):
    formatPosition = "lat:{} long{}".format(lat, long)
    return formatPosition


print(format_position(-52.33, 120.00))
