title: Finding top opioid prescribers in the U.S., an Open Data Science Tutorial
date: 2015-06-01
categories: [programming, data science]
tags: [python, data science, data, health data]
description: Using recently released large datasets this tutorial will identify the top 100 opioid prescribers within Medicare's Part D program by total drug cost. 

*Scroll to the bottom of the page if you want to get right to the python code and totals for the first CSV of data.* 

###Background and Introduction
The **Centers for Medicare and Medicaid Services (CMS)** recently released a [massive dataset][1] on the Part D program containing
data on drug amounts, their cost, how many beneficiaries and claims were involved
and the *names* and locations of the physicians prescribing these medications.

In the spirit of the open data movement, and in time for the [2015 Health Data Palooza conference][2], this tutorial series proposes to total and visualize these data. The [code][3] will be made available for anyone to download and modify. This tutorial uses *free* open source software so you can replicate these findings even if you are using your wife's old macbook air over the weekend. 

####Open Data Science with Python
This tutorial uses Python and eventually Javascript. I will be going through this using a standard text editor and the resources available via the Mac terminal. I am using Python 2.7 along with the Pandas module (all free). If you have a PC you can follow along but the screens below will look different and the steps needed to get this running may take some effort to configure. 

**Note: These tutorials may be a struggle to someone new to Python, Javascript, and the web world generally. Proceed with caution, and see other
resources for more help.**

###Results first
By the end of this tutorial you'll be able to query the top N prescribers of opioids in 2013. Below I've pulled the top 5 by total drug cost (right screen0) from the first CSV, my code is on the left:
<img class="parent" src="{{ url_for('static', filename='media/top5_prescribers.png') }}">
*Bigger screenshots are provided below*

###Find, download and explore the data
For this first tutorial we'll total drug costs for one of the CSVs. Later we'll download and perform this operation over *all* the CSVs. Download the first workbook (Aa to AI) open and save it as a CSV. There are some ways to automate this using Python--and in the futre we'll attempt a script that completes this for us. 

####Understanding what we have
Let's take a breather, back up, and try and understand what we are looking at. After saving the data in our folder we can start writing some python scripts to look and manipulate it. 

In our python code we import the Pandas module and use it to look at the first ten observations. 
<pre><code class="language-python">
import pandas as pd
#Let's read in the CSV and retain the columns we're interested in.
df = pd.read_csv("PartD_Prescriber_PUF_NPI_DRUG_Aa_AL_CY2013.csv", nrows=100)
print df.head(10)
</code></pre>In running this code we'll be able to get a sense of this dataset, the variable names and what we'll need to do to transform it into something we can use. 

<img  class="parent" src="{{ url_for('static',  filename='media/investigate.png', width=100 )}}">

From this investigation we find some key variables: the prescriber's NPI (a unique identifier), their first and last name along with their city and state, the drug's total cost, and the name of the generic drugs. 

####What drugs should we investigate. What are opioids?

We need a list of the generic drugs of interest. After some simple internet sleuthing we find this [list of opioid generics from the FDA.][4] The opioid generics identified in this list include Fentanyl, Methadone Hydrochloride (HCL), Morphine Sulfate, and Oxymorphone HCL. 

###Finding totals by provider
In the interest of time I've provided below the final form of the code. Essentially, after reading our CSV into the Pandas module we identify the opioid generics of interest, we clean the total drug cost variable, and then we sum by the unique provider identifier (NPI). Once we have those totals we write that information to the 'top_prescribers_in_first_file' CSV. I've commented out the code below to offer some insight into what's happening at each step and please let me know in the comments if you'd like more information on anything going on below.
<pre><code class="language-python">
import pandas as pd
#Let's read in the CSV and retain the columns we're interested in.
df = pd.read_csv("PartD_Prescriber_PUF_NPI_DRUG_Aa_AL_CY2013.csv")

df = df[['npi', 'total_drug_cost', 'nppes_provider_last_org_name', 'nppes_provider_first_name', 'nppes_provider_city', 'nppes_provider_state', 'generic_name']]

#We identify the following generics as opioids. 

def opiods(series):
    if series["generic_name"]=="FENTANYL":
        return 1
    elif series["generic_name"]=="METHADONE HCL":
        return 1
    elif series["generic_name"]=="MORPHINE SULFATE":
        return 1
    elif series["generic_name"]=="OXYMORPHONE HCL":
        return 1
    else:
        return 0

#The opioids function is applied and the opioids retained. 
df['opioid_var'] = df.apply(opiods, axis=1)
df = df.loc[(df.opioid_var==True)]

#Our total drug cost column is messy and needs cleaning. 

df['total_drug_cost'] = df['total_drug_cost'].fillna(0)
df['total_drug_cost'] = df['total_drug_cost'].str.strip("$")
df['total_drug_cost'] = df['total_drug_cost'].str.replace(',','')
df['total_drug_cost'] = df['total_drug_cost'].astype(float)
#Group and sum by provider NPI, sort the summed column in descending order and send our dataset to a CSV file. 
df['tot'] = df['total_drug_cost'].groupby(df['npi']).transform('sum')
df = df.drop_duplicates(cols='npi')

top100 = df.sort('tot', ascending=False)[:100]
top100 = top100[['npi', 'tot', 'nppes_provider_last_org_name', 'nppes_provider_first_name', 'nppes_provider_city', 'nppes_provider_state']]

top100.to_csv('top_prescribers_in_first_file.csv')

</code></pre>

###Results
The output CSV returns the top 100 prescribers of opioids by total drug cost in 2013. We find the very top prescriber in this dataset prescriber $798,501 worth of opioids and the top 20 prescribers in this first file prescribed over $100,000 worth of opioids.

<img class="parent" src="{{ url_for('static', filename='media/top100excel.png') }}">


*Important note: There many be important factors about a prescriber's population (e.g. having more patients with cancer or in hospice) that are behind these totals. This basic analysis does not speak to any of those particular factors.* 

###Next steps
Ok, we've done this for one of our worksheets but we have more to do. The next tutorial will show you how to loop through the CSVs we have and save the top 100 prescribers from each. From there we'll use the mindset of the [mergesort alogrithmn][5] to find
the top 100 prescribers of opioids in the country. Finally, in the last tutorial we'll take this data and visualize their totals. 

Stay tuned.

[1]: http://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Part-D-Prescriber.html
[2]: http://healthdatapalooza.org/
[3]: https://github.com/wsankey/PartDAnalysis 
[4]: http://www.fda.gov/Drugs/DrugSafety/InformationbyDrugClass/ucm251735.htm
[5]: http://en.wikipedia.org/wiki/Merge_sort
