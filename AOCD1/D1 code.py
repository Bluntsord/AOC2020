
with open('D1 dataset.py', 'r') as f:
    print(f.name)

    D1_content = f.readlines()
    length  =  len(D1_content)
    ans = list()
    # print(D1_content)
    for i in range(length):
        current = int(D1_content[i].replace("\n", ""))
        # print(D1_content[i])
        ans.append(current)
    # ans.sort()

    print(ans)
    print('PART 1')

    for i in ans:
        current = 2020 - i
        if current in ans:
            print(current,i, current * i)
            break



    print("PART 2")
    for i in ans:
        for j in ans:
            current = 2020 - i - j
            if current in ans:
                print(current, i , j, current* i * j)
                break


# def sumtovalue(value):
#     return



# f.close()


