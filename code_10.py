from yelpapi import YelpAPI
import pandas as pd

api_key = "3NMb9TmdrYix0sTqFosQB0WZT67nqU9F05SLyrke95yAc3Ckkzug1y5hyF3u0Jl4Q9axv9DwcExfQXWEKZvDcerqxGZI1LLjherUuNbCDHDeprklFfb8ZDLISgdNZXYx"
yelp_api = YelpAPI(api_key)

# Search for pizza places in Austin with sorting by rating
search_term = "Pizza"
search_location = "Austin"
search_sort_by = "rating"
search_limit = 20

search_results = yelp_api.search_query(term=search_term, location=search_location,
                                       sort_by=search_sort_by, limit=search_limit)

# Create a DataFrame from the search results
result_df = pd.DataFrame.from_dict(search_results['businesses'])

# Print the aliases of the found businesses
print(result_df['alias'])

# Get the ID for one of the businesses (for example, the first one)
id_for_reviews = result_df.loc[0, 'alias']

# Retrieve reviews for the chosen business
reviews_result = yelp_api.reviews_query(id=id_for_reviews)

# Print the reviews
for review in reviews_result['reviews']:
    print(review['text'])

# Create a DataFrame from the reviews
reviews_df = pd.DataFrame.from_dict(reviews_result['reviews'])

# Print the search results DataFrame
print(result_df)

# Save the search results to a CSV file
result_df.to_csv(f"{search_term}_{search_location}_results.csv")

# Save the reviews to a CSV file
reviews_df.to_csv(f"{id_for_reviews}_reviews.csv")

