def bold_text(func):
    def wrapper(name):
        print("start")
        result = '<b>{}</b>'.format(func(name))
        print(result)
        print("stop")

        return result

    return wrapper


def raw_text(name):
    return name


# super_text = bold_text(raw_text)

@bold_text
def super_text(name):
    return name


print(raw_text('This is my text'))
super_text('This is my text')