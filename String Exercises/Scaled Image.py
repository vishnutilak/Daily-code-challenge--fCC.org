def scale_image(size, scale):
    dim = size.split('x')
    height = str(int(int(dim[0])*scale))
    width = str(int(int (dim[1])* scale))

    return height +"x"+ width
