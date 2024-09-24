=================================
OutbreakIndividualMalariaVarGenes
=================================

The **OutbreakIndividualMalariaVarGenes** intervention class is an individual-level intervention
that enables infecting people with an exact set of antigens. This can be helpful when
experimenting with the immune model, such as testing how a person’s immune system
reacts if they are reinfected by the same parasite. To use this intervention, set the
configuration parameters **Malaria_Model** to MALARIA_MECHINISTIC_MODEL and **Malaria_Strain_Model**
to FALCIPARUM_FIXED_STRAIN.

.. include:: ../reuse/warning-case.txt

.. include:: ../reuse/campaign-example-intro.txt

.. csv-table::
    :header: Parameter, Data type, Minimum, Maximum, Default, Description, Example
    :widths: 10, 5, 5, 5, 5, 20, 5
    :file: ../csv/campaign-outbreakindividualmalariavargenes.csv

.. literalinclude:: ../json/campaign-outbreakindividualmalariavargenes.json
   :language: json
