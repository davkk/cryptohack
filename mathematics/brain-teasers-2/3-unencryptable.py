from Crypto.Util.number import inverse, long_to_bytes

N = int(
    "7fe8cafec59886e9318830f33747cafd200588406e7c42741859e15994ab62410438991ab5d9fc94f386219e3c27d6ffc73754f791e7b2c565611f8fe5054dd132b8c4f3eadcf1180cd8f2a3cc756b06996f2d5b67c390adcba9d444697b13d12b2badfc3c7d5459df16a047ca25f4d18570cd6fa727aed46394576cfdb56b41",
    16,
)

# https://factordb.com/index.php?query=89820998365358013473897522178239129504456795742012047145284663770709932773990122507570315308220128739656230032209252739482850153821841585443253284474483254217510876146854423759901130591536438014306597399390867386257374956301247066160070998068007088716177575177441106230294270738703222381930945708365089958721
p = 8239835397208516111720362847949425401045672365829937602117480449316694558226622200110057535873802132963548914201468383545676262090246827792522994758916609
q = 10900824353334471830007307529937357926160386461967884446160315218630687793341471079170750548554707926611542019859296605188535413447791710067186432371970369

e = int("10001", 16)
c = int(
    "5233da71cc1dc1c5f21039f51eb51c80657e1af217d563aa25a8104a4e84a42379040ecdfdd5afa191156ccb40b6f188f4ad96c58922428c4c0bc17fd5384456853e139afde40c3f95988879629297f48d0efa6b335716a4c24bfee36f714d34a4e810a9689e93a0af8502528844ae578100b0188a2790518c695c095c9d677b",
    16,
)

phi = (p - 1) * (q - 1)
d = inverse(e, phi)

print(long_to_bytes(pow(c, d, N)).decode())
