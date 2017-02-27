# This program is to find three numbers in the array which sum is equal to given number
def bruteforce(targetsum, numbers):
 for i in range (0, len(numbers) - 2):
    for n in range (i+1, len(numbers) - 1):
        for k in range (n+1, len(numbers)):
            if (numbers[i] + numbers[n] + numbers[k] == targetsum):
                print("Triplet is", numbers[i], numbers[n], numbers[k])


def sorted(targetsum, numbers):
    numbers.sort()
    #print(numbers)
    for i in range (0, len(numbers) - 2):
        l = i + 1
        r = len(numbers) - 1
        while l < r:
            if (numbers[i] + numbers[l] + numbers[r] == targetsum):
                print("Triplet is", numbers[i], numbers[l], numbers[r])
                l+=1
            elif (numbers[i] + numbers[l] + numbers[r] < targetsum):
                l+=1
            else:
                r-=1

def main():
    with open('numbers.dat', 'r') as f:
        imput_data = f.read()
        targetsum = int(imput_data.split('\n')[1])
        k = int(imput_data.split('\n')[0])

    numbers = [int(x) for x in imput_data.split('\n')[2:]]
    print("This run is accomplished with bruteforce algorithm")
    bruteforce(targetsum, numbers)
    print("This run is accomplished with sorted algorithm")
    sorted(targetsum, numbers)

if __name__ == "__main__":
    main()

