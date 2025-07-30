# Pokémon Dual-Type Lookup

A simple Python utility that allows users to input any two Pokémon types and returns a list of all Pokémon that have that specific dual-type combination — in either order.

This tool is helpful for trainers, theorists, and game designers who want to explore or analyze type synergies, rarity, and distribution across the generations.

## 🔍 Features

- Accepts any two Pokémon types as input (e.g., Fire and Dragon)
- Matches dual-type Pokémon regardless of input order (e.g., Fire/Dragon or Dragon/Fire)
- Pulls from a public dataset of all official Pokémon (including generations 1–8)
- Outputs a filtered list directly to the terminal

## 🧠 How It Works

The program:
- Loads a Pokémon dataset from an online CSV
- Normalizes input for capitalization/spacing
- Filters all Pokémon with matching `Type1` and `Type2` regardless of order
- Displays the result as a table

Data Source:  
[Pokemon.csv from lgreski/pokemonData](https://github.com/lgreski/pokemonData/blob/master/Pokemon.csv)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/goatnaidu06/dual-type-lookup.git  
cd dual-type-lookup  
```

### 2. Install Dependencies

```bash
pip install pandas  
```

### 3. Run the Script

```bash
python3 pkmnDualTypeLookup.py
```

You'll be prompted to enter two types:

```
Enter your first type: Water
Enter your second type: Ground
All dual-type Water/Ground and/or Ground/Water Pokémon:
* Wooper # 194  
* Quagsire # 195  
* Marshtomp # 259  
* Swampert # 260  
* Barboach # 339  
* Whiscash # 340  
* Gastrodon # 423  
* Palpitoad # 536  
* Seismitoad # 537  
* Swampert # 260 (Mega Swampert)
```

## 📁 File Structure

```
pkmnDualTypeLookup.py   # Main script for dual-type search
Pokemon.csv         # CSV dataset containing Pokémon names, types, and form data  
README.md               # Project documentation
LICENSE.txt           # Project license

```

## 🔮 Example Use Cases

- Check which Pokémon are Water/Ground types
- Find unique dual-type combos like Electric/Ice or Ghost/Normal
- Game design ideas: See underused or overused type combinations
```
Enter your first type: Water
Enter your second type: Ground
All dual-type Water/Ground and/or Ground/Water Pokémon:
* Wooper # 194  
* Quagsire # 195  
* Marshtomp # 259  
* Swampert # 260  
* Barboach # 339  
* Whiscash # 340  
* Gastrodon # 423  
* Palpitoad # 536  
* Seismitoad # 537  
* Swampert # 260 (Mega Swampert)
```

## 🎯 Future Improvements

- Add generation filters  
- Support for regional forms  
- Type effectiveness summary for the combo  
- Export results to CSV or Markdown  

## 📜 License

MIT License. See [LICENSE](LICENSE.txt) for details.

## 👨‍💻 Author

**Neil Naidu**  
[GitHub Profile](https://github.com/goatnaidu06)
