import imageio

image_names = map(lambda x: "tr%dks.jpg" % (x + 1), range(9))
images = list(map(lambda name: imageio.imread(name), image_names))

for i in range(len(images)):
    img = images[i]

    print("._%d {" % i)
    pixel = img[0][0]
    print("background: #%02x%02x%02x;\n}" % (pixel[0], pixel[1], pixel[2]))

    print("._%d .tausch {" % i)
    pixel = img[120][130]
    print("fill: #%02x%02x%02x;\n}" % (pixel[0], pixel[1], pixel[2]))

    print("._%d .rausch {" % i)
    pixel = img[211][220]
    print("fill: #%02x%02x%02x;\n}" % (pixel[0], pixel[1], pixel[2]))

    print("._%d .misc {" % i)
    pixel = img[325][595]
    print("color: #%02x%02x%02x;\n}" % (pixel[0], pixel[1], pixel[2]))

    print()