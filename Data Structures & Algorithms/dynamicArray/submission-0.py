class DynamicArray:

    def __init__(self, capacity: int):
        this.array = []
        this.cap = capacity

    def get(self, i: int) -> int:
        return this.array[i]

    def set(self, i: int, n: int) -> None:
        this.array[i] = n

    def pushback(self, n: int) -> None:
        if len(this.array) >= this.cap:
            resize()

        this.array[-1] = n

    def popback(self) -> int:
        return this.array[-1]

    def resize(self) -> None:
        this.cap *= 2

    def getSize(self) -> int:
        return len(this.array)
    
    def getCapacity(self) -> int:
        return this.cap