package main

import (
	"encoding/hex"
	"fmt"
	"os"
)

func main() {
	data, _ := hex.DecodeString(os.Args[1])
	flag := []byte("crypto{")

	keyBytes := make([]byte, len(data))
	for idx, b := range flag {
		keyBytes[idx] = b ^ data[idx]
	}
	keyBytes[len(data)-1] = '}' ^ data[len(data)-1]

	key := ""
	idx := 0
	for len(key) < len(data) {
		b := keyBytes[idx]
		if b != 0 {
			key += string(b)
		}
		idx = (idx + 1) % len(keyBytes)
	}

	fmt.Println(key)
	for idx, b := range data {
		fmt.Printf("%c", key[idx]^byte(b))
	}
}
