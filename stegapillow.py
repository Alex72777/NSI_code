from PIL import Image

def addition(fond: str, ajout: str, output_file: str) -> None:
    fond = Image.open(fond)
    ajout = image.open(ajout)
    width, height = fond.size
    
    code = Image.new('RGBA', (width, height))
    for i in range(width):
        for j in range(height):
            fondpix = fond.getpixel(i, j)
            ajoutpix = ajout.getpixel(i, j)
            newpix = (fondpix[0] + ajoutpix[0], fondpix[1] + ajoutpix[1], fondpix[2] + ajoutpix[2])
            code.putpixel((i, j), newpix)

def soustraction() -> None:
    pass

def main() -> None:
    addition("fleur.png", "bat.png", "batsecret.png")

if __name__ == "__main__":
    main()