from PIL import Image, ImageOps,ImageDraw
from pymsgbox import alert

error=0
try:
    inputimg=input("Please Enter Image Address: \n")

    img=Image.open(inputimg)
except FileNotFoundError :
    alert(text='The file %s does not exits' %inputimg, title='Error!', button='OK')
    error=1
if error== 0:
    try:
        outputtxt=input("Please Enter Ouput Text Name: \n")
        f = open(outputtxt+'.txt', "x")
    except FileExistsError :
        alert(text='Can not Write a file name: %s' %outputtxt, title='Error!', button='OK')
        error=1

if error == 0:     
    img=ImageOps.grayscale(img)
    img=ImageOps.equalize(img)
    

    dicew =100
    dicesize= int(img.width*1.0 / dicew)
    diceh =int(img.height*1.0/dicesize)
    dicecount=dicew*diceh

    newim=Image.new("L",(img.width,img.height),'white')
    newimg=ImageDraw.Draw(newim)

       
    for y in range(0,img.height-dicesize,dicesize):
        for x in range(0,img.width-dicesize,dicesize):
            thisSectorColor=0
            for dicex in range(0,dicesize):
                for dicey in range(0,dicesize):
                    thisColor=img.getpixel((x+dicex,y+dicey))
                    thisSectorColor += thisColor
            thisSectorColor /= (dicesize**2)
            #print(x,y,thisSectorColor)
                
            newimg.rectangle([(x,y), (x+dicesize,y+dicesize)],int(thisSectorColor))


            diceNumber=int((255-thisSectorColor)*6/255+1)
            
            #print (diceNumber,end='')
            f.write(str(diceNumber))

        #print()
        f.write("\n")
    f.close()
    alert(text='Your File Created and you will need %s Dices' %dicecount, title='Done', button='OK')
    #newim.show()
else:
    alert(text='Run the Program Again if U want', title='Exiting', button='Exit')
    
