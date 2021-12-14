import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.type_check import real

def mandel(x,y,size,pixels,filename):
    """Plots a mandelbrot structure with given values and saves figure in the given filname"""
    xmin, xmax = x, x + size
    ymin, ymax = y, y+size
    num_pixels = pixels

    # initial setup of calculation constant C for each pixel
    X = np.linspace(xmin, xmax, num_pixels)[None,:]
    Y = np.linspace(ymin, ymax, num_pixels)[:,None]
    C = X + 1j * Y
    # start value of Z is always 0
    Z = np.zeros_like(C)
    # P counts iterations, this is what we plot at the end
    P = np.zeros_like(C, dtype='uint8') # unsigned int 0..255

    # iteration of Z <- Z*Z + C
    for i in range(120):
        # print(f"Iteration {i}")
        # which elements are still "live"?
        live = np.abs(Z) < 2.
        # update live pixels with current iteration number
        P[live] = i 
        # iterate
        Z[live] = Z[live]*Z[live] + C[live] 

    plt.imshow(
        P, 
        origin='lower',
        extent=(X.min(), X.max(), Y.min(), Y.max())
    )
    plt.savefig(filename)

def mandel_zoom(old_x,new_x,old_y,new_y, old_size, new_size, pixels, num_steps):
    """Saves num_steps figures of mandelbrots zooming with each step towards"""
    # Lists of xs, ys and sizes to go through
    xs = np.linspace(old_x,new_x,num_steps)
    ys = np.linspace(old_y,new_y,num_steps)
    sizes = np.linspace(old_size,new_size,num_steps)

    # Loop through steps and save figures
    for i in range(num_steps):
        # Calculate zeros to add in filename, example "zoom_01.png"
        length_max_num = len(str(num_steps))
        zeros_to_add = (length_max_num - len(str(i)) + 1) * "0"
        filename = f"zoom_{zeros_to_add}{i}.png"
        mandel(xs[i],ys[i],sizes[i],pixels,filename)
    
# Will continuously
while True:
    # Take in input numebrs
    pixels = input("Antall pixeler: ")
    num_images = input("Antall zoom-bilder: ")
    try:
        # Try to format as integers, ValueError will be raised if it is not possible
        pixels = int(pixels)
        num_images = int(num_images)
        # Run mandel_zoom if all is well
        mandel_zoom(-2, 0, -1.5, 0, 3, 0.009, pixels, num_images)
    except ValueError:
        # ValueError is catched and message about integers is written
        print("Vennligst skriv inn kun heltall :)")

