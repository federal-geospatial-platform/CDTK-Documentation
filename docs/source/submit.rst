.. _submit-ref:

3. Submitting data to the DDR
=============================

.. _publication-method-ref:

3.1. Choosing a publication method
----------------------------------

The DDR has 2 publication mecanisms avaiblable to its users. Each mecanism have its pros and cons, it's up to the user to choose the one who better suits the operational needs. The user can switch from a publication method to another at any time.

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

``For projects with a large amount of data (over ~500 MB), the Directory Watcher should be prefered. The user may experience a lack of response from the plugin with large files. We are working on fixing this issue.``

.. _qgis-plugin-ref:

3.2. Using the QGIS Plugin
--------------------------

The simpliest way to publish a web service with the DDR in to use the QGIS plugin. The plugin only works on the Government of Canada Network, make sure you are on a government network or connected trough a VPN.

3.2.1. Plugin installation
~~~~~~~~~~~~~~~~~~~~~~~~~~
	
	1. To install the plugin, open QGIS and go to "Plugins -> Manage and Install Plugins".
	
	.. image:: media/qgis_plugins.png
	
	2. In the "Settings" tab, click on "Add..." and input a name (like "GeoDiscovery ") and the URL of the repository: https://federal-geospatial-platform.github.io/Plugin_Repository/plugins.xml
	
	.. image:: media/qgis_add_repo.png

	3. In the "Not installed" tab, select the plugin called "DDR Processing" and click on "Install Plugin". 
	
	.. image:: media/qgis_install.png
	
3.2.2. Plugin login
~~~~~~~~~~~~~~~~~~~

	1. To use the plugin, head to the QGIS Processing Toolbox ("Processing -> Processing Toolbox").
	
	.. image:: media/qgis_toolbox.png

	2. In the "DDR Publication" tool, expand "Authentication (first step)" and double-click on "DDR Login".

	.. image:: media/ddr_login.png
	
	3. The first time the plugin is used, click on the + sign to add new credentials.

	.. image:: media/add_creds.png
	
	4. Enter a connection name and input the GeoAD credentials provided by our support team (:ref:`help`).

	.. image:: media/authentication.png
	
	5. Now, with the new connection selected, hit the Run button to connect to the DDR.

.. _qgis-plugin-publish:

3.2.3. Publish
~~~~~~~~~~~~~~

The first time a dataset is published to the DDR, the user needs to perform a "DDR Publish". In the "DDR Publication" tool, select "Publish Project File" and input the following parameters. To make sure the package is correctly built, it is possible to perform a validation before publishing (see :ref:`ddr-validate`).

	1. Select the English project file (.qgs only).
	
	2. Select the French project file (.qgs only).
	
	3. Select a department from the list of department for which you are authorized to publish.
	
	4. Enter the medata ID of the record in the FGP catalogue.
	
	5. If you want your layers to be available as a Clip-Zip-Ship collection, select a theme [optional].
	
	6. Select the server for the download package when applicable.
	
	7. Select the QGIS server for the web services.
	
	8. In the advanced parameters, a different email for the reception of the publication report can be inputed.
	
	9. In the advanced parameters, the user can choose to keep the temporary package used to publish.

	.. image:: media/publish.png
	
3.2.4. Unpublish
~~~~~~~~~~~~~~~~

To remove a dataset from the DDR, select "Unpublish Project File" from the "DDR Publication" tool. Any corresponding collection published in the Clip-Zip-Ship will be automatically deleted by this process.

	1. Select the English project file (.qgs only).
	
	2. Select the French project file (.qgs only).
	
	3. Select the department in which the dataset is published.
	
	4. Select the server on which the downloadable files are published.
	
	5. Select the QGIS server on which the web services are published.
	
	6. In the advanced parameters, a different email for the reception of the unpublication report can be inputed.
	
	7. In the advanced parameters, the user can choose to keep the temporary package used to unpublish.

	.. image:: media/unpublish.png
	
3.2.5. Update
~~~~~~~~~~~~~

The update (republish) works exactly like the publish, but it allows the user to update an existing dataset. The parameters are the same than :ref:`qgis-plugin-publish`.

.. _ddr-validate:

3.2.3. Validate
~~~~~~~~~~~~~~~

Before sending their data to Publication, Update or Unpublication, the users can validate the content of a QGIS project file (.qgs) and its control file by using Validate. Select what process you want to validate your data for and look at the results in the Log tab.

	.. image:: media/validate.png

.. _directory-watcher-ref:

3.3. Using the directory watcher
--------------------------------

The directory watcher is an alternative publication method that consists in dropping a zipped package on a sFTP server. It can be useful for projects that require frequent updates. File creation and transmission can also be scripted from end-to-end. It is also the prefered method when dealing with large datasets.

Files needed for a publication or update using the directory watcher:

	* Control file
	* English QGS file
	* French QGS file
	* Geopackage(s) containing the data
	* Zipped download folder [optional]

3.3.1. Creating a control file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instead of using a user interface, the user must set up a control file to record their instructions. `Download the template`_ and fill the required information. The file included in the package must be named exactly "ControlFile.xlsx".

**Generic parameters tab:**

	* Email: The user email address (must be a registered user address).
	* Department: The official English department acronym (user must be authorized to publish for this department).
	* Metadata Record Identifier: The UUID of the related FGP metadata record.
	* CZS Collection Thematic [optional]: To register the collections in the Clip-Zip-Ship, select a theme.
	* QGIS Server ID [optional]: Leave this parameter empty for the moment.
	* Download repository ID [optional]: Leave this parameter empty for the moment.
	* Download folder name [optional]: The name of the folder inside the ZIP file containing the downloadable data.
	* Core Subject Term [optional]: To publish files to the FTP server, select a core subject term.
	
	.. image:: media/generic_parameters.png
	

**Service parameters tab:**

	* Service Language: Leave as is.
	* Project Filename: Name of the QGIS project files.
	* Service Name: Filed automaticaly based on the project filename.
	* Service Folder Name: Filled automatically based on the department specified in the other tab.

	.. image:: media/service_parameters.png
	
.. _Download the template: https://ftp.maps.canada.ca/pub/ddr_rdd/CDTK/templates_gabarits/ControlFile.xlsx

3.3.2. Preparing data
~~~~~~~~~~~~~~~~~~~~~

To create a complete input package, the following files must be included:

	* An English QGIS project file (see :ref:`qgis-project-ref`).
	* A French QGIS project file  (see :ref:`qgis-project-ref`).
	* A single Geopackage (GPKG) containing all the vector data (see :ref:`vector-data-ref`).
	* A control file named "ControlFile.xslx".
	* A zipped download folder [optional]
	
``Note: If the package is meant to publish/update only the downloads folder, clear the cells in the "Service parameters" tab of the Control file.``


3.3.3. File packaging
~~~~~~~~~~~~~~~~~~~~~

The files mentioned above must be present at the root of the ZIP file (not in a subfolder). The optional download folder must be named like in the "Download folder name (ftp root folder name)" parameter of the ControlFile and then zipped.

	.. image:: media/packaging.png

3.3.4. Sending the package for processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To drop an input package into the DDR, the user must have a GeoAD account and be a registered DDR user (see :ref:`help`). With your credentials in hand, use a FTP client like `FileZilla`_ to connect to the sFTP server.

	* Protocol: SFTP - SSH File Transfer Protocol.
	* Host:
	
		* Production: ftp-update.services.geo.ca
		* Staging: ftp-update-stage.services.geo.ca
		
	* User: Provided by the support, usually firstname-lastname.
	* Password: Provided by the support.
	

	.. image:: media/filezilla.png
	
Once connected, go in the "DDR_Directory_Watcher_Folder" folder and select your department's subfolder. Drop the package in the desired opeation subfolder.

	* DDR_Publish: Publishes web services and/or  for the first time.
	* DDR_Unpublish: Deletes a service and the Clip-Zip-Ship collections if any.
	* DDR_Updates: Updates an existing service (and Clip-Zip-Ship collections if any) and/or an existing download package.
	* DDR_Conditioning: Starts a conditioning process (must be put in place with the support, see :ref:`help`).

	.. image:: media/dw.png

	.. _FileZilla: https://filezilla-project.org/download.php

3.4. System messaging
---------------------

When the package processing is done, the DDR sends an email with the outcome of the operations (success or failure). If you don't receive the email, make sure to withelist the address ddr.fgpservices-servicespgf.rdd@aws.nrcan-rncan.cloud (please don't write to that unsupervised mailbox). If you still don't receive an email, contact the support: :ref:`help`.