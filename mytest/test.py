def selfAdd(a):
    # a += a
    a = a+a


a = [1, 2]
print(id(a))
selfAdd(a)
print(a)
print("__name__is %s" % __name__)
if __name__ == "__main__":
    print("mian")
