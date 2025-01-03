#!/usr/bin/env python
# coding: utf-8

# # E-Commerce Sales Analysis

# # Objectives
# # 1) Calculete yearly sale revenue earn.
# # 2) Calculate Monthly Sales and identify which is the highest & lowest saleing month.
# # 3) Analyze sales based product category & identify which is the highest and lowest category.
# # 4) The sales analysis needs to be done based on sub-category.
# # 5) Need to analyze the monthly pfrofit and identify which is the highest & lowest profit month.
# # 6) Analyze profit by Category and Sub-category.
# # 7) Analyze month wise profit.
# # 8) Calculete which region earns the highest and lowest Revenue.
# # 9) Analyze most preferalbe shiping mode by customer segment.
# # 10) Analyze Customer segment wise sales and profit.
# # ~~~~~:~~~~~
# # Required Library Imports

# In[7]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as pgo
import plotly.io as pio
import plotly.colors as pcolour
pio.templates.default = "plotly_white"


# # data import and info. read

# In[9]:


df = pd.read_csv("Sample - Superstore.csv", encoding = 'latin-1')


# In[17]:


df.head()


# # Statistical description and information of the data set 

# In[28]:


df.describe()


# In[56]:


df.info()


# # Data cleaning or manipulation
# # -----!!!~~~~

# # Order_date data type conversion

# In[54]:


df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])


# # Addition of 3 columns accordingly year, month , day

# In[61]:


df["Order_year"] = df["Order Date"].dt.year
df["Order_month"] = df["Order Date"].dt.month
df["Order_day"] = df["Order Date"].dt.dayofweek


# In[65]:


df.head(2)


# # 1) Calculete yearly sales revenue earn.

# In[71]:


Sales_by_year = df.groupby("Order_year")['Sales'].sum().reset_index()


# In[83]:


Sales_by_year
print(Sales_by_year)
Yearly_sales_fig = px.line(Sales_by_year,
                           x = 'Order_year',
                           y = 'Sales',
                           title = "Yearly Sales")
Yearly_sales_fig.show()


# # 2) Calculate Monthly Sales and identify which is the highest & lowest saleing month.

# In[85]:


Sales_by_month = df.groupby("Order_month")['Sales'].sum().reset_index()


# In[87]:


print(Sales_by_month)
Monthly_sales_fig = px.line(Sales_by_month,
                           x = 'Order_month',
                           y = 'Sales',
                           title = "Monthly Sales")
Monthly_sales_fig.show()


# # 3) Analyze sales based product category & identify which is the highest and lowest category.

# In[95]:


sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()


sales_by_category_fig = px.pie(sales_by_category, 
             values='Sales', 
             names='Category', 
             hole=0.5, 
             color_discrete_sequence=px.colors.qualitative.Pastel)

sales_by_category_fig.update_traces(textposition='inside', textinfo='percent+label')
sales_by_category_fig.update_layout(title_text='Sales Analysis by Category', title_font=dict(size=24))

sales_by_category_fig.show()


# # 4) The sales analysis needs to be done based on sub-category.

# In[98]:


sales_by_subcategory = df.groupby('Sub-Category')['Sales'].sum().reset_index()
sales_by_subcategory_fig = px.bar(sales_by_subcategory, 
             x='Sub-Category', 
             y='Sales', 
             title='Sales Analysis by Sub-Category')
sales_by_subcategory_fig.show()


# # 5) Need to analyze the monthly pfrofit and identify which is the highest & lowest profit month.

# In[116]:


profit_by_month = df.groupby('Order_month')['Profit'].sum().reset_index()
print(profit_by_month)
profit_by_month_fig = px.line(profit_by_month, 
              x='Order_month', 
              y='Profit', 
              title='Monthly Profit Analysis')
profit_by_month_fig.show()


# # 6) Analyze profit by Category and Sub-category.

# In[123]:


profit_by_category = df.groupby('Category')['Profit'].sum().reset_index()
print(profit_by_category)

fig = px.pie(profit_by_category, 
             values='Profit', 
             names='Category', 
             hole=0.5, 
             color_discrete_sequence=px.colors.qualitative.Pastel)

fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(title_text='Profit by Category', title_font=dict(size=16))

fig.show()


# In[127]:


profit_by_subcategory = df.groupby('Sub-Category')['Profit'].sum().reset_index()
print(profit_by_subcategory)
fig = px.bar(profit_by_subcategory, x='Sub-Category', 
             y='Profit', 
             title='Profit Analysis by Sub-Category')
fig.show()


# # 7) Analyze month wise profit.

# In[134]:


Profits_by_month = df.groupby("Order_month")['Profit'].sum().reset_index()


# In[144]:


print(Profits_by_month)
fig = px.line(Profits_by_month, 
              x='Order_month', 
              y='Profit', 
              title='Monthly Profit Analysis')
fig.show()


# # 8) Calculete which region earns the highest and lowest Revenue.

# In[151]:


Sales_by_region = df.groupby("Region")['Sales'].sum().reset_index()


# In[153]:


Sales_by_region


# In[157]:


fig = px.pie(Sales_by_region, 
             values='Sales', 
             names='Region', 
             hole=0.5, 
             color_discrete_sequence=px.colors.qualitative.Pastel)

fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(title_text='Sales by Region', title_font=dict(size=16))

fig.show()


# # 9)Analyze most preferalbe shiping mode by customer.

# In[173]:


shiping_mode_by_customer = df.groupby("Ship Mode")['Order ID'].count().reset_index()


# In[175]:


shiping_mode_by_customer


# In[181]:


fig = px.pie(shiping_mode_by_customer, 
             values='Order ID', 
             names='Ship Mode', 
             hole=0.3, 
             color_discrete_sequence=px.colors.qualitative.Pastel)

fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(title_text='Sales by Region', title_font=dict(size=16))

fig.show()


# # 10) Analyze Customer segment wise sales and profit.

# In[198]:


sales_profit_by_segment = df.groupby('Segment').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()

color_palette = pcolour.qualitative.Pastel

fig = pgo.Figure()
fig.add_trace(pgo.Bar(x=sales_profit_by_segment['Segment'], 
                     y=sales_profit_by_segment['Sales'], 
                     name='Sales',
                     marker_color=color_palette[0]))

fig.add_trace(pgo.Bar(x=sales_profit_by_segment['Segment'], 
                     y=sales_profit_by_segment['Profit'], 
                     name='Profit',
                     marker_color=color_palette[1]))

fig.update_layout(title='Sales and Profit Analysis by Customer Segment',
                  xaxis_title='Customer Segment', yaxis_title='Amount')

fig.show()


# In[ ]:




