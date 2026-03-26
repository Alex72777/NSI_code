from PIL import Image

def addition(fond: str, ajout: str, output_file: str, coef: int, transparancy: int = 255) -> None:
    fond = Image.open(fond)
    ajout = Image.open(ajout)
    width, height = fond.size
    
    code = Image.new('RGB', (width, height))
    for i in range(width):
        for j in range(height):
            fondpix = fond.getpixel((i, j))
            ajoutpix = ajout.getpixel((i, j))
            newpix = (fondpix[0] + ajoutpix[0] // coef,
                      fondpix[1] + ajoutpix[1] // coef,
                      fondpix[2] + ajoutpix[2] // coef)
            #newpix = (fondpix[0] + ajoutpix[0], fondpix[1] + ajoutpix[1], fondpix[2] + ajoutpix[2], transparancy)
            code.putpixel((i, j), newpix)
    
    code.show(output_file)
    code.save(output_file)

def soustraction(fond: str, ajout: str, output_file: str, coef: int, transparancy: int = 255) -> None:
    fond = Image.open(fond)
    ajout = Image.open(ajout)
    width, height = fond.size
    
    fond.convert('RGB')
    ajout.convert('RGB')
    code = Image.new('RGB', (width, height))
    for i in range(width):
        for j in range(height):
            fondpix = fond.getpixel((i, j))
            ajoutpix = ajout.getpixel((i, j))
            newpix = (fondpix[0] - ajoutpix[0] // coef,
                      fondpix[1] - ajoutpix[1] // coef,
                      fondpix[2] - ajoutpix[2] // coef)
            code.putpixel((i, j), newpix)
    
    code.show(output_file)

def main() -> None:
    addition("fleur.png", "image_bat.png", "batsecret.png", 1)
    soustraction("batsecret.png", "fleur.png", "bat_sans_secret.png", 1)

if __name__ == "__main__":
    main()