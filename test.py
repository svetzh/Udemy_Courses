# import pandas as pd
# GOT = pd.read_html("https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes")
#
# pd.set_option("display.max_columns", None)
# pd.set_option("display.max_colwidth", None)
#
# print(GOT[4])

#
# piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
# piano_tuple = ("do", "re", "mi", "fa", "sol", "la", "ti")
# print(piano_tuple[2:5])


import pandas as pd

# Create a simple DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 28]}

df = pd.DataFrame(data)
print(df)

# Iterate through the rows
for index, row in df.iterrows():
    print(f"Index: {index}")
    print(f"Name: {row['name']}")
    print(f"Age: {row['age']}")
    print("---")