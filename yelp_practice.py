from yelpapi import YelpAPI

api_key = "3NMb9TmdrYix0sTqFosQB0WZT67nqU9F05SLyrke95yAc3Ckkzug1y5hyF3u0Jl4Q9axv9DwcExfQXWEKZvDcerqxGZI1LLjherUuNbCDHDeprklFfb8ZDLISgdNZXYx"

yelp_api_instance = YelpAPI(api_key)
search_term = 'pizza'
location_term = 'El Paso, TX'

search_results = yelp_api_instance.search_query(
    term=search_term, loaction=location_term,
    sort_by='rating', limit=20)

print (search_results)