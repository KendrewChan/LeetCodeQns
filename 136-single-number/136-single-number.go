import (
    "fmt"
)

func singleNumber(nums []int) int {
    var curr int = 0
    for i := 0; i < len(nums); i++ {
        curr = curr ^ nums[i]   
    }
    return curr
}