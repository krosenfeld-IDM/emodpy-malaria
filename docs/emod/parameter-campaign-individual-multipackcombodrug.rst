==================
MultiPackComboDrug
==================

The **MultiPackComboDrug** intervention class is an individual-level intervention that explicitly
models which doses of anti-malarial pills are taken when. This intervention is similar to the
:doc:`parameter-campaign-individual-adherentdrug` class, but allows modeling pill packs that involve
multiple drugs with different dosing per drug.


.. include:: ../reuse/warning-case.txt

.. include:: ../reuse/campaign-example-intro.txt

.. csv-table::
    :header: Parameter, Data type, Minimum, Maximum, Default, Description, Example
    :widths: 10, 5, 5, 5, 5, 20, 5
    :file: ../csv/campaign-multipackcombodrug.csv

.. literalinclude:: ../json/campaign-multipackcombodrug.json
   :language: json


The **Doses** array allows the user to specify what drugs are taken in what dose.  **The Dose_Interval**
parameter is used to determine the number of days between these doses.  A dose can be specified to
have zero drugs.  For example, if we wanted to model a 7-day pill pack that involved two drugs where
the person gets two doses of DrugA on Day 0 and then one every other day for 7-days and DrugB was to
be taken every day for 4-days, we would configure it like the following:

.. code-block:: json

    {
        "Dose_Interval": 1,
        "Doses": [
            [ "DrugA", "DrugA", "DrugB" ],
            [                   "DrugB" ],
            [ "DrugA",          "DrugB" ],
            [                   "DrugB" ],
            [ "DrugA"                   ],
            [                           ],
            [ "DrugA"                   ]
        ]
    }


However, if DrugB was instead to be taken twice--once on Day 0 and once on Day 4, it would be configured
like the following:

.. code-block:: json

    {
        "Dose_Interval": 2,
        "Doses": [
            [ "DrugA", "DrugA", "DrugB" ],
            [ "DrugA"                   ],
            [ "DrugA",          "DrugB" ],
            [ "DrugA"                   ]
        ]
    }


