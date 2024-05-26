class SelectionSort:
    def __init__(self, array) -> None:
        self.array = array
    
    def sort(self) -> list:

        n = len(self.array)
        for i in range(n):
            min = i
            for j in range(i+1, n):
                if(self.array[j] < self.array[min]):
                    min = j
            self.array[min], self.array[i] = self.array[i], self.array[min]
        return self.array

select = SelectionSort([10,9,8,7,6,8,3,6,2])
print(select.sort())