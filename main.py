from text2image import preprocess, process
#import text2image


# input user_query

user_query ='A young man with blond hair, mustache, a big nose, eyeglasses'

def main(user_query):
    df_new = process.load_data()
    ds, tfidf_matrix, vec_tfidf = process.vectorization(df_new)
    tfidf_matrix_query = process.text_audience_input(user_query, ds, tfidf_matrix, vec_tfidf)
    index_highsimilarity = process.calc_cosine_similarity(tfidf_matrix, tfidf_matrix_query)
    path_to_savedimages = process.show_pics(df_new, index_highsimilarity)

    return path_to_savedimages

if __name__ == '__main__':
    main(user_query)