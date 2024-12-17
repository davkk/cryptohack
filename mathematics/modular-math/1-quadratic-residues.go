package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	p, _ := strconv.Atoi(os.Args[1])
	x, _ := strconv.Atoi(os.Args[2])

	// a^2 === x mod p
	for a := 1; a < p-1; a++ {
		if a*a%p == x {
			fmt.Printf("a = %d\n", a)
			return
		}
	}

	fmt.Println("nothing found")
}
