# Define the base image - use official python image from docker
FROM python:3.10-slim 

# Expose the port to be used to run the application
EXPOSE 8501

# Create a working directory
WORKDIR /app

# Copy all the requirements into the new directory created 
# Copy [source / destination]
COPY requirements.txt ./requirements.txt

# Install all that is in the requirements.txt file
RUN pip3 install -r requirements.txt

# Copy our app from the current directory to the working area
COPY . .

# Run the streamlit app
CMD streamlit run app.py




