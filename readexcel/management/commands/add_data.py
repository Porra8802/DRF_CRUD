from django.core.management.base import BaseCommand
from readexcel.models import ReadExcel
from sqlalchemy import create_engine

import pandas as pd

class Command(BaseCommand):
    help_text='A command to add data from Excel to DB'

    def handle(self, *args, **options):
        excel_file='uni2.xlsx'
        df= pd.read_excel(excel_file)
        engine=create_engine('sqlite:///db.sqlite3')
        df.to_sql(ReadExcel._meta.db_table, if_exists='replace', con=engine, index=False)
        sum_columns=['C', 'D']
        additional_col=['E']
        new_df=df.reindex(df.columns.to_list()+additional_col, axis=1)
        for i in range(0, len(new_df)):
            if new_df.loc[i, 'C']>0 and new_df.loc[i, 'D']>0:
                new_df.loc[i, 'E']=new_df.loc[i, 'C'] + new_df.loc[i, 'D']
              
            else:
                new_df.loc[i, 'E']=0
        print(new_df)


