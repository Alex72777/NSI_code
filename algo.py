def dec_to_bin(dec: int) -> str:
    binaire = ''
    while dec // 2 > 0:
        if dec / 2 % 2:
            binaire += "0"
        else:
            binaire += "1"
        dec /= 2

    return binaire

print(dec_to_bin(13))
