from functools import reduce

def apply_function(x, func):
    return func(x)

def format_cols(car_df):
    car_df.columns = car_df.columns.str.lower().str.replace(' ',"_")
    car_df.rename(columns= {'st': 'state'}, inplace=True)
    return car_df

def clean_invalid_values(car_df):
    car_df["gender"].replace(to_replace=r'^[Ff]\w+', value='F', regex=True, inplace=True)
    car_df["gender"].replace(to_replace=r'^[Mm]\w+', value='M', regex=True, inplace=True)

    car_df["education"].replace({"Bachelors": "Bachelor"},inplace=True)

    car_df["state"].replace({"AZ": "Arizona", "Cali": "California", "WA": "Washington"},inplace=True)


    car_df = car_df.applymap(lambda x: x.replace('%',"") if isinstance(x,str) else x)

    car_df["vehicle_class"].replace(to_replace=["Sports Car","Luxury SUV","Luxury Car"],\
                                     value=["Luxury"]*3, inplace=True)

    return car_df

def format_type(car_df):
    # Your code here
    col = 'customer_lifetime_value'
    car_df[col] = car_df[col].apply(lambda x: float(str(x)))
    
    col2 = 'number_of_open_complaints'
    car_df[col2] = car_df[col2].apply(lambda num: int(num.split('/')[1] \
                                                    if isinstance(num,str) else -1))
    return car_df

def drop_nulls(car_df):
    # Lets drop rows of customers with nan values
    car_df.dropna(subset=['customer'],inplace=True)
    car_df.dropna(subset=['customer'],inplace=True)
    car_df['gender'].fillna(car_df.gender.mode()[0],inplace=True)
    car_df['gender'].fillna(car_df.gender.mode()[0],inplace=True)
    car_df['customer_lifetime_value'].fillna(method='bfill',inplace=True)
    car_df['customer_lifetime_value'].fillna(method='bfill',inplace=True)
    return car_df

def drop_dups(car_df):
    if car_df.duplicated().sum(): 
        print(f"ran drop dup: {sum}")
        car_df.drop_duplicates(inplace=True)
    return car_df

clean_funcs = [format_cols,clean_invalid_values,format_type,drop_nulls,drop_dups]

def run_clean_func(car_df):
    df = car_df
    for func in clean_funcs:
        df = apply_function(df, func)
    return df
