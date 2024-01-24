import pandas as pd
import zipfile
import const as c 

class CSVTransformer:

    @staticmethod
    def read_data(path, name, header, skipfooter, skiprows):
        with zipfile.ZipFile(file=path, mode='r') as z:
            with z.open(name) as f:
                df = pd.read_excel(f, header=header, skipfooter=skipfooter, skiprows=skiprows)
        return df

    @staticmethod
    def transformations(tuples_list):
        new_list = []
        for i, tuple in enumerate(tuples_list):
            if i == 0 or i == 1:
                new_list.append(tuple[0])
            elif 2 <= i <= 15:
                new_list.append(tuple[1])
        return new_list

    @staticmethod
    def execute():
        df = CSVTransformer.read_data(c.path, c.name, c.header, c.skipfooter, c.skiprows)
        parsed_names = CSVTransformer.transformations(tuples_list=list(df.columns))
        df.columns = parsed_names
        df.to_csv(r'Victims_Age_by_Offense_Category_2022(processed).csv', index=False)

try:
    CSVTransformer.execute()
except Exception as e:
    print(f"Se ha producido un error: {e}")