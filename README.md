**Mahalanobis distance plugin**
---------------------------
QGIS Plugin. Calculates distance that indicates which regions in a landscape are most similar to some ideal landscape. More about mahalanobis distance: http://www.jennessent.com/arcview/mahalanobis_description.htm

**License:**

Copyright (C) MahalanobisDistance, Author: Damian Harasymczuk

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.


**Input:** 

 - Singleband raster layers. Each layer should depict the same area.
 - Mean value. A single value for each raster.

**Output:**

 - Singleband raster layer. Size and geodata are taken from first input
   layer on the list (top row in the input table).

**Example:**
Test data

*Input layer #1 temperature*
![enter image description here](http://i.imgur.com/yvshEx8.png)

*Input layer #2 precipitation*
![enter image description here](http://i.imgur.com/Wl1rqnt.png)

*Find areas closest to the ideal conditions: temperature=18, precipitation=110*
![enter image description here](http://i.imgur.com/4jf5FxY.png)

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 4cbec1042da057b49e239cfd8bb310db0054b1d6
*Result*
![enter image description here](http://i.imgur.com/abuqduA.png)

*Green areas are closest to the ideal landscape.*
<<<<<<< HEAD
![enter image description here](http://i.imgur.com/jnuFfXt.png)
=======
![enter image description here](http://i.imgur.com/jnuFfXt.png)
=======
*Result                       *
![enter image description here](http://i.imgur.com/abuqduA.png)

*Green areas are closest to the ideal landscape.*
![enter image description here](http://i.imgur.com/jnuFfXt.png)
>>>>>>> a121f8a9e46fb5f9963d92e10881bb92270438fb
>>>>>>> 4cbec1042da057b49e239cfd8bb310db0054b1d6
