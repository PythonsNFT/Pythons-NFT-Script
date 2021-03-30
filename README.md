# Pythons-NFT-Script
I've uploaded my code used to generate PythonsNFT as free and open source under a MIT license. This project was my first deep dive into Python to create something other than homework excercises from training courses. At the time of writing and posting the code, I feel like I've already learned so much more and would do many things differently. I'm sure to an intermeidate or seasoned programmer the code is pretty clunky and ugly, but as a beginner I'm thrilled to have been able to generate what was in my head through something completely new to me. 

Google and Stack Overflow were very heavily utilized and referenced throughout (and still are). My biggest obsticle was figuring out how to actually draw pixels through code to generate the Pythons. At first I was trying to compile the Pythons by merging together layers of pixel drawings I made, but this was becoming very labor intensive and I wasn't sure how to technically integrate image merges with the For loop statements, which was the one thing that felt most comfortable to me. I kept seeing references to Numpy in deep Google dives on how to draw pixels with code and once I discovered that np.array() could be used with variables to plot pixels with defined RGB values, that was the breakthrough I needed conceptually to begin pulling it all together.  This still led to many hours of trial and error but I could see a path forward. One easy change I would make/recommend to anyone using this script is to integrate the array tables and main script into one file.  Breaking them out was not necessary and was not Python Zen.

In conclusion, I feel like I learned a lot and it was great first immersive dive into Python. Many things in this script could be done more effeciently and I would encourage this script be used as a starting or jumping off point to be modified. 

Note on Running the Script:
I used the IDE PyCharm to construct and execute the script, which required some manual installation of Python Interpreters through the PyCharm preferences menu. Running the script will only generate 1 image at a time


Helpful references regarding Numpy arrays for images:
https://bic-berkeley.github.io/psych-214-fall-2016/arrays_and_images.html

https://www.datacamp.com/community/tutorials/python-numpy-tutorial

https://numpy.org/doc/stable/user/basics.creation.html

https://numpy.org/doc/stable/user/basics.indexing.html


Other beginner helpful resources:
https://docs.python.org/3/tutorial/controlflow.html

https://pynative.com/python-random-randrange/

*edits for grammer
