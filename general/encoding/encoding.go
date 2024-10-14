package main

import (
	"encoding/base64"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"math/big"
	"net"
	"unicode"
)

type Response struct {
	Type    string
	Encoded json.RawMessage
}

type Final struct {
	Flag string
}

type Request struct {
	Decoded string `json:"decoded"`
}

func mod(a, b rune) rune {
	return (a%b + b) % b
}

func main() {
	conn, _ := net.Dial("tcp", "socket.cryptohack.org:13377")
	defer conn.Close()

	for idx := 0; idx < 100; idx++ {
		buffer := make([]byte, 1024)
		bytesRead, _ := conn.Read(buffer)

		var resp Response
		json.Unmarshal(buffer[:bytesRead], &resp)

		var result string

		switch resp.Type {
		case "base64":
			var respEncoded string
			json.Unmarshal(resp.Encoded, &respEncoded)
			data, _ := base64.StdEncoding.DecodeString(respEncoded)
			result = string(data)
		case "hex":
			var respEncoded string
			json.Unmarshal(resp.Encoded, &respEncoded)
			data, _ := hex.DecodeString(respEncoded)
			result = string(data)
		case "rot13":
			var respEncoded string
			json.Unmarshal(resp.Encoded, &respEncoded)
			rot13 := make([]rune, len(respEncoded))
			for idx, ch := range respEncoded {
				switch {
				case !unicode.IsLetter(ch):
					rot13[idx] = ch
				case unicode.IsLower(ch):
					rot13[idx] = (ch-'a'+13)%26 + 'a'
				case unicode.IsUpper(ch):
					rot13[idx] = (ch-'A'+13)%26 + 'A'
				}
			}
			result = string(rot13)
		case "bigint":
			var respEncoded string
			json.Unmarshal(resp.Encoded, &respEncoded)
			num := new(big.Int)
			num.SetString(respEncoded[2:], 16)
			result = string(num.Bytes())
		case "utf-8":
			var parsedArray []rune
			json.Unmarshal(resp.Encoded, &parsedArray)
			result = string(parsedArray)
		}

		fmt.Println(resp.Type, result)

		req := Request{Decoded: result}
		message, _ := json.Marshal(req)
		conn.Write(message)
	}

	buffer := make([]byte, 1024)
	bytesRead, _ := conn.Read(buffer)

	var final Final
	json.Unmarshal(buffer[:bytesRead], &final)
	fmt.Println(final.Flag)
}
