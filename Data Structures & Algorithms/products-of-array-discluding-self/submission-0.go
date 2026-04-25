func productExceptSelf(nums []int) []int {
    numsLen := len(nums)

    result := make([]int, numsLen)
    prefix := make([]int, numsLen)
    suffix := make([]int, numsLen)
    
    prefix[0] = 1
    for i := 1; i < len(nums); i++ {
        prefix[i] = nums[i-1] * prefix[i-1]
    }

    suffix[numsLen-1] = 1
    for i := numsLen-2; i >= 0; i-- {
        suffix[i] = nums[i+1] * suffix[i+1]
    }

    for i := range nums {
        result[i] = prefix[i] * suffix[i]
    }

    // 1 1 2 8
    // 48 24 6 1

    return result
}
