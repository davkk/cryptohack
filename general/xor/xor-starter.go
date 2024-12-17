package main

import (
	"fmt"
)

func main() {
	fmt.Print("crypto{")
	for _, ch := range "label" {
		fmt.Printf("%c", ch^13)
	}
	fmt.Print("}\n")
}
