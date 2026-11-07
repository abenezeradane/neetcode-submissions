type DynamicArray struct {
	slice []int
	capacity int
	contains int
}

func NewDynamicArray(capacity int) *DynamicArray {
	return &DynamicArray{
		make([]int, capacity),
		capacity,
		0,
	}
}

func (da *DynamicArray) Get(i int) int {
	return da.slice[i]
}

func (da *DynamicArray) Set(i int, n int) {
	da.slice[i] = n
}

func (da *DynamicArray) Pushback(n int) {
	if da.contains == da.capacity {
		da.resize()
	}

	da.slice[da.contains] = n
	da.contains++
}

func (da *DynamicArray) Popback() int {
	da.contains--
	return da.slice[da.contains]
}

func (da *DynamicArray) resize() {
	var buffer []int = da.slice

	da.capacity *= 2
	da.slice = make([]int, da.capacity)
	copy(da.slice, buffer)
}

func (da *DynamicArray) GetSize() int {
	return da.contains
}

func (da *DynamicArray) GetCapacity() int {
	return da.capacity
}
