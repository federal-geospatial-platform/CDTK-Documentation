.. table:: Table 1: Metadata Field Description

   +----------------------------------------+----------+------------------+
   | .. image:: vertopal_40208e89b75        |          |                  |
   | 1415fb056b7bec6b8446b/media/image1.png |          |                  |
   |    :width: 6.425in                     |          |                  |
   |    :height: 1.475in                    |          |                  |
   |                                        |          |                  |
   | **FGP Standard Operating Procedure**   |          |                  |
   +----------------------------------------+----------+------------------+
   | Category: Federal Geospatial Platform  |          | Doc type:        |
   |                                        |          | **Procedure**    |
   +----------------------------------------+----------+------------------+
   | Filename:                              | SOP      | Date:            |
   | **SOP44                                | Number:  | **2016-12-23**   |
   | 01-DDRInputPackageCreation_aa03.docx** |          |                  |
   |                                        | SOP-4401 |                  |
   +----------------------------------------+----------+------------------+
   | Version Issue and Status: **aa03 open  | SOP      |                  |
   | draft**                                | C        |                  |
   |                                        | ategory: |                  |
   |                                        | 4000     |                  |
   |                                        | Data     |                  |
   |                                        |          |                  |
   |                                        | Sub-c    |                  |
   |                                        | ategory: |                  |
   |                                        | 4400     |                  |
   |                                        | Data     |                  |
   |                                        | Disse    |                  |
   |                                        | mination |                  |
   |                                        | Re       |                  |
   |                                        | pository |                  |
   +----------------------------------------+----------+------------------+

SOP-4401 – DDR Input Package Creation 
======================================

Purpose
-------

The purpose of this document is to describe the input information
required to make the Data Dissemination Repository (DDR) services work
properly. It explains how to create the different input packages used by
the Contributor Support Team to launch the DDR services. It is intended
for use by anyone who has the rights to submit data and Web services to
the DDR with the possibility for Client Departments who have less
expertise in creating geospatial services to be assisted by the
Contributor Support Team.

Scope
-----

This procedure applies to all input package creation. When it comes to
submitting it to the FGP DDR subsystem, client departments must contact
the contributors support team who will complete the process in their
name. This situation will remain as long as the FGP access control and
cost model are not completely defined and implemented. In the future,
Client Departments will have the ability to submit their package
themselves, with or without Contributor Support Team assistance.

Responsibility in FGP
---------------------

.. table:: Table 2: Naming Concatenation Table

   +------------+---------------------------------------------------------+
   | **A        | FGP DDR Team Lead                                       |
   | uthority** |                                                         |
   +------------+---------------------------------------------------------+
   | **C        | The CST is the interface between the contributor and    |
   | ontributor | the Catalogue, the DDR storage, and the web services    |
   | Support    | group.                                                  |
   | Team**     |                                                         |
   +------------+---------------------------------------------------------+
   | **Client   | The CS Help team assist the contributor in the          |
   | Services   | preparation of the DDR input package.                   |
   | Help**     |                                                         |
   +------------+---------------------------------------------------------+

Records and References
----------------------

**UUID** Use this reference
http://www.gcpedia.gc.ca/wiki/Federal_Geospatial_Platform/Policies_and_Standards/Catalogue/Release

**Naming Convention** Use the Federal Geospatial Platform/Policies and
Standards/Catalogue/Release/Appendix B Guidelines.

**Metadata Excel Spreadsheet Template** <enter the name of the
spreadsheet template here>

**Thesaurus** You can find the core subject thesaurus at
http://www.thesaurus.gc.ca/default.asp?lang=En&n=EAEAD1E6-1

**Data Projections** FGP contributors are strongly encouraged to make
their data available in one or more of the four projections presented
here in order of preference:

1. NAD83 / Canada Atlas Lambert EPSG:3978 `> <http://epsg.io/3978>`__
      http://epsg.io/3978

2. WGS84 / Pseudo-Mercator EPSG:3857 `> <http://epsg.io/3857>`__
      http://epsg.io/3857

3. NAD83 (CSRS) / Canada Atlas Lambert EPSG:3979
      `> <http://epsg.io/3979>`__ http://epsg.io/3979

4. NAD83 (CSRS) EPSG:4617 `> <http://epsg.io/4617>`__
      http://epsg.io/4617

Description and Usage
---------------------

The DDR is a subsystem of the FGP which, combined with the catalog,
allows users to instantiate geospatial services in a controlled data
repository. Standardization of the repository structure and its access
mechanism ensures the integrity of the data and services published in
the FGP. ArcGIS and FME deployed on a cluster of servers form the
infrastructure behind DDR.

The cluster also incorporates a shared storage, an FTP server, a
database, and many other components needed by the system to perform its
tasks.

Refer to Figure 1, below. DDR offers three different services: publish,
unpublish and update. To publish, the metadata entry must precede a call
to the FGP catalogue. At the end of a successful link, the user receives
an email with the URL link to perform an online resource update to the
catalogue.

The unpublish service allows the user to delete the downloadable data
and map services that are not needed anymore in the DDR.

The update service is a way of chaining the two previous services in
order to completely unpublish and republish the downloadable data and
map services to the DDR.

.. image:: vertopal_40208e89b751415fb056b7bec6b8446b/media/image2.png
   :width: 6.5in
   :height: 4.04236in

Figure 1: DDR Input Package Creation

Publish and Update Input Package Creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The publish and update services use the same input package to capture
the needed parameters to perform their respective tasks. There is an
Excel spreadsheet template to facilitate the collection of needed
information. The following sections describe the sections found in the
Excel template.

The standard input to the DDR publish service is a set of files
organized as a package. The package must be compressed (zipped) to ease
transfer and conserve disk space. All files must be put in the input
package root directory. This section presents the files that may be
added into the input package, depending on whether web services or
download services are requested.

Esri File Geodatabases (FGDB)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  There should be one FGDB for French and one for English or only one
   bilingual FGDB.

-  FGDB at release 10.1 or better.

-  FGDB Feature Classes spatial reference system must be the same as the
   one set in the Data Frame Properties of ArcMap. In addition, the
   selected spatial reference system should be the same as the one
   targeted for the viewer (see Appendix A: Naming conventions).The base
   map selected uses the spatial reference system used by the viewer. If
   the spatial reference system is not the same, re-projection will need
   to occur.

-  Each of the feature class in the FGDB:

-  Contains only one type of feature (for example, only points or only
   lines or only polygons)

-  Contains only simple 2D or 3D features.

-  May contain multi-parts or single-part features.

-  May contain features with elevation (z) and measures (m).

-  Follows the proposed naming convention (see Files Geodatabase (FGDB);
   Feature Class Naming Standard).

-  Have one or more attributes characterizing each feature beyond the
   unique system identifier (OBJECTID).

-  Follows the proposed attributes naming convention (see Appendix A:
   Naming conventions\ `10 <#appendix-a-naming-conventions>`__).

-  If there is more than one feature class in the FGDB, then all feature
   classes should represent a consistent theme. For example, Hydrography
   theme made of different feature classes – such as major rivers,
   secondary rivers, creeks, springs, barrage, and rapids. They should
   be describable by a single metadata records and publishable as a
   single Map Service containing one layer for each of the layers in the
   MXD Map document. If these conditions are not met, then thematic
   grouping should be considered as separate data sets and thus be
   separated in their own FGDB and enter FGP as distinct data sets;

-  If multiple feature classes have the same theme, the same feature
   type, the same attributes, and only differ by geographic extent, for
   example, municipal, province, and NTS decoupage. Attempt to merge
   these feature classes into one single feature class that does not
   contain feature overlaps. During the merging operation, it is not
   necessary to dissolve the entities to remove the intersections at the
   original data sets boundaries as this may lead to issues regarding
   the FGDB Feature Classes content limits, for example, the maximum
   number of vertices for a single feature.

-  The FGDB file follows the defined naming convention (see Appendix A:
   Naming conventions. on page `10 <#appendix-a-naming-conventions>`__).

-  The final FGDB must be zipped in a single file.

Esri Map Documents (.mxd) 
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  There should be one MXD for French and one for English or only one
   bilingual MXD;

-  The MXD must contain each of the Feature Classes contained in the
   FGDB as layers in the map document;

-  Layers must be assigned for each of the feature layers according to
   the contributor’s requirements. The symbology can be:

-  The same for all the features in the layer (Features).

-  Based on the unique value of one or more attributes (Categories).

-  Based on the graduated or proportional normalized value of one
   attribute (Quantities).

-  Based on the value of one or more attributes (Charts).

-  Based on the quantities of one or more attributes (Multiple
   Attributes).

-  Layers can have a scale dependency defined to avoid drawing all
   features at all the viewing scales.

-  Layers can have labelling activated to display feature names or an
   important feature characteristic. Label classes can be defined and
   associated to scale dependencies to avoid drawing the labels at all
   scales.

-  The Map documents may contain “Group Layers”.

-  The Map documents must contain only layers to publish in the Map
   service (must not contain a base map).

-  The Map documents should be saved with the full spatial extent;

-  The Map documents name should be the same as the Service name and the
   FGDB name (see section).

-  The Coordinate system should be defined in the Data Frame Properties
   tab and must be the same as the data (see Coordinate System section).

-  The following fields must be activated in the Layer fields tab:

-  SHAPE

-  OBJECTID

-  The fields used for the symbolisation

-  All the desired fields in the Map Service

-  Refer to Figure 2, below. In the **Layer Properties** click on the
   **Display** tab. In the **Display Expression** area, set the
   **Field:** to **Provider**. The FGP viewer uses this field to display
   automatically a value when the cursor passes over a feature.

.. image:: vertopal_40208e89b751415fb056b7bec6b8446b/media/image3.png
   :width: 3.59449in
   :height: 2.79134in

Figure 2: Setting Display Expression

Symbology
^^^^^^^^^

Complex symbology should be avoided (multilevel symbols, hatched or
other pattern in surfaces) because they can slow down the service
response time. This is even more important if the service has a large
number of features and vertices or more than one layer. Follow these
recommendations:

-  Avoid complex symbology.

-  Use simple lines.

-  Use simple surface (no pattern).

-  Point symbology can be more complex with limited effect on the
   response time.

-  If possible, remove as much vertices as possible.

-  If possible, merge features to reduce number of feature in the
   service.

Label
^^^^^

Currently, the FGP viewer cannot display labels from ESRI Map Service.

Package Control file
~~~~~~~~~~~~~~~~~~~~

-  The configuration file contains all the relevant information about
   the package content. The following information is essential in order
   to provide the necessary minimum input to the DDR system to work
   properly.

-  For the first version of the DDR, an Excel file will be used to
   gather all the information needed. The FGP Contributor Support Team
   can provide an Excel.

-  The DDRConfigFile is divided in 1/3 main sections – General

-  Publisher information (username and email)

-  Metadata File Identifier

-  This field makes the link with the FGP Catalogue. To find this ID,
   select the targeted geospatial record in the FGP Catalogue and scroll
   down to the **File Identifier** in the **Additional Information**
   section.

-  ArcGIS Server ID (optional)

-  This information is not necessary if you want to use the default
   ArcGIS Server ID that is set to your department in the DDR Registry.
   If you want to use another ArcGIS Server licence, register it in the
   registry (see the DDR AdminGuide) and enter the ID here.

-  Download repository ID (FTP Site) (Optional)

-  This information is not necessary if you want to use the default
   Download repository ID that is set to your department in the DDR
   Registry. If you want to use another Download repository ID, register
   it in the registry (see the DDR AdminGuide) and enter the ID here.

-  Core Subject term

-  Choose a subject term in the downloadable version (.csv) available on
   the Government of Canada Core Subject Thesaurus
   (http://www.thesaurus.gc.ca/default.asp?lang=En&n=EAEAD1E6-1).

-  The DDRConfigFile is divided in 2/3 main sections – Map Service

-  This section gives details to help realize the Web Map Service
   Publication. If no service publication is requested, this section
   must be left empty.

-  In the Map Service Information subsection (upper subsection), Service
   1 and 2 columns refer to a possible French and English publication.
   Both columns must be filled if two FGDB are provided, one French and
   one English.

-  Fill the Service 1 column only if a bilingual FGDB is provided.

-  Service Name

-  The service will not be published if Service Name is not filled, see
   Map Service Naming Standard section.

-  Map Document Filename (.mxd)

-  Name of the MXD file, see MXD File Naming Standard section.

-  Dataset Filename (FGDB)

-  Name of the FGDB file (see section)

-  FGDB files must also be zipped in a single file.

-  Service Folder Name

-  This gives the sub folder of ArcGIS Server where the service will be
   deployed. The TBS acronym (upper cases) of your department in English
   is a good choice!

-  Services Capabilities

-  This section includes service parameters for Web service
   customisation.

-  In the Map Service Metadata subsection (lower subsection),

-  Each metadata field description must be given in French and in
   English in order to have bilingual metadata.

-  The Table 1, below gives a brief description of each metadata field.

.. table:: Table 3: Feature Class Naming Standard

   +-------+--------------+----------+-----------------+----------------+
   | Met   | Description  | Appli    | Example         | HNAP Metadata  |
   | adata |              | cability |                 | reference      |
   +=======+==============+==========+=================+================+
   | Su    | A short      | M        | Canadian        | None           |
   | mmary | summary of   | andatory | airports served |                |
   |       | the service. |          | by NAV CANADA   |                |
   |       |              |          | control towers  |                |
   |       |              |          | or flight       |                |
   |       |              |          | service         |                |
   |       |              |          | station.        |                |
   +-------+--------------+----------+-----------------+----------------+
   | D     | A detailed   | M        | This field      | Data           |
   | escri | description  | andatory | could be a      | Identification |
   | ption | of the       |          | complete copy   | (MD_DataI      |
   |       | service.     |          | (or a shorter   | dentification) |
   |       |              |          | version) of the | 5.3.1.2        |
   |       |              |          | “Description”   |                |
   |       |              |          | already         |                |
   |       |              |          | included in the |                |
   |       |              |          | FGP Catalogue   |                |
   +-------+--------------+----------+-----------------+----------------+
   | Tags  | Keywords or  | M        | Airports, Air   | Keywords       |
   |       | terms that   | andatory | transport,      | (MD_Keywords)  |
   |       | describe the |          | Geographic      | 5.3.6.1        |
   |       | service,     |          | data, Aviation, |                |
   |       | separated by |          | Canada, Air     |                |
   |       | commas.      |          | Navigation      |                |
   |       | Keywords are |          |                 |                |
   |       | a useful way |          |                 |                |
   |       | to quickly   |          |                 |                |
   |       | and easily   |          |                 |                |
   |       | identify and |          |                 |                |
   |       | find         |          |                 |                |
   |       | specific     |          |                 |                |
   |       | content with |          |                 |                |
   |       | ArcGIS       |          |                 |                |
   |       | Online or    |          |                 |                |
   |       | other        |          |                 |                |
   |       | applications |          |                 |                |
   |       | developed to |          |                 |                |
   |       | use these    |          |                 |                |
   |       | keywords.    |          |                 |                |
   +-------+--------------+----------+-----------------+----------------+
   | A     | Text         | M        | http://open     | Legal          |
   | ccess | describing   | andatory | .canada.ca/en/o | Constraints    |
   | and   | the          |          | pen-government- | (MD_Leg        |
   | Use   | restrictions |          | licence-canada. | alConstraints) |
   | c     | and legal    |          |                 | acc            |
   | onstr | p            |          |                 | essConstraints |
   | aints | rerequisites |          |                 | 5.4.2.2,       |
   |       | for          |          |                 | useConstraints |
   |       | accessing    |          |                 | 5.4.2.3        |
   |       | and using    |          |                 |                |
   |       | the service. |          |                 |                |
   +-------+--------------+----------+-----------------+----------------+
   | Cr    | Organization | M        | Government of   | None           |
   | edits | that has     | andatory | Canada; Natural |                |
   |       | produced the |          | Resources       |                |
   |       | data set,    |          | Canada; Earth   |                |
   |       | plus other   |          | Sciences        |                |
   |       | o            |          | Sector; Canada  |                |
   |       | rganizations |          | Centre for      |                |
   |       | as           |          | Mapping and     |                |
   |       | necessary.   |          | Earth           |                |
   |       | This         |          | Observation :   |                |
   |       | information  |          |                 |                |
   |       | is displayed |          |                 |                |
   |       | in web       |          |                 |                |
   |       | applications |          |                 |                |
   |       | as           |          |                 |                |
   |       | attribution  |          |                 |                |
   |       | on the       |          |                 |                |
   |       | bottom part  |          |                 |                |
   |       | of the map.  |          |                 |                |
   +-------+--------------+----------+-----------------+----------------+

-  The DDRConfigFile is divided in 3/3 main sections – Download Package

-  This section refers to the files that will be downloadable from the
   DDR FTP site.

-  If no download package publication is requested, this section must be
   left empty.

-  The package name parameter must be filled. This will be the folder
   name on the ftp site.

-  For each file you must give the:

-  File name. (FGDB and shapefile must be zipped. File name must include
   the .zip extension)

-  FTP Subfolder (optional)

A set of Ancillary files (for download)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Download Package should contain:

-  **Data Set** in the selected format:

-  Data Set formats offered as part of the Download Packages should
   include an Open Data format or a proprietary format if the adoption
   of the proprietary format is widespread. The spatial data formats
   proposed are:

-  Esri File Geodatabase (FGDB);

-  KML;

-  GeoJSON;

-  Shapefile;

-  CSV (comma-separated values) or Text (tab-delimited) – suggested for
   point features only.

-  **Document describing data content**. Include at least on description
   attribute from the following list:

-  List of attributes and description (doc, xls, txt, csv, pdf)

-  Specification (doc, pdf)

-  Catalogue (doc, xls, txt, csv, html, pdf)

-  Data model (doc, xls, html, pdf)

-  Complementary documents (doc, xls, txt, csv, pdf)

Coordinate System
-----------------

FGP contributors are strongly encouraged to make their data available in
one or more of the four projections presented here in order of
preference:

1. NAD83 / Canada Atlas Lambert EPSG:3978 `> <http://epsg.io/3978>`__
   http://epsg.io/3978

5. WGS84 / Pseudo-Mercator EPSG:3857 `> <http://epsg.io/3857>`__
   http://epsg.io/3857

6. NAD83 (CSRS) / Canada Atlas Lambert EPSG:3979
   `> <http://epsg.io/3979>`__ http://epsg.io/3979

7. NAD83 (CSRS) EPSG:4617 `> <http://epsg.io/4617>`__
   http://epsg.io/4617

**Note:** The base maps used by the FGP viewer are in projections 1 and
2 of the list above. Projection 1 is the default projection used in the
FGP viewer. For performance reasons, it is preferable to use the same
projection for the data than the FGP base map in order to avoid
on–the-fly reprojection mechanism.

FGP Naming Conventions
----------------------

Please follow the following naming conventions for your input package.

Generic Naming Standards 
~~~~~~~~~~~~~~~~~~~~~~~~~

-  Begin title with the name or subject of the resource. The most-unique
   content of name or subject should come first.

-  Names must start with a letter.

-  Name strings should include only:

-  Alphanumeric characters (letters and numbers)

-  Use \_ to separate words

-  Name strings must not include:

-  Spaces, periods, dashes, or any other special characters

-  Name should not exceed 70 characters.

-  If abbreviations are used, use standard abbreviations. If letters are
   to be removed to form an ad-hoc abbreviation, removal of vowels first
   is the preferred method. Abbreviations should not obscure the logical
   meaning of the name.

-  Avoid the use of acronyms.

-  Names should not include reference to the organization.

Official Languages
------------------

According to *FGP Web Service Requirements* (link to reference sheet)
web services must be made available in both official languages.
Departments are encouraged to separate web services, one in English and
one in French. Bilingual web services (one service, two languages) are
also supported by the FGP catalogue and visualization application but
separate services for each official language is the most desirable
scenario for usability.

Appendix A: Naming conventions
------------------------------

File Geodatabase (FGDB) Naming Standard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Generic standards apply (see Generic Naming Standards).

-  Name should be lower case.

-  The name should be formed using a concatenation of:

.. table:: Table 4: Field Name Components

   +------------+------------+------------------+-------+---------------+
   | App        | Component  | Description      | D     | Example       |
   | licability |            |                  | omain |               |
   |            |            |                  | Type  |               |
   +============+============+==================+=======+===============+
   | Mandatory  | General    | General subject  | User  | energy_i      |
   |            | Descriptor | descriptor       | spec  | nfrastructure |
   |            |            |                  | ified |               |
   +------------+------------+------------------+-------+---------------+
   | Optional   | Location   | Location covered | User  | Quebec,       |
   |            | Descriptor | by the dataset   | spec  | Ottawa,       |
   |            |            |                  | ified | B             |
   |            |            |                  |       | affin_Island, |
   |            |            |                  |       | etc.          |
   +------------+------------+------------------+-------+---------------+
   | Optional   | Scale/     | Data capture     | Coded | 20k, 50k,     |
   |            | Resolution | scale,           | Value | 250k, 2M,     |
   |            | Descriptor | divided by 1000  |       | etc.          |
   |            |            | (=k), or         |       |               |
   |            |            | 1,000,000 (=M).  |       |               |
   +------------+------------+------------------+-------+---------------+
   | Optional   | Year       | Year, or year    | Coded | 2003          |
   |            |            | range            | Value | 2001_2007     |
   |            |            | of data capture  | or    |               |
   |            |            |                  | range |               |
   +------------+------------+------------------+-------+---------------+
   | Optional   | Coordinate | EPSG code of the | Coded | epsg3978      |
   |            | system     | coordinate       | Value |               |
   |            |            | system           |       | epsg3957      |
   +------------+------------+------------------+-------+---------------+
   | Optional   | Version    | Dataset version, | Coded | v1, v2, v3,   |
   |            |            | if               | Value | etc           |
   |            |            | multiple         |       |               |
   |            |            | versions are     |       |               |
   |            |            | present          |       |               |
   +------------+------------+------------------+-------+---------------+
   | Optional\* | Language   | Data language    | Coded | en, fr        |
   |            |            |                  | Value |               |
   +------------+------------+------------------+-------+---------------+
   | \*When     |            |                  |       |               |
   | both       |            |                  |       |               |
   | official   |            |                  |       |               |
   | languages  |            |                  |       |               |
   | FGDB are   |            |                  |       |               |
   | provided   |            |                  |       |               |
   | in the     |            |                  |       |               |
   | input      |            |                  |       |               |
   | package,   |            |                  |       |               |
   | the FGDB   |            |                  |       |               |
   | names      |            |                  |       |               |
   | should be  |            |                  |       |               |
   | in English |            |                  |       |               |
   | and with   |            |                  |       |               |
   | the        |            |                  |       |               |
   | language   |            |                  |       |               |
   | indicator, |            |                  |       |               |
   | i.e. \_en  |            |                  |       |               |
   | or \_fr.   |            |                  |       |               |
   | This       |            |                  |       |               |
   | reco       |            |                  |       |               |
   | mmendation |            |                  |       |               |
   | makes it   |            |                  |       |               |
   | easier for |            |                  |       |               |
   | FGDB       |            |                  |       |               |
   | man        |            |                  |       |               |
   | ipulation, |            |                  |       |               |
   | storage    |            |                  |       |               |
   | and        |            |                  |       |               |
   | r          |            |                  |       |               |
   | eadability |            |                  |       |               |
   | by         |            |                  |       |               |
   | bilingual  |            |                  |       |               |
   | ap         |            |                  |       |               |
   | plications |            |                  |       |               |
   +------------+------------+------------------+-------+---------------+

.\ **Note:** Use optional components only when relevant and useful.

Examples:

-  energy_infrastructure_ontario_250k_2016.gdb

-  watershed_quebec_250k_2015_en.gdb

-  watershed_quebec_250k_2015_fr.gdb

-  community_pasture_50k_2002_2011_en.gdb

-  community_pasture_50k_2002_2011_fr.gdb

Files Geodatabase (FGDB); Feature Class Naming Standard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Generic standards apply (see Generic Naming Standards).

-  Must be limited to 160 characters. However, keep in mind that a 32
   characters limit exists for data published to ArcSDE, and shorter
   names are generally easier to work with.

-  Names should be lower case.

-  Feature Class names should be in the official language of the FGDB.

-  The name should be formed using a concatenation of:

.. table:: Table 5: Field Name Alias

   +------------+-----------------+----------+----------+----------------+
   | Component  | Description     | Applica  | Domain   | Example        |
   |            |                 | bility\* | Type     |                |
   +============+=================+==========+==========+================+
   | Subject    | Feature Class   | M        | User     | censu          |
   | Descriptor | subject         | andatory | s        | s_consilidated |
   |            | descriptor      |          | pecified |                |
   +------------+-----------------+----------+----------+----------------+
   | Type       | A more specific | M        | User     | subdivisions   |
   |            | type            | andatory | s        |                |
   | Descriptor | description.    |          | pecified |                |
   +------------+-----------------+----------+----------+----------------+
   | Scale/     | Data capture    | Optional | Coded    | 20k, 50k,      |
   | Resolution | scale,          |          | Value    | 250k, 2M,      |
   | Descriptor | divided by 1000 |          |          |                |
   |            | (=k),           |          |          |                |
   |            | or 1,000,000    |          |          |                |
   |            | (=M).           |          |          |                |
   +------------+-----------------+----------+----------+----------------+
   | Year       | Year, or year   | Optional | Coded    | 2003           |
   |            | range           |          | Value or | 2001_2007      |
   |            | of data capture |          | range    |                |
   +------------+-----------------+----------+----------+----------------+
   | Feature    | Feature         | Optional | Coded    | *English*      |
   | Type       | geometry        |          | Value    |                |
   |            | type.           |          |          | | polygon,     |
   |            |                 |          |          |   line,        |
   |            |                 |          |          | | point, anno, |
   |            |                 |          |          |   ras          |
   |            |                 |          |          |                |
   |            |                 |          |          | *French*       |
   |            |                 |          |          |                |
   |            |                 |          |          | | polygone,    |
   |            |                 |          |          |   ligne,       |
   |            |                 |          |          | | point, anno, |
   |            |                 |          |          |   ras          |
   +------------+-----------------+----------+----------+----------------+
   | Version    | Dataset         | Op       | Coded    | v1, v2, v3,    |
   |            | version, if     | tional\* | Value    | etc            |
   |            | multiple        |          |          |                |
   |            | versions are    |          |          |                |
   |            | present         |          |          |                |
   +------------+-----------------+----------+----------+----------------+

\* The use of the Version optional component should not be used for the
feature class name if already used for the FGDB name.

Note: Use optional components only when relevant and useful.

Examples:

-  fueltank_location_20k_2006_point_v1

-  inventaire_grands_projets_Canada_v1

-  census_consilidated_division_2012

-  landcover_classification_30M

Files Geodatabase (FGDB); Field Naming Standard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Generic standards apply (see Generic Naming Standards)

-  Field Names should be descriptive of the field content

-  The use of lower case should be preferred

-  The use of only one case type is preferred (only uppercase or only
   lower case)

-  Each field names must be unique

-  The Field name should be in English and the same for all official
   languages FGDB versions (the field names alias should be use for the
   translation in each FGDB (See the section “Files Geodatabase (FGDB);
   Field alias Naming Standard”).

-  Field names should contain standard abbreviations to keep the field
   name as short as possible. Abbreviations should not obscure the
   logical meaning of the field name.

-  Where both official languages are present in the same entity, the
   field name must end with the language indicator, i.e. \_en or \_fr
   (ex. ecozone_name_fr, ecozone_name_en).

-  Keep in mind that if the datasets is converted into shape file, field
   length is limited to 10.

Field naming convention example

The following are example of possible field name components:

-  The field name could be composed of the following components:

.. table:: Table 6: Name Concatenation

   +----------+--------------------------+---------------+----------------+
   | C        | Description              | Applicability | Examples       |
   | omponent |                          |               |                |
   +==========+==========================+===============+================+
   | Prime    | A prime word establishes | Mandatory     | Cover, Use,    |
   | word     | the subject type of the  |               | Geo, Station,  |
   |          | data item being named.   |               | System         |
   +----------+--------------------------+---------------+----------------+
   | Qu       | A qualifying word        | Optional      | Land, Y, Major |
   | alifying | categorizes the data     |               |                |
   | word     | item within its subject  |               |                |
   |          | type.                    |               |                |
   +----------+--------------------------+---------------+----------------+
   | Class    | A class word identifies  | Optional      | Code, Number,  |
   | word     | the nature of the data   | (very         | Name, Coord    |
   |          | item being defined.      | recommended)  |                |
   +----------+--------------------------+---------------+----------------+

-  Prime words are not mandatory as part of a physical name where the
   prime word is the same as the table name.

-  Qualifying words may be omitted if the uniqueness and completeness of
   data is retained.

-  For ease of readability, any meaningful permutation (or ordering) of
   the prime/qualifying/class words is permitted, to remain close to the
   logical name.

-  Abbreviated class words should be used if they exist (e.g. IND, NUM,
   DESC, CMNT)

Examples:

-  land_cover_code

-  land_use_code

-  major_system_name

-  y_geo_coord

-  road_number

-  road_name

-  city_name

-  city_id

-  number_of_lane

Files Geodatabase (FGDB); Field alias Naming Standard 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  The use of blank and special characters is permitted.

-  Both upper and lower cases are permitted.

-  Field Names alias should be descriptive of the field content.

-  Field names alias must start with a letter.

-  All field names alias must be unique.

-  Field names alias must be in the official language of the FGDB.

-  Field names alias should be evocative.

-  Field names alias should not contain abbreviations, if possible.

The following are the details on the field name alias components:

-  Prime words are not mandatory as part of a physical name where the
   prime word is the same as the table name.

-  Qualifying words may be omitted if the uniqueness and completeness of
   data is retained.

-  For ease of readability, any meaningful permutation (or ordering) of
   the prime, qualifying, class, or any words is permitted, to remain
   close to the logical name.

-  Abbreviated class words should be used if they exist (for example,
   IND, NUM, DESC, CMNT).

-  The field name alias should be composed of the following components.
   Table 5 defines the field name aliases.

+---------+---------------------------+------------+------------------+
| Co      | Description               | App        | Examples         |
| mponent |                           | licability |                  |
+=========+===========================+============+==================+
| Prime   | A prime word establishes  | Mandatory  | Cover, Use, Geo, |
| word    | the subject type of the   |            | Station, System  |
|         | data item being named.    |            |                  |
+---------+---------------------------+------------+------------------+
| Qua     | A qualifying word         | Optional   | Land, Y, Major   |
| lifying | categorizes the data item |            |                  |
| word    | within its subject type.  |            |                  |
+---------+---------------------------+------------+------------------+
| Class   | A class word identifies   | Mandatory  | Code, Number,    |
| word    | the nature of the data    |            | Name, Coord, Id, |
|         | item being defined.       |            | Descriptor,      |
|         |                           |            | Priority         |
+---------+---------------------------+------------+------------------+

Examples:

-  Geographic Coordinates Y (latitude)

-  City Identifier

-  Identifiant de la ville

-  Number of lane

-  Nombre de voie

MXD File Naming Standard 
~~~~~~~~~~~~~~~~~~~~~~~~~

-  The MXD File naming convention follow the same rules describe for the
   FGDB naming convention (see File Geodatabase (FGDB) Naming Standard
   section).

Map Service Naming Standard 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Should be the same as the FGDB and the MXD names used to generate the
   Map Service (See File Geodatabase (FGDB) Naming Standard section).
   Only one FGDB per Map Service is permitted.

Map Service; Layers Naming Standard (in the mxd)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, ArcMap use the Feature Class name to set the layer name. The
user can modify the layer name in the table of content of the mxd.

-  The use of blank and special characters is permitted.

-  Both upper case and lower case are permitted.

-  For English services, title capitalization rules must be applied:

-  Always capitalize the first and the last word.

-  Capitalize all nouns, pronouns, adjectives, verbs, adverbs, and
   subordinate conjunctions ("as", "because", "although").

-  Lowercase all articles, coordinate conjunctions ("and", "or", "nor"),
   and prepositions regardless of length, when they are other than the
   first or last word. (Note: NIVA prefers to capitalize prepositions of
   five characters or more ("after", "among", "between").)

-  Lowercase the "to" in an infinitive.

-  All layer names must be unique.

-  Layer names must be in the official language of the service.

-  Layer names should be evocative.

-  Layer names should not contain abbreviations, if possible.

-  The name should be formed using a concatenation as described in Table
   6.

+------------+---------------------+---------+----------+-------------+
| Component  | Description         | Applic  | Domain   | Example     |
|            |                     | ability | Type     |             |
+============+=====================+=========+==========+=============+
| Subject    | Layer subject       | Ma      | User     | Fuel Tank   |
| Descriptor | descriptor          | ndatory | s        | L           |
|            |                     |         | pecified | ocalisation |
+------------+---------------------+---------+----------+-------------+
| Spatial    | Layer spatial       | O       | User     | Canada      |
| Extend     | extend              | ptional | s        |             |
|            |                     |         | pecified | Québec      |
|            |                     |         |          |             |
|            |                     |         |          | Québec      |
|            |                     |         |          |             |
|            |                     |         |          | Alberta     |
|            |                     |         |          |             |
|            |                     |         |          | etc.        |
+------------+---------------------+---------+----------+-------------+
| Scale/     | Layer display       | O       | Coded    | | 20k, 50k, |
| Resolution | scale,              | ptional | Value or | | 250k, 2m, |
| Descriptor | divided by 1000     |         | range    |             |
|            | (=k), or 1,000,000  |         |          | 1k-2m,      |
|            | (=m)                |         | min      |             |
|            |                     |         | value=   | 2m-30m      |
|            |                     |         | 1k max   |             |
|            |                     |         | va       |             |
|            |                     |         | lue=100m |             |
+------------+---------------------+---------+----------+-------------+
| Year       | Year, or year range | O       | Coded    | | 2003,     |
|            | of data capture or  | ptional | Value or | | 2001 to   |
|            | prediction          |         | range    |   2007,     |
|            |                     |         |          |             |
|            |                     |         |          | 2001 à 2007 |
+------------+---------------------+---------+----------+-------------+
| Feature    | Feature geometry    | O       | Coded    | *English*   |
| Type       | type.               | ptional | Value    |             |
|            |                     |         |          | | polygon,  |
|            |                     |         |          |   line,     |
|            |                     |         |          | | point,    |
|            |                     |         |          |             |
|            |                     |         |          | annotation, |
|            |                     |         |          |   raster    |
|            |                     |         |          |             |
|            |                     |         |          | *French*    |
|            |                     |         |          |             |
|            |                     |         |          | | polygone, |
|            |                     |         |          |   ligne,    |
|            |                     |         |          | | point,    |
|            |                     |         |          |             |
|            |                     |         |          | annotation, |
|            |                     |         |          |   matriciel |
+------------+---------------------+---------+----------+-------------+
| Version    | Dataset version, if | O       | Coded    | v1, v2, v3, |
|            | multiple versions   | ptional | Value    | etc.        |
|            | are present         |         |          |             |
+------------+---------------------+---------+----------+-------------+
| **Note:**  |                     |         |          |             |
| Use        |                     |         |          |             |
| optional   |                     |         |          |             |
| components |                     |         |          |             |
| only when  |                     |         |          |             |
| relevant   |                     |         |          |             |
| and        |                     |         |          |             |
| useful.    |                     |         |          |             |
+------------+---------------------+---------+----------+-------------+

All the optional name components must be in a unique pair of brackets
where each component is separated by a comma.

Examples:

-  Fuel Tanks [Canada, 20k-2m, 2006, line, v1]

-  Réservoirs d’essence [Canada, 20k-2m, 2006, ligne, v1]

-  Inventaire des grands projets [Canada, 2015]

-  Inventaire des grands projets [Canada, 2015]

-  Land Cover, Classification [30m]

-  Couverture du sol, classification [30m]

-  Indice de bien-être des collectivités (IBC) [Québec, 1k-1m, 2012,
   polygone]

-  Community Well-Being (CWB) Index [Quebec, 1k-1m, 2012, polygon]

-  Airports

-  Aéroports

Map Service; Field Naming Standard (in the mxd)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Should be the same as the corresponding FGDB Field alias (see Files
   Geodatabase (FGDB); Field alias Naming Standard section).
