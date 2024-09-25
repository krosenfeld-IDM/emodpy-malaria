import os
from typing import List, Dict


from COMPS import AuthManager
from COMPS.Data import Simulation, QueryCriteria
from idmtools.core import ItemType
from idmtools.entities.iplatform import IPlatform
from idmtools_platform_comps.comps_platform import COMPSPlatform
from idmtools_platform_slurm.slurm_platform import SlurmPlatform


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
    elif isinstance(platform, SlurmPlatform):
        # TODO: Implement this with slurm platform
        num_cores = 1
    return num_cores

def get_workdir_from_simulations(platform: 'IPlatform', comps_simulations: List[Simulation]) -> Dict[str, str]:
    """
    Get COMPS filepath
    Args:
        platform: idmtools Platform
        comps_simulations: COMPS Simulations

    Returns: dictionary with simid as key and filepath as value

    """

    if platform.environment.upper() == "SLURMSTAGE" or platform.environment.upper() == "CALCULON":
        mounts = AuthManager.get_environment_macros(platform.environment)['DOCKER_MOUNTS']
        mounts = {v[0]: v[1:4] for v in [m.split(';') for m in mounts.split('|')]}
        # pretend I'm on Linux and set the Linux mapping environment variables
        for k, v in mounts.items():
            os.environ[k] = ';'.join([v[0], v[2]])
    sim_work_dir = {str(sim.id): sim.hpc_jobs[-1].working_directory for sim in comps_simulations if sim.hpc_jobs}

    return sim_work_dir

def build_burnin_df(exp_id: str, platform):
    """
    return dataframe which contains serialized_file_path, serialized_population_filenames
    Args:
        exp_id:
        platform:

    Returns:
        dataframe:
        Run_Number | Serialization_Time_Steps | task_type | sweep_tag | simid | serialized_file_path|Num_Cores|Serialized_Population_Filenames
    Note, Serialized_Population_Filenames depends on n_cores. if n_cores = 2, Serialized_Population_Filenames look
    like these: state-00050-000.dtk, state-00050-001.dtk
    """

    df = platform.create_sim_directory_map(exp_id)
    # add Num_Cores to df
    df["Num_Cores"] = df["simid"].apply(_get_core_counts, platform=platform)

    try:
        burnin_length_in_days = int(df["Serialization_Time_Steps"].iloc[0].strip('[]'))
    except AttributeError:
        # different versions of pandas save this as either a string or a list
        burnin_length_in_days = df["Serialization_Time_Steps"].iloc[0][-1]

    df["Serialized_Population_Filenames"] = df["Num_Cores"].apply(_get_serialized_filenames, timesteps=burnin_length_in_days)
    df = df.reset_index(drop=True)
    return df
