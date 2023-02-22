2. Preparing the data
=====================

2.1. Data
---------

The CDTK support most GIS data formats, but there is some minimum settings required to make the publication workflow work.

2.1.1. Vector data
~~~~~~~~~~~~~~~~~~

All vector data is stored in a PostGIS database on the CDTK servers. The input data must be contained in a OGC Geopackage (GPKG) to be ingested by the CDTK. If the user is using the CDTK QGIS plugin to publish the data (see section  :ref:`qgis-plugin-ref`), then the vector layers will be automatically converted to a GPKG no matter the source format. If the user chooses the input package method (see section :ref:`directory-watcher-ref`), the source of the vector layers has to be stored in a GPKG included in the package.

	* **Using the QGIS plugin method**: Any vector format supported.
	
	* **Using the input package method**: All vector sources are stored in a GPKG.
	
**IMPORTANT:** No matter the input format, the corresponding layers in both languages projects must have a common source containing both English and French attributes.

2.1.2. Raster data
~~~~~~~~~~~~~~~~~~

Any type of raster data is supported be the CDTK. The data has to by stored by the user on a web server accessible to the CDTK. The data is not copied to the CDTK servers, it remains in its original location and the web service produced calls and displays the data from its source. If the data source is not available, then the raster layer in the web service will fail to load.

2.2. QGIS Project
-----------------

In order to publish web services with the CDTK, the user needs to create one QGIS project file for each official language. The only format supported is ".qgs", ".qgz" is **not supported**. The projects have to be named with the following naming convention:

	* Project file names are in lower case.
	* The English project file name ends with **"_en"**.
	* The French project file name ends with **"_fr"**.
	* The basenames of both projects are identical (i.e.: major_projects_en and major_projects_fr).
	* The user should not publish two projects named with the same first 15 characters (i.e.: **major_projects_**\ inventory_en and **major_projects_**\ index_en).

2.2.1. Converting from ESRI MXD file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

À remplir

.. _map-projection-ref:

2.2.2. Map and data projection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The CDTK only support the 6 Coordinate Reference Systems (CRS) below. All the layers need to have the same CRS than the project.

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

2.2.3. Project properties
~~~~~~~~~~~~~~~~~~~~~~~~~

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
	


2.2.4. Layer properties
~~~~~~~~~~~~~~~~~~~~~~~

As for the project properties, each layer has to be configured individually with care. If the service is published to the Clip-Zip-Ship (see :ref:`czs-ref` section), only the metadata filled in the layer properties will appear in the CZS as each layer will create an individual collection.

* Mandatory:

	* In the "QGIS Server" tab, each layer must have a unique short name. 
	
	.. image:: media/layer_short_name.png

	* The corresponding layer in the other language's project must have the exact **same short name**.
	
	* There is no need to fill the other fields in that tab as any information inputed in the "Metadata" will be automatically copied over to the "QGIS Server" tab by the CDTK process.


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
	
	
2.3. Downloads
--------------

À remplir
