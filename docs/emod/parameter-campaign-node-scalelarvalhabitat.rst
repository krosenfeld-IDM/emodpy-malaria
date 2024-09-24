==================
ScaleLarvalHabitat
==================

The **ScaleLarvalHabitat** intervention class is a node-level intervention that enables
species-specific habitat modification within shared habitat types. This intervention has a similar
function to the demographic parameter **ScaleLarvalMultiplier**, but enables habitat availability to
be modified at any time or at any location during the simulation, as specified in the campaign
event.

To reset the multiplier, you must either replace the existing one with a new intervention where the
multiplier/factor is 1.0 or use the **Disqualifying_Properties** to cause the intervention to abort.

.. include:: ../reuse/warning-case.txt

.. include:: ../reuse/campaign-example-intro.txt

.. csv-table::
    :header: Parameter, Data type, Minimum, Maximum, Default, Description, Example
    :widths: 10, 5, 5, 5, 5, 20, 5
    :file: ../csv/campaign-scalelarvalhabitat.csv

.. literalinclude:: ../json/campaign-scalelarvalhabitat.json
   :language: json
