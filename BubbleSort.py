class BubbleSort:
    def __init__(self, array) -> None:
        self.array = array
    
    def sort(self) -> list:
        
        for j in range(len(self.array)):
            for i in range(len(self.array)-j-1):
                if self.array[i] > self.array[i+1]:
                    self.array[i], self.array[i+1] = self.array[i+1], self.array[i]

        return self.array

a = [4,6,2,5,7,32,65,4,2,2,3,4,5,3]
bubble =BubbleSort(a)
print(bubble.sort())