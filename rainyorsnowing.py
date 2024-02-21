def getData(weather):
    global data
    val = True
    while val:
        data = input(f"Is it {weather}? ")
        val = checking(data)
    return data


def checking(data):
    if data == "yes" or data == "no":
        return False
    else:
        return True


rain = getData("raining")
snow = getData("snowing")

# Check if either rain or snow is True
if rain == "yes" or snow == "yes":
    print("True")
else:
    print("False")
