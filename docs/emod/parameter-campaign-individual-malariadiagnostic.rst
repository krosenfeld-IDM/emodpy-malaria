=================
MalariaDiagnostic
=================


The **MalariaDiagnostic** intervention class is similar to 
:doc:`parameter-campaign-individual-simplediagnostic`, but distributes a test
for malaria. There are several types of configurable diagnostic tests, and the
type selected determines the other parameters used. 

You should note that the results of **MalariaDiagnostic** can be different
than what you see in the reports.  The intervention takes an independent
measurement from the reports.  It has its own parameters that control the
sensitivity and detection threshold.


.. include:: ../reuse/warning-case.txt


.. include:: ../reuse/campaign-example-intro.txt


.. csv-table::
    :header: Parameter, Data type, Minimum, Maximum, Default, Description, Example
    :widths: 10, 5, 5, 5, 5, 20, 5
    :file: ../csv/campaign-malariadiagnostic.csv


.. literalinclude:: ../json/campaign-malariadiagnostic.json
   :language: json
