# Get an already prebuilt gcloud image that will be usefull running gcloud comands
FROM google/cloud-sdk:latest
# FROM python:3.8
#Create a subdirectory, enter it and clone our github repo to get the code for the trainer
RUN git clone https://github.com/jhammarstedt/gcloud_MLOPS_demo.git
RUN cd gcloud_MLOPS_demo/containers/deploy-toai/
#Copy the deploy script from /containers/$current_container

COPY deploy_toai.sh .


#using bash we run the deploy script we just copied in here
ENTRYPOINT ["bash","./deploy_toai.sh"]
