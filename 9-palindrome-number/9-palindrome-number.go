func isPalindrome(x int) bool {
    if x < 0 {
        return false
    }
    var curr int = x
    var temp int
    for curr / 10 >= 0 {
        temp = temp*10 + curr % 10
        curr /= 10
        if curr == 0 {
            break
        }
    }
    return temp == x
}