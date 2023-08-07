class MergeSort:

    def __init__(self, arr):

        self.arr = arr

        self.i = 0
        self.j = 0
        self.k = 0

        self.sorting()
        self.printList()

    def sorting(self):
        mid = len(self.arr) // 2
        lift = self.arr[:mid]
        right = self.arr[mid:]

        if len(self.arr > 1):
            while self.i < len(lift) and self.j < len(right):
                if lift[self.i] < right[self.j]:
                    self.arr[self.k] = lift[self.i]
                    self.i += 1
                else:
                    self.arr[self.k] = right[self.j]
                    self.j += 1
                self.k += 1

            while self.i < len(lift):
                self.arr[self.k] = lift[self.i]
                self.i += 1
                self.k += 1

            while self.j < len(right):
                self.arr[self.k] = right[self.j]
                self.j += 1
                self.k += 1

            self.sorting()

    def printList(self, arr):
        for i in range(len(self.arr)):
            print(self.arr[i], end=" ")


def main():
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    print(arr)
    print("Sorted array is: ", end="\n")
    run = MergeSort(arr)
    run.printList()


if __name__ == '__main__':
    main()
