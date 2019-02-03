def main():
    l = list()
    l.append(2)
    l.append(3)

    # print(l.index(3))

    while l:
        print(l.pop())

    if not l:
        print("Finally empty")

main()