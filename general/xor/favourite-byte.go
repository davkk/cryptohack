package main

import (
	"encoding/hex"
	"fmt"
	"os"
	"strings"
)

func main() {
	data, _ := hex.DecodeString(os.Args[1])

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
