#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # EMPLOYEE DATA ANALYSIS PROJECT

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


print("\n===== LOADING DATASET =====")


# # LOAD DATASET 

# In[3]:


emp_df = pd.read_csv(r"C:\Users\LENOVO\OneDrive\Documents\employees.csv")

print("\nFirst 5 rows:")
print(emp_df.head())

print("\nLast 5 rows:")
print(emp_df.tail())


# # BASIC INFORMATION

# In[4]:


print("\nShape of dataset:")
print(emp_df.shape)

print("\nData types:")
print(emp_df.dtypes)

print("\nInfo:")
print(emp_df.info())


# # MISSING VALUES

# In[5]:


print("\nMissing values per column:")
print(emp_df.isnull().sum())

emp_df['Salary'] = emp_df['Salary'].fillna(emp_df['Salary'].mean())
emp_df['Team'] = emp_df['Team'].fillna("No Team")


# # DUPLICATES

# In[6]:


print("\nDuplicate rows:", emp_df.duplicated().sum())


# # FEATURE ENGINEERING

# In[7]:


emp_df['Salary in Thousands'] = emp_df['Salary'] / 1000
emp_df['Bonus Amount'] = emp_df['Salary'] * emp_df['Bonus %'] / 100


# # STRING OPERATIONS
# 

# In[8]:


emp_df['Team'] = emp_df['Team'].astype(str).str.lower()

print("\nEmployees whose name starts with J:")
print(emp_df[emp_df['First Name'].str.startswith('J', na=False)])


# # DATETIME OPERATIONS

# In[9]:


emp_df['Start Date'] = pd.to_datetime(emp_df['Start Date'])

emp_df['Start Year'] = emp_df['Start Date'].dt.year
emp_df['Day of Week'] = emp_df['Start Date'].dt.day_name()

print("\nEmployees who joined in 1993:")
print(emp_df[emp_df['Start Year'] == 1993])


# # FILTERING / BOOLEAN INDEXING

# In[10]:


print("\nLegal Team Employees:")
print(emp_df[emp_df['Team'] == 'legal'])

print("\nSalary > 120000:")
print(emp_df[emp_df['Salary'] > 120000])

print("\nFemale Senior Management:")
print(emp_df[(emp_df['Gender'] == 'Female') & (emp_df['Senior Management'] == True)])

print("\nFinance OR Product Team:")
print(emp_df[emp_df['Team'].isin(['finance', 'product'])])


# # GROUPBY ANALYSIS

# In[11]:


print("\nAverage Salary by Team:")
print(emp_df.groupby('Team')['Salary'].mean())

print("\nTotal Bonus by Team:")
print(emp_df.groupby('Team')['Bonus Amount'].sum())

print("\nHighest Salary by Senior Management:")
print(emp_df.groupby('Senior Management')['Salary'].max())


# # AGGREGATION

# In[12]:


print("\nTeam Salary Statistics:")
print(emp_df.groupby('Team')['Salary'].agg(['mean','min','max']))

print("\nSalary + Bonus % by Team:")
print(emp_df.groupby('Team')[['Salary','Bonus %']].mean())


# # TRANSFORM

# In[13]:


emp_df['Team Average Salary'] = emp_df.groupby('Team')['Salary'].transform('mean')


# # FINAL CASE STUDY

# In[15]:


# Fill missing salary with median
emp_df['Salary'] = emp_df['Salary'].fillna(emp_df['Salary'].median())

# Group by Team & Gender
team_gender = emp_df.groupby(['Team','Gender'])['Salary'].mean()
print("\nTeam + Gender Average Salary:")
print(team_gender)

# Highest paying team
highest_team = emp_df.groupby('Team')['Salary'].mean().sort_values(ascending=False)
print("\nHighest Paying Team:")
print(highest_team.head(1))

print("\n===== PROJECT COMPLETED SUCCESSFULLY =====")


# In[1]:


python -m nbconvert --to script "assignment 11.ipynb"


# In[ ]:




