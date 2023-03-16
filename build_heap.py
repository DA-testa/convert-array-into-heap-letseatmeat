# python3

def heapifying(data, n, i, swaps):
    l = 2 * i + 1
    r = 2 * i + 2
    
    small = i
    if l<n and data[l] < data[small]:
        small = l
    if r<n and data[r] < data[small]:
        small = r
    
    if small != i:
        swaps.append((i,small))
        data[i], data[small] = data[small], data[i]
        heapifying(data, n, small, swaps)
    
def build_heap(data):
    swaps = []
    n = len(data)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range(n // 2 -1, -1, -1):
        heapifying(data, n, i, swaps)

    return swaps


def main():
    text = input()
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    if 'I' in text:

    # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    if 'F' in text:
        file_in = input()
        with open("tests/" + file_in, 'r') as f:
            n = int(input())
            data = list(map(int, f.readLIne().split()))
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
