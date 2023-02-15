import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import annoy

data = pd.read_parquet("fashion_logs.parquet")

def data_process (data, features) : 
    product_data = data[['product_id'] + features].drop_duplicates('product_id')
    product_data[features] = product_data[features].astype('str')
    product_data.reset_index(drop=True, inplace=True)
    product_data['features'] = product_data['product_gender']+' ' +product_data['baseColor']+' ' +product_data['season']+' ' +product_data['year']+' ' +product_data['usage']+' ' +product_data['Category']

    tfidf = TfidfVectorizer()
    product_tfidf = tfidf.fit_transform(product_data['features'])
    product_tfidf = pd.DataFrame(product_tfidf.todense(), columns = tfidf.get_feature_names_out())
    return product_data, product_tfidf

product_data, product_tfidf = data_process(data, ['product_gender', 'baseColor', 'season', 'year', 'usage', 'Category'])

def recomm_sys (product_id) :
    product_data, product_tfidf = data_process(data, ['product_gender', 'baseColor', 'season', 'year', 'usage', 'Category'])

    load_annoy = annoy.AnnoyIndex(f=product_tfidf.shape[1], metric='angular')
    load_annoy.load('product.ann')

    product_index = product_data[product_data['product_id'] == product_id].index[0]
    product_vec = product_tfidf.iloc[product_index, :]
    get_nns_list = load_annoy.get_nns_by_vector(vector=product_vec, n=21, include_distances=False) # 유사한 벡터를 찾기 때문에 본인 포함
    return product_data.iloc[get_nns_list[1:]]
