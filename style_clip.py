import replicate
import requests
from PIL import Image
import os
#from web_load_image import load_image
import numpy as np
#from google.cloud import storage
#import request_image

# Check project on GCP
# gcloud projects list

# Export to env before start
# export REPLICATE_API_TOKEN="r8_OUL8yz2IUaDjewlOtVB11VUxNfZay6s3CMKx6"


# Paths - Change to GCP
##########################################################################################################################
original_image_path = '/Users/lucaskawasaki/Desktop/Project/replicate/original/000019.jpg' # input from user and search dataset
output_path = '/Users/lucaskawasaki/Desktop/Project/replicate/generated/'
##########################################################################################################################


# client = storage.Client()
# bucket = client.get_bucket(bucket)
# blob = bucket.blob(path)
# original_image_path = blob.download_as_string()

#original_image_path = gs://raw-data-align-celeba/styleGAN_project/img_align_celeba/000019.jpg

# Input and set variables
##########################################################################################################################
#target = 'black hair' # input from user
#manipulation_strength = [-7.5, -6.0, -4.5, -3.0, -1.5, 1.5, 3.0, 4.5, 6.0, 7.5] # 10 points
#manipulation_strength = [-4.5, -3.0, 3.0, 4.5]
#print(manipulation_strength)
##########################################################################################################################


##########################################################################################################################
def image_generator(image, target, manipulation):
    output = replicate.run('orpatashnik/styleclip:7af9a66f36f97fee2fece7dcc927551a951f0022cbdd23747b9212f23fc17021',
                           input={'input': open(image, "rb"), # user input
                                  'neutral': 'a happy face', # default
                                  'target': target, # user input
                                  'manipulation_strength': manipulation, # manipulation_strength
                                  'disentanglement_threshold': 0.15 # default
                                 }
                          )
    return output # link generated by replicate
##########################################################################################################################

##########################################################################################################################
def save_image(link, manipulation):
    img_data = requests.get(link).content
    output_image_path = str(manipulation) + '.jpg'
    with open(output_image_path, 'wb') as handler:
        handler.write(img_data)
    return output_image_path


# def save_image(link, folder_path, manipulation):
#     img_data = requests.get(link).content
#     output_image_path = folder_path + '/' + str(manipulation) + '.jpg'
#     with open(output_image_path, 'wb') as handler:
#         handler.write(img_data)
#     return output_image_path


##########################################################################################################################

def style_clip(original_image_path, target, manipulation_strength):
#def style_clip(original_image_path, target, folder_path, manipulation_strength):

    # Create a output image based on image input, target input and manipulation strength variation
    ##########################################################################################################################
    for manipulation in manipulation_strength:
        print(manipulation)
        output = image_generator(image=original_image_path, target=target, manipulation=manipulation)
        save_image(link=output, manipulation=manipulation)

    # for manipulation in manipulation_strength:
    #     print(manipulation)
    #     output = image_generator(image=original_image_path, target=target, manipulation=manipulation)
    #     save_image(link=output, folder_path=folder_path, manipulation=manipulation)
    ##########################################################################################################################




# manipulation_strength = np.arange(3, 8.2, 0.2) #
# manipulation_strength = np.round(manipulation_strength, 2).tolist()




# # Target input
# ##############################################################
# target_input = {
#     'hair': ['black'], #, 'blonde'],
#     'eyes': ['blue'], #, 'brown'],
#     'nose': ['thin'],
#     #'chin': ['double'],
#     #'smile': ['smile'], #, 'not smile'],
#     #'ear': ['big']
# }
# #target_input_keys = list(target_input.keys())
# print(target_input['hair'][0])
