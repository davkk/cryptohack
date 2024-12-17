package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) != 3 {
		os.Exit(1)
	}

	a, _ := strconv.ParseInt(os.Args[1], 10, 64)
	b, _ := strconv.ParseInt(os.Args[2], 10, 64)

	for b != 0 {
		tmp := b
		b = a % b
		a = tmp
	}

	fmt.Println(a)
}
