# Cryptohack - General

1. ASCII - vim

format each number into their own line

record macro and execute on each line:

```
:s/\d\+/\=nr2char(submatch(0))/g
```

select all and `gJ`

2. Hex

```
% echo -n 63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d | xxd -r -p
```

3. Base64

```
% echo -n 72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf | xxd -r -p | base64
```


4. Bytes and Big Integers

```
% bc <<< "obase=16;11515195063862318899931685488813747395775516287289682636499965282714637259206269"
63727970746F7B336E633064316E365F346C6C5F3768335F7734795F6430776E7D
% echo -n 63727970746F7B336E633064316E365F346C6C5F3768335F7734795F6430776E7D | xxd -r -p
```

5. Encoding Challenge

Run:

```bash
go run encoding.go
```
