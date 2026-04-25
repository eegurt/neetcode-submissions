type Solution struct{}

func (s *Solution) Encode(strs []string) string {
    result := ""
    for i, s := range strs {
        result += len(s) + "#" + s
    }
    return result
}

func (s *Solution) Decode(encoded string) []string {
    strs := []string{}
    i := 0
    
    for i < len(encoded) {
        j := i
        for encoded[j] != '#' {
            j++
        }
        tokenLen, _ := strconv.Atoi(encoded[i:j])
        strs = append(strs, encoded[i:j + tokenLen + 1])
        i = j + tokenLen + 1
    }
    return strs
}
