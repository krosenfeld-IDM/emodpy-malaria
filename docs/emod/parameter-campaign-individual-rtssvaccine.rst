===========
RTSSVaccine
===========

The **RTSSVaccine** intervention class protects individuals against infection acquisition by
directly boosting the :term:`circumsporozoite protein (CSP)` antibody concentration. This contrasts
with the :doc:`parameter-campaign-individual-simplevaccine` intervention, which is used to modify
the probability of acquisition or transmission.

The CSP antibody reduces the probability that sporozoites survive to infect the liver/hepatocytes. A
higher **Boosted_Antibody_Concentration** means the person will be less likely to have sporozoites
survive and infect the hepatocytes. Without the vaccine, CSP does not do anything. The following
:doc:`parameter-configuration-immunity` parameters impact CSP and its sporozoite killing ability:

*  **Antibody_CSP_Killing_Threshold**
*  **Antibody_CSP_Killing_Inverse_Width**
*  **Antibody_CSP_Decay_Days**

.. include:: ../reuse/warning-case.txt

.. include:: ../reuse/campaign-example-intro.txt

.. csv-table::
    :header: Parameter, Data type, Minimum, Maximum, Default, Description, Example
    :widths: 10, 5, 5, 5, 5, 20, 5
    :file: ../csv/campaign-rtssvaccine.csv

.. literalinclude:: ../json/campaign-rtssvaccine.json
   :language: json