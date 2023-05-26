
import gfx
doc = gfx.open("pdf", "document.pdf")
img = gfx.ImageList()
img.setparameter("antialise", "1") # turn on antialising
page1 = doc.getPage(1)
img.startpage(page1.width-50,page1.height-50)
page1.render(img)
img.endpage()
img.save("thumbnail80x80.png")