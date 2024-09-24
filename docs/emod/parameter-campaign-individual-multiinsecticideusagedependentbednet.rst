====================================
MultiInsecticideUsageDependentBednet
====================================

The **MultiInsecticideUsageDependentBednet** intervention class is an individual-level intervention
that is similar to the :doc:`parameter-campaign-individual-usagedependentbednet`
class but allows the addition of multiple insecticides.

The effectiveness of the intervention is combined using the following equation:

Total efficacy = 1.0 – (1.0 – efficacy_1) * (1.0 – efficacy_2) * … * (1.0 – efficacy_n)


.. include:: ../reuse/warning-case.txt

.. include:: ../reuse/campaign-example-intro.txt

.. csv-table::
    :header: Parameter, Data type, Minimum, Maximum, Default, Description, Example
    :widths: 10, 5, 5, 5, 5, 20, 5
    :file: ../csv/campaign-multiinsecticideusagedependentbednet.csv

.. literalinclude:: ../json/campaign-multiinsecticideusagedependentbednet.json
   :language: json