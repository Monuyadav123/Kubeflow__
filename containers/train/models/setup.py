
from setuptools import setup
 
REQUIRED_PACKAGES = [pandas,torch,sklearn,torchvision]
 
setup(
   name="Test_model",
   version="0.1",
   scripts=["model_prediction.py"],
   install_requires=REQUIRED_PACKAGES
)