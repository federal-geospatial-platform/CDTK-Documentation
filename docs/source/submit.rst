.. _submit-ref:

3. Submitting data to CDTK
==========================

.. _publication-method-ref:

3.1. Choosing a publication method
----------------------------------

The CDTK has 2 publication mecanisms avaiblable to its users. Each mecanism have its pros and cons, it's up to the user to choose the one who better suits the operational needs. The user can switch from a publication method to another at any time.

	+-------------------+------------------------------------------------------------------+------------------------------------------------------+
	| Method            | Pros                                                             | Cons                                                 |
	+===================+==================================================================+======================================================+
	| QGIS Plugin       | * Any vector format supported                                    | * Publication parameters have to be entered each time|
	|                   |                                                                  |                                                      |
	|                   | * No data packaging needed                                       |                                                      |
	|                   |                                                                  |                                                      |
	|                   | * Easy user interface                                            |                                                      |
	|                   |                                                                  |                                                      | 
	+-------------------+------------------------------------------------------------------+------------------------------------------------------+
	| Directory watcher | * Easy scripting                                                 | * Only vector format supported is GPKG               |
	|                   |                                                                  |                                                      |
	|                   | * Publication parameters entered only once in a control file     | * No graphic interface                               |
	|                   |                                                                  |                                                      |
	|                   |                                                                  | * Data needs to be packaged properly                 |
	|                   |                                                                  |                                                      |
	+-------------------+------------------------------------------------------------------+------------------------------------------------------+


.. _qgis-plugin-ref:

3.2. Using the QGIS Plugin
--------------------------

The simpliest way to publish a web service with the CDTK in to use the QGIS plugin. The plugin only works on the GC Network, make sure you are on a government network or connected trough a VPN.

3.2.1. Plugin installation
~~~~~~~~~~~~~~~~~~~~~~~~~~
	
	1. To install the plugin, open QGIS and go to "Plugins -> Manage and Install Plugins".
	
	.. image:: media/qgis_plugins.png
	
	2. In the "Settings" tab, click on "Add..." and input a name (CDTK) and the URL of the repository: https://federal-geospatial-platform.github.io/Plugin_Repository/plugins.xml
	
	.. image:: media/qgis_add_repo.png

	3. In the "Not installed" tab, select the plugin called "CDTK" and click on "Install Plugin". 
	
	.. image:: media/qgis_install.png
	
3.2.2. Plugin login
~~~~~~~~~~~~~~~~~~~

	1. To use the plugin, head to the QGIS Processing Toolbox ("Processing -> Processing Toolbox").
	
	.. image:: media/qgis_toolbox.png

	2. 

	.. image:: media/qgis_add_repo.png

.. _directory-watcher-ref:

3.3. Using the directory watcher
--------------------------------

À remplir

3.3.1. Creating a control file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

À remplir

3.3.2. File packaging
~~~~~~~~~~~~~~~~~~~~~

3.4. System messaging
---------------------

À remplir