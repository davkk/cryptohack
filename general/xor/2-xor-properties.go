package main

import (
	"encoding/hex"
	"fmt"
)

func decodeHex(input string) []byte {
	data, _ := hex.DecodeString(input)
	return data
}

func xor(a, b []byte) []byte {
	result := make([]byte, len(a))
	for idx := range a {
		result[idx] = a[idx] ^ b[idx]
	}
	return result
}

func main() {
	key1 := decodeHex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
	key23 := decodeHex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
	final := decodeHex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

	fmt.Printf("%s\n", xor(final, xor(key23, key1)))
}
