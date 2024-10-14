package main

import (
	"fmt"
)

func main() {
	str := "label"
	fmt.Print("crypto{")
	for _, ch := range str {
		fmt.Printf("%c", ch^13)
	}
	fmt.Print("}\n")
}
