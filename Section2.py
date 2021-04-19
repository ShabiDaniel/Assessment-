from dataprep.clean
import clean_phone

df = pd.DataFrame({'phone': ['0812345678']})
clean_phone(df, 'phone')