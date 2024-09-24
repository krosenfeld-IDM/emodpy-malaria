=====================
ReportVectorMigration
=====================

The vector migration report (ReportVectorMigration.csv) provides detailed information on when and
where vectors are migrating. As there will be one line for each migrating vector, it is beneficial
to use the parameters **Start_Day** and **End_Day** to limit the size of the output file. Note that
only female vectors migrate.

See :doc:`software-migration-vector` for more information on how to create vector migration files.


Configuration
=============

To generate the report, configure the following parameters in the custom_reports.json file:

.. csv-table::
    :header: Parameter, Data type, Min, Max, Default, Description
    :widths: 8, 5, 5, 5, 5, 20

    **End_Day**, float, 0, 3.40E+38, 3.40E+38, "The day to stop collecting data for the report."
    **Start_Day**, float, 0, 3.40E+38, 0, The day to start collecting data for the report.


.. code-block:: json

    {
        "Reports": [
            {
                "Start_Day": 372,
                "End_Day": 912,
                "class": "ReportVectorMigration"
            }
        ],
        "Use_Defaults": 1
    }




Report structure and data channel descriptions
==============================================

The file contains the following data channels:

.. csv-table::
    :header: Data channel, Data type, Description
    :widths: 10, 10, 20

    Time, integer, The day that the vector migrated.
    ID, integer, "The ID of the vector or cohort.  Note that when using the cohort model, a cohort may need to split such that some of the cohort migrates to the node and some do not, creating new cohort IDs. This may make it difficult to follow cohorts by ID."
    FromNodeID, integer, The ID of the node that the vector was migrating from.
    ToNodeID, integer, The ID of the node that the vector traveled to.
    MigrationType, string, "The method of migration used by the vector: local or regional."
    Species, string, The name of the species of vector.
    Age, integer, The number of days the vector has been alive.
    Population, integer, "The number of vectors that are migrating. If **Vector_Sampling_Type** is set to TRACK_ALL_VECTORS or SAMPLE_INDIVIDUAL_VECTORS this will be set to 1. If it is set to VECTOR_COMPARTMENTS_NUMBER or VECTOR_COMPARTMENTS_PERCENT then the number will be greater than one, and indicates that 'X' number of vectors are involved in that line of the report, with 'X' vectors of that age moving from node to node."


Example
=======

The following is an example of ReportVectorMigration.csv:

.. csv-table::
    :header: Time, ID, FromNodeID, ToNodeID, Migration type, Species, Age, Population
    :widths: 10, 10, 10, 10, 10, 10, 10, 10

    365, 7203794, 25, 24, local, Arabiensis, 0, 3
    365, 7203820, 25, 20, local, Arabiensis, 0, 7
    365, 7203846, 25, 19, local, Arabiensis, 0, 6
    365, 7203872, 25, 24, local, Arabiensis, 1, 7
    365, 7203898, 25, 20, local, Arabiensis, 1, 4
    365, 7203924, 25, 19, local, Arabiensis, 1, 8
    365, 7203950, 25, 24, local, Arabiensis, 2, 3
    365, 7203976, 25, 20, local, Arabiensis, 2, 7