package main

import (
	"image"
	"image/color"
	"image/png"
	"os"
)

func readImage(filename string) image.Image {
	file, _ := os.Open(filename)
	defer file.Close()

	img, _ := png.Decode(file)
	return img
}

func main() {
	lemur := readImage("./lemur.png")
	flag := readImage("./flag.png")

	key := image.NewRGBA(lemur.Bounds())

	for y := 0; y < lemur.Bounds().Dx(); y++ {
		for x := 0; x < lemur.Bounds().Dx(); x++ {
			r1, g1, b1, _ := lemur.At(x, y).RGBA()
			r2, g2, b2, _ := flag.At(x, y).RGBA()

			key.Set(x, y, color.RGBA{
				R: byte(r1 ^ r2),
				G: byte(g1 ^ g2),
				B: byte(b1 ^ b2),
				A: byte(255),
			})
		}
	}

	outfile, _ := os.Create("key.png")
	defer outfile.Close()

	png.Encode(outfile, key)
}
