from PIL import Image, ImageDraw, ImageFont

if __name__ == '__main__':
    w, h = 220, 190
    img = Image.new('RGB', (w, h), color = (255, 255, 255))
    fnt = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 15)
    img1 = ImageDraw.Draw(img)

    fill2 = (19, 119, 169) # colour used for data

    l1=['Sluis','F','1990-01-22'] # List data to use for certificate

#vertical line
    shape = [(0, 0), (0, h)]
    img1.line(shape, fill="red", width=0)

    # vertical line
    shape = [(w-1, 0), (w, h)]
    img1.line(shape, fill="red", width=0)

    shape = [(0, 0), (w , 0 )]
    img1.line(shape, fill ="red", width = 0)
    img1.text((0, 0), l1[0], fill=fill2, font=fnt)


    shape = [(0, 49), (w, 49)]
    img1.line(shape, fill="red", width=0)
    img1.text((50, 0), l1[1], fill=fill2, font=fnt)


    shape = [(0, 100), (w, 100)]
    img1.line(shape, fill="red", width=0)
    img1.text((100, 0), l1[2], fill=fill2, font=fnt)


    #img.show()
    #img1.text((10,10), "Hello World", font=fnt, fill=(255,255,0))
    img.save('pil_red.png')

