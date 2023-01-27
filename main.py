from code.classes import district
from code.visualisation import visualisation, output
from code.algorithms import random, random_a_star
from code.experiments import experiment1

'''
Voor nu heb ik een paar stappen eruit gecomment aangezien we nog aan het testen zijn
'''

# -------------------------------- Input ----------------------------------
district_number = 3
experiment_runs = 500


# --------------------------- Create district -----------------------------
district = district.District(district_number)


# ----------------------------- Random Route ------------------------------
#random.create_all_routes(district)


# ------------------------------ A* Route ---------------------------------
random_a_star.create_all_routes(district)


# ----------------------- District Visualisation ---------------------------
visualisation.visualise(district)


# ------------------------------ Output ------------------------------------
#output.generate_json(district)


# ----------------------------- Experiment ---------------------------------
#experiment1.experiment(district_number, experiment_runs)
