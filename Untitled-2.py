for i in range(5):
    for j in range(5, 10):
        print(j)
        for k in range(10, 15):
            k += 1
            print(k)
    print(i)
    break