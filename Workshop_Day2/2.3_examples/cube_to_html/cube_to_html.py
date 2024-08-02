# ---------------------------------------------------------------------------------------
#
# cube_to_html.py
#
# This program takes the absolute path to a cubefile from the command line and generates
# an html file for visualization in the same folder with the same name. This requires a
# local edit to the moly package to extend the figure class (figure.py) with the function
# write_html from plotly graph objects.
#
# Created Feb 15 2024 by Isaac Spackman
# ---------------------------------------------------------------------------------------
import moly 
import sys

# set default values
isovalue = 0.01
mystyle="ball_and_stick"

# get user inputs
for i in range(len(sys.argv)):
    try:
        if sys.argv[i] == "-f":
            # get the absolute path to the cubefile from command line
            cubeFile = sys.argv[i+1]
    except IndexError:
        sys.exit("NO CUBE FILE PROVIDED")
    try:
        if sys.argv[i] == "-i":
            # update the isovalue to the user selection
            isovalue = float(sys.argv[i+1])
    except IndexError:
        print("NO ISOVALUE PROVIDED- USING DEFAULT")
    except ValueError:
        print("INVALID ISOVALUE- USING DEFAULT")
    try:
        if sys.argv[i] == "-s":
            # update the style to the user selection
            mystyle = sys.argv[i+1]
    except IndexError:
        print("NO ISOVALUE PROVIDED- USING DEFAULT")


# create a new absolute path to the desired output html file
fileName = cubeFile.split("//")[-1]
fileName = fileName[:-4] + "html"


fig = moly.Figure()

# accepts plotly graph object color scales
fig.add_cube(
    cubeFile,
    colorscale="Bluered",
    iso=isovalue,
    opacity=0.1,
    style=mystyle
)


fig.write_html(fileName)

# note this requires an extension of the default moly figure class that must be edited locally
# you can add this functionality by opening the figure.py file within your moly distribution
# and adding the new class function write_html(self,path) that uses the plotly function write_html
