# module imports
from PIL import Image

# import pixel array tables with rare rolls
# these values and attributes are applied to the type of Python rolled below
from pythonsnft_arrays import *

# Roll for Python type
for y in range(100):
        y = random.randint(0, 100)

        if y in range(0, 61):        # if random number is less than 60, garter
                array = array_1 # garter array

        elif y in range(61, 87):     # if random number is between 61 and 86, rattlesnake
                array = array_2 # rattler array

        elif y in range(87, 97):     # if random number is between 87 and 97, cobra
                array = array_3 #cobra array

        else:                      # if random number is 97 or greater, mamba
                array = array_4 # mamba array


# dtype=np.uint8 converts array table RGB values to integers and creates image
arr = np.array(array, dtype=np.uint8)
python_image = Image.fromarray(arr)

# resize image larger, keeping 24x24 pixel format
resize = (400, 400)
python_image = python_image.resize(resize, resample=0)

# save image
# python_image.save("copy&paste_your_file_path/define_filename.png", 'PNG')

# show image on screen
python_image.show()
