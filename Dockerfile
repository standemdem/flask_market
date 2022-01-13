FROM ubuntu:latest
RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt
# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]

