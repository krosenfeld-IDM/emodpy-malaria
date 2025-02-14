from emod_api import schema_to_class as s2c
from emodpy_malaria.interventions.common import add_campaign_event

iv_name = "MosquitoRelease"


def _mosquito_release(campaign,
                      intervention_name: str = iv_name,
                      released_number: int = None,
                      released_fraction: float = None,
                      released_infectious: float = None,
                      released_species: str = "arabiensis",
                      released_genome: list[list[str]] = None,
                      released_mate_genome: list[list[str]] = None,
                      released_microsporidia: str = ""
                      ):
    """
        Configures node-targeted MosquitoRelease class intervention. The MosquitoRelease intervention class adds
        mosquito release vector control programs to the simulation. Mosquito release is a key vector control mechanism
        that allows the release of sterile males, genetically modified mosquitoes, or even Microsporidia-infected
        mosquitoes.

    Args:
        campaign: A campaign builder that also contains schema_path parameters
        intervention_name: The optional name used to refer to this intervention as a means to differentiate it from
            others that use the same class. It’s possible to have multiple MosquitoRelease interventions
            if they have different Intervention_Name values.
        released_number: The number of vectors to release, sets Released_Type = "FIXED_NUMBER"
        released_fraction: The fraction of the current population of mosquitoes to release.
            The 'population' will depend on the sex and species of the mosquitoes being released, and it will be the
            population count from the previous time step.
            Sets Released_Type = "FRACTION"
        released_infectious: The fraction of vectors released that are to be infectious.
            One can only use this feature when 'Malaria_Model'!='MALARIA_MECHANISTIC_MODEL_WITH_PARASITE_GENETICS'
        released_species: The case-sensitive name of the species of vectors to be released.
        released_genome: This defines the alleles of the genome of the vectors to be released.
            It must define all of the alleles including the gender 'gene'.  '*' is not allowed.
            Default is  [["X", "X"]]. This only works for vectors that have no genes defined.
        released_mate_genome: This defines the alleles of the mate genome of the vectors to be released.
            The Released_Mate_Genome must be male, and Released_Genome must be female. It must define all of the alleles
            including the gender 'gene'. '*' is not allowed. When this parameter is defined, the released female vectors
            will be fully gestated and ready to lay eggs, which will be the product of Released_Genome and
            Released_Mate_Genome.
        released_microsporidia: String indicating the Strain_Name of the microsporidia strain being released.

    Returns:
        Configured MosquitoRelease intervention
    """
    if not released_genome:
        released_genome = [["X", "X"]]
    # setting released_fraction or released_number to 0 is valid
    if ((released_number is not None and released_fraction is not None) or
            (released_number is None and released_fraction is None)):
        raise ValueError("Please define either released_number or released_fraction to determine how to release "
                         "mosquitoes, \n not both.\n")

    if isinstance(released_microsporidia, bool):
        if released_microsporidia:  # to take care of old code
            raise ValueError("ERROR: _mosquito_release's released_microsporidia is now a string, "
                  "which is the Strain_Name for microsporidia strain defined in config.\n")

    intervention = s2c.get_class_with_defaults("MosquitoRelease", campaign.schema_path)
    intervention.Intervention_Name = intervention_name

    if released_number is not None:
        intervention.Released_Number = released_number
    else:
        intervention.Released_Fraction = released_fraction

    intervention.Released_Infectious = released_infectious if released_infectious else 0
    intervention.Released_Species = released_species
    intervention.Released_Genome = released_genome
    if released_mate_genome:
        intervention.Released_Mate_Genome = released_mate_genome
    intervention.Released_Wolbachia = "VECTOR_WOLBACHIA_FREE"
    intervention.Released_Microsporidia_Strain = released_microsporidia
    return intervention


def add_scheduled_mosquito_release(
        campaign,
        start_day: int = 0,
        node_ids: list = None,
        repetitions: int = 1,
        timesteps_between_repetitions: int = 365,
        intervention_name: str = iv_name,
        released_number: int = None,
        released_fraction: float = None,
        released_infectious: float = None,
        released_species: str = "arabiensis",
        released_genome: list[list[str]] = None,
        released_mate_genome: list[list[str]] = None,
        released_microsporidia: any = None):
    """
        Adds a node-targeted MosquitoRelease class intervention to the campaign. The MosquitoRelease intervention class
        adds mosquito release vector control programs to the simulation. Mosquito release is a key vector control
        mechanism that allows the release of sterile males, genetically modified mosquitoes, or even
        Microsporidia-infected mosquitoes.

    Args:
        campaign: A campaign builder that also contains schema_path parameters
        start_day: The day to release the vectors.
        node_ids: List of nodes to which to distribute the intervention. [] or None, indicates all nodes
            will get the intervention
        repetitions: The number of times an intervention is given, used with timesteps_between_repetitions. -1 means
            the intervention repeats forever. Sets **Number_Repetitions**
        timesteps_between_repetitions: The interval, in timesteps, between repetitions. Ignored if repetitions = 1.
            Sets **Timesteps_Between_Repetitions**
        intervention_name: The optional name used to refer to this intervention as a means to differentiate it from
            others that use the same class. It’s possible to have multiple MosquitoRelease interventions
            if they have different Intervention_Name values.
        released_number: The number of vectors to release, sets Released_Type = "FIXED_NUMBER"
        released_fraction: The fraction of the current population of mosquitoes to release.
            The 'population' will depend on the sex and species of the mosquitoes being released, and it will be the
            population count from the previous time step.
            Sets Released_Type = "FRACTION"
        released_infectious: The fraction of vectors released that are to be infectious.
            One can only use this feature when 'Malaria_Model'!='MALARIA_MECHANISTIC_MODEL_WITH_PARASITE_GENETICS'
        released_species: The case-sensitive name of the species of vectors to be released.
        released_genome: This defines the alleles of the genome of the vectors to be released.
            It must define all of the alleles including the gender 'gene'.  '*' is not allowed.
            Default is  [["X", "X"]]. This only works for vectors that have no genes defined.
        released_mate_genome: This defines the alleles of the mate genome of the vectors to be released.
            The Released_Mate_Genome must be male, and Released_Genome must be female. It must define all of the alleles
            including the gender 'gene'. '*' is not allowed. When this parameter is defined, the released female vectors
            will be fully gestated and ready to lay eggs, which will be the product of Released_Genome and
            Released_Mate_Genome.
        released_microsporidia: The Strain_Name from the Microsporidia list defined for this species.
            Each species has its own strains. Empty String means no microsporidia.

    Returns:
        Formatted intervention
    """

    node_intervention = _mosquito_release(campaign=campaign,
                                          intervention_name=intervention_name,
                                          released_number=released_number,
                                          released_fraction=released_fraction,
                                          released_infectious=released_infectious,
                                          released_species=released_species,
                                          released_genome=released_genome,
                                          released_mate_genome=released_mate_genome,
                                          released_microsporidia=released_microsporidia)
    add_campaign_event(campaign=campaign,
                       start_day=start_day,
                       node_ids=node_ids,
                       repetitions=repetitions,
                       timesteps_between_repetitions=timesteps_between_repetitions,
                       node_intervention=node_intervention)


def new_intervention_as_file(campaign, start_day: int = 1, filename: str = "MosquitoRelease.json"):
    """
        Creates a campaign file with a MosquitoRelease intervention
        
    Args:
        campaign: A campaign builder that also contains schema_path parameters
        start_day: The day to release the vectors.
        filename: name of campaign filename to be created

    Returns:
        returns filename
    """
    add_scheduled_mosquito_release(campaign=campaign, start_day=start_day, released_number=1)
    campaign.save(filename)
    return filename
