
# Import all from fasthtml.common
#### YOUR CODE HERE

# Import pandas
#### YOUR CODE HERE

# Initialize a fasthtml app
#### YOUR CODE HERE

# Using pandas, read in he 'ds_event.csv' file
#### YOUR CODE HERE

# Define a route for the landing page
# that uses a `get` method
#### YOUR CODE HERE

    # Generate the raw html for the pandas table
    # with the pandas .to_html method
    #### YOUR CODE HERE

    # Convert the raw html to a fasthtml object
    # using the fasthtml NotStr function
    #### YOUR CODE HERE

    # Using the `Titled` fasthtml function
    # Set the title of the page to an informative
    # title for the data, and pass the fasthtml table
    # as the second argument
    # Return the result
    #### YOUR CODE HERE

# Define a route with a dynamic
# `keyword` variable that can be passed
# to the routing function
# Include a `date` query parameter
#### YOUR CODE HERE

    # Filter the pandas dataframe to rows where the 
    # `description` column contains the `keyword`
    # received as an argument to this function
    #### YOUR CODE HERE

    # Check if date is not falsey
    #### YOUR CODE HERE
        # Filter the dataframe down to rows
        # where the `date` column is equal to the date
        # query parameter
        #### YOUR CODE HERE
    
    # Convert the filtered dataframe to
    # a list of dictionaries
    #### YOUR CODE HERE

    # Return the data as a json response
    #### YOUR CODE HERE


# Keep this line unchanged
serve()