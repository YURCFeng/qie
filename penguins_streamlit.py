# import streamlit as st
# import pickle
# rf_pickle = open('random_forest_penguin.pickle', 'rb')
# map_pickle = open('output_penguin.pickle', 'rb')
# rfc = pickle.load(rf_pickle)
# unique_penguin_mapping = pickle.load(map_pickle)
# st.write(rfc)
# st.write(unique_penguin_mapping)

import streamlit as st
import pickle

rf_pickle = open("random_forest_penguin.pickle", "rb")
map_pickle = open("output_penguin.pickle", "rb")
rfc = pickle.load(rf_pickle)
unique_penguin_mapping = pickle.load(map_pickle)
rf_pickle.close()
map_pickle.close()
# island = st.selectbox("Penguin Island", options=["Biscoe", "Dream", "Torgerson"])
# sex = st.selectbox("Sex", options=["Female", "Male"])
# bill_length = st.number_input("Bill Length (mm)", min_value=0)
# bill_depth = st.number_input("Bill Depth (mm)", min_value=0)
# flipper_length = st.number_input("Flipper Length (mm)", min_value=0)
# body_mass = st.number_input("Body Mass (g)", min_value=0)
# st.write(
#     "the user inputs are {}".format(
#         [island, sex, bill_length, bill_depth, flipper_length, body_mass]
#     )
# )
island = st.selectbox("Penguin Island", options=["Biscoe", "Dream", "Torgerson"])
sex = st.selectbox("Sex", options=["Female", "Male"])
bill_length = st.number_input("Bill Length (mm)", min_value=0)
bill_depth = st.number_input("Bill Depth (mm)", min_value=0)
flipper_length = st.number_input("Flipper Length (mm)", min_value=0)
body_mass = st.number_input("Body Mass (g)", min_value=0)
island_biscoe, island_dream, island_torgerson = 0, 0, 0
if island == "Biscoe":
    island_biscoe = 1
elif island == "Dream":
    island_dream = 1
elif island == "Torgerson":
    island_torgerson = 1
sex_female, sex_male = 0, 0
if sex == "Female":
    sex_female = 1
elif sex == "Male":
    sex_male = 1

new_prediction = rfc.predict(
    [
        [
            bill_length,
            bill_depth,
            flipper_length,
            body_mass,
            island_biscoe,
            island_dream,
            island_torgerson,
            sex_female,
            sex_male,
        ]
    ]
)
prediction_species = unique_penguin_mapping[new_prediction][0]
st.subheader("Predicting Your Penguin's Species:")
st.write("We predict your penguin is of the {} species".format(prediction_species))
st.write(
    "We used a machine learning (Random Forest) model to "
    "predict the species, the features used in this prediction "
    " are ranked by relative importance below."
)
st.image("feature_importance.png")
