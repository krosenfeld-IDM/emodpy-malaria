from COMPS.Data import QueryCriteria

from idmtools.core import ItemType
from idmtools_platform_comps.comps_platform import COMPSPlatform
from idmtools_platform_container.container_platform import ContainerPlatform


def _get_serialized_filenames(num_cores, timesteps):
    if num_cores == 1:
        serialized_list = [f"state-{str(timesteps).zfill(5)}.dtk"]
    else:
        serialized_list = [f"state-{str(timesteps).zfill(5)}-{str(core_count).zfill(3)}.dtk"
                           for core_count in range(num_cores)]
    return serialized_list


def _get_core_counts(sim_id, platform):
    num_cores = 1
    if isinstance(platform, COMPSPlatform):
        sim = platform.get_item(sim_id, ItemType.SIMULATION, raw=True)
        sim.refresh(QueryCriteria().select_children('hpc_jobs'))
        num_cores = int(sim.hpc_jobs[-1].configuration.max_cores)
    elif isinstance(platform, ContainerPlatform):
        num_cores = 1
    return num_cores


def build_burnin_df(exp_id: str, platform, serialize_days):
    """
    return dataframe which contains outpath, serialized_population_filenames
    Args:
        exp_id:
        platform:

    Returns:
        dataframe:
        Run_Number | Serialization_Time_Steps | task_type | sweep_tag | simid | outpath|Num_Cores|Serialized_Population_Filenames
    Note, Serialized_Population_Filenames depends on n_cores. if n_cores = 2, Serialized_Population_Filenames look
    like these: state-00050-000.dtk, state-00050-001.dtk
    """

    df = platform.create_sim_directory_df(exp_id)
    # add Num_Cores to df
    df["Num_Cores"] = df["simid"].apply(_get_core_counts, platform=platform)

    try:
        burnin_length_in_days = serialize_days
    except AttributeError:
        # different versions of pandas save this as either a string or a list
        burnin_length_in_days = df["Serialization_Time_Steps"].iloc[0][-1]

    df["Serialized_Population_Filenames"] = df["Num_Cores"].apply(_get_serialized_filenames, timesteps=burnin_length_in_days)
    df = df.reset_index(drop=True)
    return df
