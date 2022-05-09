func reverseBits(num uint32) uint32 {
    var reverse uint32
    for i := 0; i < 32; i++ {
        reverse = reverse*2 + num%2
        num /= 2
    }
    return reverse
}