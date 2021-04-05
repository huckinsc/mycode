#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    startdate = "start_date=2019-11-11"

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    #print(neodata)

    
    largest_name = ""
    largest_size = -1
    closest_name = ""
    closest_dist = 99999999999.9
    hazard_ct = 0
    print("Number of records: ", neodata['element_count'])
    for date in neodata['near_earth_objects']:
        for asterdict in neodata['near_earth_objects'][date]:
            #print(asterdict['name'])
            if asterdict['estimated_diameter']['kilometers']['estimated_diameter_max'] > largest_size:
                largest_size = asterdict['estimated_diameter']['kilometers']['estimated_diameter_max']
                largest_name = asterdict['name']
            if float(asterdict['close_approach_data'][0]['miss_distance']['kilometers']) < closest_dist:
                closest_dist = float(asterdict['close_approach_data'][0]['miss_distance']['kilometers'])
                closest_name = asterdict['name']
            if asterdict["is_potentially_hazardous_asteroid"]:
                hazard_ct += 1
    print("Largest asteroid:")
    print("\t",largest_name , " at " , largest_size,"KM")
    print("Closet asteroid:")
    print("\t",closest_name, "at" , closest_dist,"KM")
    print("The number of hazradus asteroids was:", hazard_ct)

if __name__ == "__main__":
    main()

