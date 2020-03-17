# Use an official Python runtime as a parent image
FROM python:3.6.3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app
ADD app.py /app
ADD get_digit_info.py /app
ADD model.pth /app

# Install any needed packages specified in requirements.txt
#RUN pip install -r requirements.txt 
#RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/

RUN pip install --trusted-host mirrors.aliyun.com -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]

