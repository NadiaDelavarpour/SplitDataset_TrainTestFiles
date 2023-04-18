#!/usr/bin/env python
# coding: utf-8

# In[78]:


import os
import random
import shutil


# In[79]:


# Set the paths for your original folder, train folder, and validation folder
original_folder = "H:/Ortho_Data/Annotation_Images/Image_All/Images/"
train_folder = "H:/Ortho_Data/Annotation_Images/train"
val_folder = "H:/Ortho_Data/Annotation_Images/val"

# Create the train and validation folders if they don't exist
if not os.path.exists(train_folder):
    os.makedirs(train_folder)
if not os.path.exists(val_folder):
    os.makedirs(val_folder)


# In[80]:


# Set the split ratio (80% train, 20% validation)
split_ratio = 0.92


# In[81]:


# Get the list of image files in the original folder
image_files = [f for f in os.listdir(original_folder) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
print(image_files)


# In[82]:


# Shuffle the list of image files
random.shuffle(image_files)


# In[83]:


# Split the image files into train and validation sets based on the split ratio
split_index = int(len(image_files) * split_ratio)
train_files = image_files[:split_index]
val_files = image_files[split_index:]


# In[84]:


# Copy the image files and their corresponding json files to the train and validation folders
for file in train_files:
    # Copy the image file
    shutil.copy(os.path.join(original_folder, file), train_folder)
    # Copy the corresponding json file
    json_file = os.path.splitext(file)[0] + '.json'
    shutil.copy(os.path.join(original_folder, json_file), train_folder)


# In[85]:


for file in val_files:
    # Copy the image file
    shutil.copy(os.path.join(original_folder, file), val_folder)
    # Copy the corresponding json file
    json_file = os.path.splitext(file)[0] + '.json'
    shutil.copy(os.path.join(original_folder, json_file), val_folder)


# In[ ]:




