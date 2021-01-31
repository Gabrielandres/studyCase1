#%%
import pandas as pd 
campaign = pd.read_csv('https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/bank.csv')
# %%
pd.set_option('display.max_rows', None, 'display.max_columns', None)
print(campaign)
# %%
import altair as alt 
nonExistentData = campaign[campaign['poutcome'] == 'nonexistent']
print(len(nonExistentData))
nonExistentData.head(10)

#%%
alt.data_transformers.disable_max_rows()
poutcome = alt.Chart(campaign).mark_bar(
    
).encode(
    alt.X('y:N', title='y'),
    alt.Y('count()', title='Random set of customers'),
    color=alt.Color('y:N', legend=None),
    column=alt.Column('poutcome:N', title='Has the client subscribed a term deposit?')
).properties(
    width=50,
)

poutcome
# %%
poutcome.save('poutcome.png')
# %%
job = alt.Chart(campaign).mark_bar(
    
).encode(
    alt.X('y:N', title='y'),
    alt.Y('count()', title='Number of people'),
    color=alt.Color('y:N', legend=None),
    column=alt.Column('job:N', title='Description of Jobs')
).properties(
    width=50,
)

job
# %%
job.save('job.png')
# %%
marital = alt.Chart(campaign).mark_bar(
    
).encode(
    alt.X('y:N', title='y'),
    alt.Y('count()', title='Number of people'),
    color=alt.Color('y:N', legend=None),
    column=alt.Column('marital:N', title='Marital Status')
).properties(
    width=50,
)

marital
# %%
marital.save('marital.png')
# %%
education = alt.Chart(campaign).mark_bar(
    
).encode(
    alt.X('y:N', title='y'),
    alt.Y('count()', title='Number of people'),
    color=alt.Color('y:N', legend=None),
    column=alt.Column('education:N', title='Education Status')
).properties(
    width=70,
)

education
# %%
education.save('education.png')
# %%
default = alt.Chart(campaign).mark_bar(
    
).encode(
    alt.X('y:N', title='y'),
    alt.Y('count()', title='Number of people'),
    color=alt.Color('y:N', legend=None),
    column=alt.Column('default:N', title='Credit in default')
).properties(
    width=50,
)

default
# %%
default.save('default.png')
# %%
housing = alt.Chart(campaign).mark_bar(
    
).encode(
    alt.X('y:N', title='y'),
    alt.Y('count()', title='Number of people'),
    color=alt.Color('y:N', legend=None),
    column=alt.Column('housing:N', title='Housing loan')
).properties(
    width=50,
)

housing
# %%
housing.save('housing.png')
# %%
loan = alt.Chart(campaign).mark_bar(
    
).encode(
    alt.X('y:N', title='y'),
    alt.Y('count()', title='Number of people'),
    color=alt.Color('y:N', legend=None),
    column=alt.Column('loan:N', title='Personal loan')
).properties(
    width=50,
)

loan
# %%
loan.save('loan.png')
# %%
