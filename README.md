HDR Image Synthesizer
=====================

HDR is a simple Python script to create high dynamic range images from a list of pictures.

Usage
-----

The command line interface is quite simple:

```
HDR -f originals
```

This will load all the images contained in the folder _originals_, order it by lightness and create a HDR image named _out.jpg_ in the current folder.

Options
-------

The script accepts a number of options to customize its behaviour.

* __-h__, __--help__
	* show the help message and exit
* __-f FOLDER__, __--folder FOLDER__
	* the folder from which the images will be loaded
* __-o OUTPUT__, __--output OUTPUT__
	* the output file. _Default: out.jpg_
* __-b BLEND__, __--blend BLEND__
	* the blending factor used for creating the masks. _Default: 0.5_
* __-r__, __--reverse__
	* reverse the sorting direction
* __-d__, __--debug__
	* prints debug information during the process
* __-v__, __--version__
	* output version information and exit
	
Bug tracker
-----------

Have a bug? Please create an issue here on GitHub!

https://github.com/ganglio/HDR/issues

Twitter account
---------------

Keep up to date on my blurbs by following ganglio on Twitter, <a href="http://twitter.com/ganglio">@ganglio</a>.

Authors
-------

**Roberto Torella**

+ http://twitter.com/ganglio
+ http://github.com/ganglio

**Michela Esposito**

+ http://twitter.com/crumpledleaf

Copyright and license
---------------------

Copyright 2011 Roberto Torella

This work is licensed under a <a href="http://creativecommons.org/licenses/by-nc-sa/3.0/">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License</a>.
