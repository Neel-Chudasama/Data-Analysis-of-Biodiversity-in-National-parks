'''
Use this line to reload the library after making changes
import ds_utils
from importlib import reload
reload(ds_utils)
'''


def eda(df):
    """
    getting some basic information about each dataframe
    shape of dataframe i.e. number of rows and columns
    total number of rows with null values
    total number of duplicates
    data types of columns

    Args:
    df (dataframe): dataframe containing the data for analysis
    """
    print()
    print(f"Rows: {df.shape[0]} \t Columns: {df.shape[1]}")
    print()
    
    print(f"Total null rows: {df.isnull().sum().sum()}")
    print(f"Percentage null rows: {round(df.isnull().sum().sum() / df.shape[0] * 100, 2)}%")
    print()
    
    print(f"Total duplicate rows: {df[df.duplicated(keep=False)].shape[0]}")
    print(f"Percentage dupe rows: {round(df[df.duplicated(keep=False)].shape[0] / df.shape[0] * 100, 2)}%")
    print()
    
    print(df.dtypes)
    print("-----\n")
    
    print()
    print("The head of the dataframe is: ")
    display(df.head(5))
    
    print()
    print("The tail of the dataframe is:")
    display(df.tail(5))
    
    print()
    print("Description of the numerical columns is as follows")
    display(df.describe())

def protected(value):
    '''
    This function is used with the lambda function to create a new column containing boolean data. Im this case it returns False if the reow has no intervention data in it.
    
    Args:
    value: This the cell value which is taken from another column
    '''
    if value == 'No Intervention':
        return False
    else:
        return True

def one_value(names_list):
    '''
    This function returns the first object in the list if there are multiple items split by a comma 

    Args:
    names_list: list which needs to be split
    '''    
    for index,i in enumerate(names_list):
        if ',' in i:
            names_split = i.split(',')
            names_list[index] = names_split[0]
    return names_list 


def general_name(names_list):
    '''
    This function returns the first animal name if it has a brackets or the last word as the animal name if it doesn't

    Args:
    names_list: list containing animal names
    '''
    for index,i in enumerate(names_list):
        names_split = i.split(' ')
        if ')' in names_split[-1]:
            names_list[index]=names_split[0]
        else:
            names_list[index]=names_split[-1]
    return names_list


def plot_count(names_list):
    '''
    This function plots the count of the animals

    Args:
    names_list: list containing animals and the count that gets plotted
    '''

    from collections import Counter
    counts = Counter(names_list)
    df = pd.DataFrame.from_dict(counts, orient='index').rename(columns = {0:'Count'}, index = {'':'Animals'})
    df.sort_values(by='Count',ascending = False).head(10).plot(kind = 'bar',figsize = (15,7))
    plt.xticks(rotation = 0)
    plt.xlabel('Animal Names')
    plt.ylabel('Count')
    plt.title("Count of animal per species")
    plt.show()


def observation_per_park(animal, animal_df):
    '''
    This function returns the number of observations per park and plots them as a bar chart

    Args:
    animal: The animal name being plotted
    animal_df: The dataframe containing only that set of animals 
    '''
    animal_df.groupby(['park_name','is_protected']).sum().unstack().plot(kind='bar',figsize = (15,7))
    plt.xticks(rotation = 0)
    plt.title("Number of observations for " + str(animal)+ " per park")  
    plt.xlabel("Park name")
    plt.ylabel("Number of observations")
    plt.legend(title='Protected or not',labels = ['False','True'])
    plt.show()