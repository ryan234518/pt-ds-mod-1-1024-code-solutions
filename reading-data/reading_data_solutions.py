# %%
import pandas as pd

# %%
new_cars = pd.read_csv(r"C:\Users\ryank\pt-ds-mod-1-1024-code-solutions\reading-data\mtcars.csv")
#takes the file path as a raw string instead of trying to read each backslash as a command
#if we just add another backslash to each backslash, this is also another way to read the file path

# %%
new_cars

# %%
new_cars.head() #shows the first 5 rows within the data 

# %%
import os

# %%
os.system('pwd')

# %%
!cd

# %%
pd.read_csv('mtcars.csv')

# %%
new_cars.to_csv("changed_cars.csv")

# %%
pd.read_csv(r"C:\Users\ryank\pt-ds-mod-1-1024-code-solutions\reading-data\changed_cars.csv")

# %%
new_Beer = pd.read_csv(r"C:\Users\ryank\pt-ds-mod-1-1024-code-solutions\reading-data\beer.txt", sep = ' ')

# %%
new_Beer

# %%
new_Beer.to_csv("changed_Beer", index = False)

# %%
pd.read_csv(r"C:\Users\ryank\pt-ds-mod-1-1024-code-solutions\reading-data\changed_Beer")

# %%
new_Beer

# %%
new_data = pd.read_csv(r"C:\Users\ryank\pt-ds-mod-1-1024-code-solutions\reading-data\u.data", sep = '\t')

# %%
new_data

# %%
new_data.to_csv('changed_data')

# %%
pd.read_csv(r"C:\Users\ryank\pt-ds-mod-1-1024-code-solutions\reading-data\changed_data", sep = ',')

# %%
new_data

# %%
new_item = pd.read_csv(r"C:\Users\ryank\pt-ds-mod-1-1024-code-solutions\reading-data\u.item", sep = '|', encoding = 'ISO-8859-1')

# %%
new_item.to_csv("changed_item", index = False)

# %%
pd.read_csv(r"C:\Users\ryank\pt-ds-mod-1-1024-code-solutions\reading-data\changed_item", sep = ',', encoding = 'ISO-8859-1')


