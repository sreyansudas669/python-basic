def sample():
    name ="SREYANSU"

    def sample2():
        nonlocal name
        print(name)
        name="papu"
        print(name)

    sample2()
    print(name)

sample()