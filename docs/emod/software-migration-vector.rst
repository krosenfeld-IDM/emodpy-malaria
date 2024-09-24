======================
Vector migration files
======================

Vector migration files describe the rate of migration of vectors *out* of a geographic :term:`node`
analogously to human migration (see :doc:`software-migration` for more information), although vector
migration does not support gender and age parameters.  Vector migration is one way, such that each
trip made by a vector is independent of previous trips made by the vector. The rates in the file
are used to control whether or not a vector will migrate: the rate specified is used to get a "time
to leave on trip" value from an exponential distribution. If the value is less than one day, then the
vector will migrate.

In order to use a vector migration file, the configuration parameter **Vector_Sampling_Type** must
be set to either TRACK_ALL or SAMPLE_IND_VECTORS. If default geography is used (the configuration
parameter **Enable_Demographics_Builtin** is set to 1, and **Default_Geography_Initial_Node_Population**
and **Default_Geography_Torus_Size** are configured), vectors can only migrate (or not) using
**Enable_Vector_Migration**, and vector migration files are not used.

Vectors can migrate regionally or locally, and there are multiple modifiers available to influence
migration to particular nodes over others. See :doc:`parameter-configuration` for more information
on the parameters governing vector migration.


JSON metadata file
==================

The metadata file is a JSON-formatted file that includes a metadata section and a node offsets
section. The **Metadata** section contains a JSON object with parameters, some of which are
strictly  informational and some of which are used by |exe_s|. However, the informational ones may
still be important to understand the provenance and meaning of the data.

Parameters
----------

The following parameters can be included in the vector migration metadata file:

.. csv-table::
    :header: Parameter, Data type, Description
    :widths: 10,5,20

    Author, string, The author of the file.
    DatavalueCount, integer, "(Used by |EMOD_s|.) The number of outbound data values per node (max 100). The number must be the same across every node in the binary file."
    DateCreated, string, The day the file was created.
    IdReference, string, "(Used by |EMOD_s|.) A unique, user-selected string that indicates the method used by |EMOD_s| for generating **NodeID** values in the input files. For more information, see :doc:`software-inputs`."
    NodeCount, integer, (Used by |EMOD_s|.) The number of nodes to expect in this file.
    NodeOffsets, string, "(Used by |EMOD_s|.) A string that is **NodeCount** :math:`\times` 16 characters long. For each node, the first 8 characters are the origin **NodeID** in hexadecimal. The second 8 characters are the byte offset in hex to the location in the binary file where the destination **NodeIDs** and migration rates appear."
    Tool, string, The script used to create the file.


Example
-------

.. literalinclude:: ../json/vector-migration-metadata.json
   :language: json


.. see https://wiki.idmod.org/pages/viewpage.action?pageId=46367722 for info