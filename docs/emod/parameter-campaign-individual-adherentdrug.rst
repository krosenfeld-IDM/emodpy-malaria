============
AdherentDrug
============

The **AdherentDrug** class is an individual-level intervention that extends
:doc:`parameter-campaign-individual-antimalarialdrug` class and allows for incorporating different
patterns of adherence for taking packs of anti-malarial drugs. Non-adherence means that the drugs
will not be taken on the prescribed schedule; this will lengthen the time taken to clear parasites
from the person's system, and can lengthen the duration that a feeding mosquito may become infected.


.. include:: ../reuse/warning-case.txt

.. include:: ../reuse/campaign-example-intro.txt

.. csv-table::
    :header: Parameter, Data type, Minimum, Maximum, Default, Description, Example
    :widths: 10, 5, 5, 5, 5, 20, 5
    :file: ../csv/campaign-adherentdrug.csv

.. literalinclude:: ../json/campaign-adherentdrug.json
   :language: json

