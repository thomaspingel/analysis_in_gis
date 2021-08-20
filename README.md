# analysis_in_gis

These notebooks with require an installation of [ArcGIS Pro](https://apps.itpals.vt.edu/arcgis/ArcGIS_Pro_Installation_Instructions.pdf) and Anaconda with a class environment.

#### Anaconda installation instructions
* [Download and install the software](https://www.anaconda.com/products/individual).  It's free, and can install on Windows, Linux, and Mac.
* The default installation of Anaconda comes with numpy, Pandas, matplotlib, and many other useful packages.  However, it does not come with many geospatial packages.  Installation of these can sometimes be challenging.  There are two main ways to do it.  First, you can use Anaconda's package manager conda to do it.  Or, you can use pip, Python's primary installer.  Both have benefits and drawbacks.  However, we'll use conda to do most of it.
* Install instructions after opening an Anaconda command window (paste these three lines in, one-at-a-time; the third one is long!)
~~~
conda create --name analysis_in_gis --file https://nearearthimaginglab.org/python/neil.20210708.txt
conda activate analysis_in_gis
pip install opencv-python notebook-as-pdf
~~~
From here, you should be able to close the window, and use normally except that: when you open the Anaconda command window, in addition to changing directory to your working directory you'll need to type
~~~
conda activate analysis_in_gis
~~~ 
