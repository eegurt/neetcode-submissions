type Solution struct{}

func (s *Solution) Encode(strs []string) string {
    result := ""
    
    for i, s := range strs {
        if i == 0 {
            result += s
            continue
        }
        result += "✌" + s
    }
    return result
}

func (s *Solution) Decode(encoded string) []string {
    if len(encoded) == 0 {
        return []string{""}
    }

    strs := []string{}
    start := 0
    for i, r := range encoded {
        if r == '✌' {
            strs = append(strs, encoded[start:i])
            start = i + 3
        }
    }
    strs = append(strs, encoded[start:])
    return strs
}
