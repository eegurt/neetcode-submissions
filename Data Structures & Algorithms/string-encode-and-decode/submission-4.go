type Solution struct{}

func (s *Solution) Encode(strs []string) string {
    result := ""
    for _, s := range strs {
        result += strconv.Itoa(len(s)) + "#" + s
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
        start := j + 1
        tokenLen, _ := strconv.Atoi(encoded[i:j])
        strs = append(strs, encoded[start:start+tokenLen])
        i = start + tokenLen
    }
    return strs
}
