Preparing the data
==================

Data
----

The user of the CDTK can use the Data Dissemination Repository (DDR) to publish web services, downloadable files and Clip-Zip-Ship collections. The DDR support most GIS data formats, but there is some minimum settings required to make the publication workflow work.

.. _vector-data-ref:

Vector data
~~~~~~~~~~~

All vector data is stored in a PostGIS database on the DDR servers. The input data must be contained in a OGC Geopackage (GPKG) to be ingested by the DDR. If the user is using the DDR QGIS plugin to publish the data (see section  :ref:`qgis-plugin-ref`), then the vector layers will be automatically converted to a GPKG no matter the source format. If the user chooses the input package method (see section :ref:`directory-watcher-ref`), the source of the vector layers has to be stored in a GPKG included in the package.

	* **Using the QGIS plugin method**: Any vector format supported.
	
	* **Using the input package method**: All vector sources are stored in a GPKG.
	
``IMPORTANT: No matter the input format, the corresponding layers in both languages projects must have a common source containing both English and French attributes.``

Raster data
~~~~~~~~~~~

Any type of raster data is supported be the DDR. The data has to by stored on a web server accessible to the DDR. If the web services created are accessible publicly, the raster needs to be hosted on a public server as well. The data is not copied to the DDR servers, it remains in its original location and the web service produced calls and displays the data from its source. If the data source is not available, then the raster layer in the web service will fail to load.


.. _qgis-project-ref:

QGIS Project
------------

In order to publish web services with the DDR, the user needs to create one QGIS project file for each official language. The only format supported is ".qgs", ".qgz" is **not supported**. The projects have to be named with the following naming convention:

	* Project file names are in lower case.
	* The first character of the project file name must be a letter.
	* Only unaccented alphanumeric characters and underscores are allowed.
	* The English project file name ends with **"_en"**.
	* The French project file name ends with **"_fr"**.
	* The basenames of both projects are identical (i.e.: major_projects_en and major_projects_fr).
	* The user should not publish two projects named with the same first 15 characters (i.e.: **major_projects_**\ inventory_en and **major_projects_**\ index_en).

Converting from ESRI MXD file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Coming on next release.

.. _map-projection-ref:

Map and data projection
~~~~~~~~~~~~~~~~~~~~~~~

The DDR only support the 6 Coordinate Reference Systems (CRS) below. All the layers need to have the same CRS than the project.

	+------+---------------------------------------------+
	| EPSG | Description                                 |
	+======+=============================================+
	| 3857 | WGS 84 / Pseudo-Mercator (Google Maps, ESRI)|
	+------+---------------------------------------------+
	| 3978 | NAD83 / Canada Atlas Lambert                |
	+------+---------------------------------------------+
	| 3979 | NAD83(CSRS) / Canada Atlas Lambert          |
	+------+---------------------------------------------+
	| 4269 | NAD83                                       |
	+------+---------------------------------------------+
	| 4326 | WGS84 - World Geodetic System 1984          |
	+------+---------------------------------------------+
	| 4617 | NAD83(CSRS)                                 |
	+------+---------------------------------------------+

Project properties
~~~~~~~~~~~~~~~~~~

Each project should be built with care by filling some mandatory and suggested information. Mandatory information is required to make a successful publication, while the suggested information will increase the user experience and the discoverability of your dataset. 

* Mandatory:

	* In the "General" tab, set "Save paths" to "Relative".
	
	.. image:: media/project_properties_relative_path.png

	* In the "CRS" tab, choose a projection listed in the :ref:`map-projection-ref` section and make sure that all the layers use the same CRS.
	
	.. image:: media/crs_selection.png


* Suggested:

	* In the "Metadata" tab, as much information as possible about the project should be provided, particularly:
	
		* Title
		* Author
		* Abstract
		* ISO Categories
		* Keywords
	


Layer properties
~~~~~~~~~~~~~~~~

As for the project properties, each layer has to be configured individually with care. If the service is published to the Clip-Zip-Ship (see :ref:`czs-ref` section), only the metadata filled in the layer properties will appear in the CZS as each layer will create an individual collection.

* Mandatory:

	* In the "QGIS Server" tab, each layer must have a unique short name. 
	
	.. image:: media/layer_short_name.png

	* The corresponding layer in the other language's project must have the exact **same short name**.
	
	* There is no need to fill the other fields in that tab as any information inputed in the "Metadata" will be automatically copied over to the "QGIS Server" tab by the DDR process.


* Suggested:

	* In the "Metadata" tab, as much information as possible about the layer should be provided, particularly:
	
		* Title
		* Author
		* Abstract
		* ISO Categories
		* Keywords

	* In the "Fields" tab, it is possible to hide some fields from the GetFeatureInfo response in the web service. By example, French attributes can be hidden in the English project and vice-versa.
	
	.. image:: media/fields.png
	
	* To enhance user experience, field aliases should be set in the "Attributes Form" tab. 
	
	.. image:: media/aliases.png
	
	* If the layer is time-enabled, please fill the necessary information in the "Temporal" tab.
	
	
Downloads
---------

The CDTK includes a public FTP distribution site where the user can make files available for download. The process of uploading these files is integrated to the DDR publication mecanism. 

	1. Create a distinct folder containing all the files and subfolders to be stored on the FTP site.
	
	2. Compress this folder into a .zip file (other extensions not supported).
	
The download package is now ready to be joined to the publication (see :ref:`submit-ref` section).
