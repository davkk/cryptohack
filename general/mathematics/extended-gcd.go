package main

import (
	"fmt"
	"os"
	"strconv"
)

// a*u + b*v = gcd(a, b)

func main() {
	if len(os.Args) != 3 {
		os.Exit(1)
	}

	a, _ := strconv.Atoi(os.Args[1])
	b, _ := strconv.Atoi(os.Args[2])

	x, y := 0, 1
	u, v := 1, 0

	for a != 0 {
		quot, res := b/a, b%a

		tmpU, tmpV := x-u*quot, y-v*quot
		x, y = u, v
		u, v = tmpU, tmpV

		b, a = a, res
	}

	fmt.Println(x, y)
}
