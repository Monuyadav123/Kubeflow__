# Get an already prebuilt gcloud image that will be usefull running gcloud comands
FROM gcr.io/deeplearning-platform-release/pytorch-cpu:latest

# Create a subdirectory, enter it and clone our github repo to get the code for the trainer
RUN git clone https://github.com/jhammarstedt/gcloud_MLOPS_demo.git
RUN cd gcloud_MLOPS_demo/containers/train/
# Copy the deploy script from /containers/$current_container
COPY . .

# using bash we run the deploy script we just copied in here

ENTRYPOINT ["bash","./setup_model.sh"]
