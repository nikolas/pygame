import os
try:
    import pygame
    import pygame.image
    import Numeric as N
    import pygame.surfarray as surfarray
    from pygame.locals import *
except ImportError:
    raise ImportError, 'Error Importing Pygame/surfarray/image or Numeric'


pygame.init()
print 'Press the mouse button to advance image.'
print 'Press the "s" key to save the current image.'



def surfdemo_show(array_img, name):
    "displays a surface, waits for user to continue"
    screen = pygame.display.set_mode(array_img.shape[:2], 0, 32)
    surfarray.blit_array(screen, array_img)
    pygame.display.flip()
    pygame.display.set_caption(name)
    while 1:
        e = pygame.event.poll()
        if e.type == MOUSEBUTTONDOWN: break
        elif e.type == KEYDOWN and e.key == K_s:
            screen.save(name+'.bmp')
        elif e.type == QUIT: raise SystemExit




#allblack
allblack = N.zeros((128, 128))
surfdemo_show(allblack, 'allblack')


#striped
striped = N.zeros((128, 128, 3))
striped[:] = (255, 0, 0)
striped[:,::3] = (0, 255, 255)
surfdemo_show(striped, 'striped')


#imgarray
imagename = os.path.join('data', 'arraydemo.jpg')
imgsurface = pygame.image.load(imagename)
imgarray = surfarray.array2d(imgsurface)
surfdemo_show(imgarray, 'imgarray')


#flipped
flipped = imgarray[:,-1:0:-1]
surfdemo_show(flipped, 'flipped')


#scaledown
scaledown = imgarray[::2,::2]
surfdemo_show(scaledown, 'scaledown')


#scaleup
size = N.array(imgarray.shape)*2
scaleup = N.zeros(size)
scaleup[::2,::2] = imgarray
scaleup[1::2,::2] = imgarray
scaleup[:,1::2] = scaleup[:,::2]
surfdemo_show(scaleup, 'scaleup')


#redimg
rgbarray = surfarray.array3d(imgsurface)
redimg = N.array(rgbarray)
redimg[:,:,1:] = 0
surfdemo_show(redimg, 'redimg')


#soften
soften = N.array(rgbarray)*1
soften[1:,:]  += rgbarray[:-1,:]*8
soften[:-1,:] += rgbarray[1:,:]*8
soften[:,1:]  += rgbarray[:,:-1]*8
soften[:,:-1] += rgbarray[:,1:]*8
soften /= 33
surfdemo_show(soften, 'soften')


#crossfade (50%)
src = N.array(rgbarray)
dest = N.zeros(rgbarray.shape)
dest[:] = 20, 50, 100
diff = (dest - src) * 0.50
xfade = src + diff.astype(N.Int)
surfdemo_show(xfade, 'xfade')



#alldone