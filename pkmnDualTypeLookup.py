#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 17:25:32 2025

@author: NeilN
"""

import pandas as pd

# Load Pokémon data
data_url = 'https://raw.githubusercontent.com/lgreski/pokemonData/refs/heads/master/Pokemon.csv'
poke_df = pd.read_csv(data_url)

# Ensure column names are correctly formatted
poke_df.columns = poke_df.columns.str.strip()

# User input handling
def clean_input(type_name):
    type_name = type_name.strip().capitalize()
    return type_name

# Prompt user for input
type1_input = clean_input(input("Enter your first type: "))
type2_input = clean_input(input("Enter your second type: "))

# Filter Pokémon based on type combination
filtered_pokemon = poke_df[
    ((poke_df['Type1'] == type1_input) & (poke_df['Type2'] == type2_input)) |
    ((poke_df['Type1'] == type2_input) & (poke_df['Type2'] == type1_input))
]

# Display results
if filtered_pokemon.empty:
    print(f"No dual-type {type1_input}/{type2_input} Pokémon found.")
elif type2_input ==  " ":
  print(f"All {type1_input}-type Pokémon:")
  for _, row in filtered_pokemon.iterrows():
      print(f"* {row['Name']} ({row['ID']})")
else:
    print(f"All dual-type {type1_input}/{type2_input} and/or {type2_input}/{type1_input} Pokémon:")
    for _, row in filtered_pokemon.iterrows():
        print(f"* {row['Name']} # {row['ID']}", end=" ")
        print("(" + row['Form'] + ")" if row['Form'] != " " else " ")

