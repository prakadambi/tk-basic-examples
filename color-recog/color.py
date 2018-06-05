from PIL import Image
import scipy
import scipy.cluster
from pprint import pprint
import scipy.misc
import codecs
import numpy
import matplotlib.pyplot as plt
from matplotlib.colors import hex2color, rgb2hex
#import webcolors
#import pyttsx
import sys
import Tkinter as Tk
import tkFileDialog

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def file_chooser():
    global filename
    filename=tkFileDialog.askopenfilename(initialdir="~/work/python_parse_genxml/latest_code/tk_examples/color-recog/",title="Select file",filetypes=(("jpeg files","*.jpg"),("all files","*.*")))
    print filename
    process_image(filename)

def process_image(filename):
    global main_frame
    Tk.Label(main_frame, text="Dominant color").grid(row = 5, column = 0,padx=10,pady=10)
    dom=Tk.Label(main_frame, text="",width=10)
    dom.grid(row = 5, column = 1,padx=10,pady=10)

    Tk.Label(main_frame, text="Auxillary color").grid(row = 6, column = 0,padx=10,pady=10)
    aux=Tk.Label(main_frame, text="",width=10)
    aux.grid(row = 6, column = 1,padx=10,pady=10)

    jpg_image = Image.open(filename)#Image.open(sys.argv[1])
    #disp_im=ImageTk.PhotoImage(image)
    file_gif=filename.replace("jpg","gif")
    file_gif=file_gif.replace("sample","esample")
    #print file_gif
    disp_im=Tk.PhotoImage(file=file_gif)
    Tk.Label(main_frame,text="Input Image").grid(row=4,column=0,padx=10,pady=10)
    img_label=Tk.Label(main_frame,height=80,width=120,image=disp_im)
    img_label.image=disp_im
    img_label.grid(row=4,column=1,padx=10,pady=10)
    NUM_CLUSTERS = 5

    # Convert image into array of values for each point.
    ar = scipy.misc.fromimage(jpg_image)
    shape = ar.shape
    #print (shape)

    # Reshape array of values to merge color bands.
    if len(shape) > 2:
        ar = ar.reshape(scipy.product(shape[:2]), shape[2])

    #print (ar.shape)
    # Get NUM_CLUSTERS worth of centroids.

    codes,_= scipy.cluster.vq.kmeans(ar.astype(float), NUM_CLUSTERS)

    #print(codes)

    # Pare centroids, removing blacks and whites and shades of really dark and really light.
    original_codes = codes
    for low, hi in [(60, 200), (35, 230), (10, 250)]:
        codes = scipy.array([code for code in codes 
                             if not ((code[0] < low and code[1] < low and code[2] < low) or
                                     (code[0] > hi and code[1] > hi and code[2] > hi))])
        if not len(codes): codes = original_codes
        else: break
    codes= codes.astype(int)
    #print(codes)


    # Assign codes (vector quantization). Each vector is compared to the centroids
    # and assigned the nearest one.
    vecs, _ = scipy.cluster.vq.vq(ar, codes)#index of the code array closest in ar
    #print(vecs)

    # Count occurences of each clustered vector.
    counts, bins = scipy.histogram(vecs, len(codes))

    #print(bins,counts)
    codes1=codes/255
    #print(codes1)

    colors=[rgb2hex(code) for code in codes1]
    #print(colors)

    total = scipy.sum(counts)
    #print(total)
    color_dist = dict(zip(colors, [count/float(total) for count in counts]))
    #print(color_dist)
    #print("counts are",counts)
    #print("codes are",codes)
    # Find the most frequent color, based on the counts.
    index_max = scipy.argmax(counts)
    #print("max index:",index_max)

    peak = codes[index_max]
    #print("Peak is ",peak)

    color = rgb2hex(peak/255)

    #engine = pyttsx.init()
    #rate = engine.getProperty('rate')
    #engine.setProperty('rate', rate-75)
    #voices=engine.getProperty('voices')
    #for voice in voices:
    #	if(voice.gender=="female"):
    #		engine.setProperty('voice',voice.id)
    #		break;

    #try:
            #c=webcolors.rgb_to_name(peak)
    print("Dominant Color is : ")
    print(peak)
    peak=tuple(peak)
    dom_col='#%02x%02x%02x' % peak
        #engine.say('The dominant color is ')
        #engine.say(c)
    '''except ValueError:
            closest_name = closest_colour(peak)
            dom_col='#%02x%02x%02x' % peak

            print("Dominant Color is : ")
            print(closest_name)
        #engine.say('The Dominant color is ')
        #engine.say(closest_name)'''

    # Find the most frequent color, based on the counts.
    counts=numpy.delete(counts,index_max)
    codes=numpy.delete(codes,index_max,0)

    #print("new counts is",counts)
    #print("new codes is",codes)
    index_max = scipy.argmax(counts)
    #print('2nd itermax is ',index_max)

    peak = codes[index_max]
    #print(peak)

    color = rgb2hex(peak/255)

    #try:
        #c=webcolors.rgb_to_name(peak)
    print("Auxillary Color is : ")
    print(peak)
    peak=tuple(peak)
    aux_col='#%02x%02x%02x' % peak
        #print(c)
        #engine.say('Auxillary color is ')
        #engine.say(c)
    '''
    except ValueError:
            closest_name = closest_colour(peak)
            print("Auxillary Color is : ")
            print(closest_name)
        #engine.say('Auxillary color is ')
        #engine.say(closest_name)
    #engine.runAndWait()
    '''
    dom["bg"]=dom_col
    aux["bg"]=aux_col


    #global filename
global main_frame
top = Tk.Tk()
main_frame = Tk.Frame(top)
main_frame.grid(column=0,row=0)#, sticky=(N,W,E,S) )
Tk.Label(main_frame, text="Welcome to the color recognition module!").grid(row = 1, column = 0,padx=10,pady=10)
Tk.Label(main_frame, text="Pick any image file to know the most dominant colors").grid(row = 2, column = 0,padx=10,pady=10)

Tk.Button(main_frame,
                   text="Choose a file",
                   fg="blue",
                   command=file_chooser).grid(column=0,row=3,padx=10,pady=10)

#print filename
top.mainloop()
