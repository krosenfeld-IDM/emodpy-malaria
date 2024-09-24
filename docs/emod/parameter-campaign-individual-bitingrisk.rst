==========
BitingRisk
==========

The **BitingRisk** class allows you to adjust the relative risk that the person is bitten by a
vector. As an intervention, it allows you to target specific groups at specific times during the
simulation.

The relative biting rate can be initially set by setting **Enable_Demographic_Risk** to 1 and then
configuring **IndividualAttributes**, **RiskDistributionFlag**, **RiskDistributionParam1**, and
**RiskDistributionParam2**. This will give each new person their own relative risk.

The relative biting rate can be thought of as having two parts: the relative risk value and the age
dependent value. Age dependence is set using the  **Age_Dependent_Biting_Risk_Type** parameter.
These two values (from age dependence and relative risk) are multiplied to get the resulting rate,
which is then used to control how much contagion is deposited from an infectious individual and the
probability that an infection is acquired.

This intervention expires. To reset it, distribute another **BitingRisk** intervention that sets it
back to the original value. Note that this is a *relative* biting rate. For example, giving everyone
a value of 10 is the same as giving everyone a value of 1. This intervention is used to indicate
some individuals are more likely to be bitten than others.


.. include:: ../reuse/warning-case.txt

.. include:: ../reuse/campaign-example-intro.txt

.. csv-table::
    :header: Parameter, Data type, Minimum, Maximum, Default, Description, Example
    :widths: 10, 5, 5, 5, 5, 20, 5
    :file: ../csv/campaign-bitingrisk.csv

.. literalinclude:: ../json/campaign-bitingrisk.json
   :language: json
