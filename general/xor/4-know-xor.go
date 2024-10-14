package main

import (
	"encoding/hex"
	"fmt"
	"strings"
)

func main() {
	data, _ := hex.DecodeString("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
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
	fullKey := strings.Repeat(key, len(data)/len(key))

	for idx, b := range data {
		fmt.Printf("%c", fullKey[idx]^byte(b))
	}
}
