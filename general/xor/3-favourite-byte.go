package main

import (
	"encoding/hex"
	"fmt"
	"strings"
)

func main() {
	data, _ := hex.DecodeString("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

	var result string
	idx := byte(0)

	for !strings.HasPrefix(result, "crypto") {
		result = ""
		for _, ch := range data {
			result += fmt.Sprintf("%c", ch^idx)
		}
		idx++
	}

	fmt.Println(idx, result)
}
