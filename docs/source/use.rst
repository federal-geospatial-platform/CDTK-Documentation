4. Using the results
====================

4.1. Access links
-----------------

4.1.1. Web services
~~~~~~~~~~~~~~~~~~~

When a publication or update process completes successfuly, the user receives an email containing the links to the web services. 

.. image:: media/email.png

4.1.2. Downloads directory
~~~~~~~~~~~~~~~~~~~~~~~~~~

If the user added a download directory, the links to the downloadable files will be sent in a separate email.

4.2. Using an OGC web service
-----------------------------

The QGIS Servers are able to serve data according to strandard protocols as described by the **Open Geospatial Consortium (OGC)**. Extra vendor parameters and requests are supported in addition to the original standard that greatly enhance the possibilities of customizing its behavior thanks to the QGIS rendering engine. The followings protocols are available by default when publishing a service with the DDR:

	* WMS 1.1.1 and 1.3.0
	* WFS 1.0.0 and 1.1.0
	* WCS 1.0.0 and 1.1.1
	* WMTS 1.0.0
	
To get more information about the different protocols, refer to the `QGIS Server documentation`_.

.. _QGIS Server documentation: https://docs.qgis.org/3.28/en/docs/server_manual/services.html

4.2.1. GetCapabilities
~~~~~~~~~~~~~~~~~~~~~~

The URL in the success email consists in the GetCapabilities request for the WMS protocol. It can be used to call the service within an application or map viewer. It can also be consulted as a XML in a web browser to get information about the structure and metadata of the web service.

The URL for the GetCapabilities is made of 5 different parts:

	* The base URL of the QGIS server.
	* The schema name in the PostGIS database (the provided department name).
	* The project name to access.
	* The protocol to be used (values are WMS/WFS/WCS/WMTS).
	* The desired version (depends on the protocol).
	* The request type (GetCapabilities)
	
	.. image:: media/getcap.png

4.2.2. GetMap
~~~~~~~~~~~~~

À remplir

