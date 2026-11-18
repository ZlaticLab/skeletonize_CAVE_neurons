"""
Please run pip install for any packages that you may be missing. See the imports below.

Dev: Samia Mohinta
Affiliation: University of Cambridge, UK
"""
import os
import sys
import navis
import trimesh
import pandas as pd
from tqdm import tqdm
import pickle
import numpy as np
import pymaid as pm
from cloudvolume import CloudVolume
import scipy.stats as stats
import matplotlib.pyplot as plt
from collections import defaultdict

username = "x"
token = "z"
auth_pass = "y"
url = "https://neurophyla.mrc-lmb.cam.ac.uk/catmaid/fibsem/"
skeleton_path = "./skeletons"
project_id = 48 # pass your own project id. This is extremely imp. If you are not sure what that is reach out to Samia Mohinta/Albert Cardona.

rm = pm.CatmaidInstance(server=url, api_token=token, http_user=username, project_id=project_id, http_password=auth_pass,
                        caching=False)


# segment ids you have skeletonized. Replace the below
ids_of_interest = [720575940405104379, 720575940405307349, 720575940405552659, 720575940405594319, 720575940405795172,
                   720575940405803046, 720575940406483996, 720575940406488460, 720575940406683436, 720575940406807915,
                   720575940406808427, 720575940407022582, 720575940407425991, 720575940407694958, 720575940408389592,
                   720575940408775396, 720575940408912632, 720575940410237440, 720575940410621695,
                   720575940415400896, 720575940415570975, 720575940407157162]

for id_of_interest in tqdm(ids_of_interest):
    neuron_of_interest = np.load(f"{skeleton_path}/{id_of_interest}.npy", allow_pickle=True).item()
    neuron_of_interest.nodes.radius = 0
    neuron_of_interest.nodes.z = neuron_of_interest.nodes.z  # + 63800 # this value may need to be re-calculated and need if your CATMAID instance has an offset. Do not add it otherwise. Again check with SM/AC when unsure.
    _ = pm.upload_neuron(neuron_of_interest, source_type=None, force_id=True, remote_instance=rm)
    cur_skid = pm.get_skids_by_name(id_of_interest, remote_instance=rm).skeleton_id.values[0]
    pm.add_annotations([cur_skid], [id_of_interest], remote_instance=rm)
    pm.add_meta_annotations([str(id_of_interest)], ['vnc_ids'], remote_instance=rm) # change "vnc_ids" to an annotation tag of your choice.
