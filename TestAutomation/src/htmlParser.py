#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all('a'):
        print(anchor.get('href', '/'))
        
        
# #!/usr/bin/env python3
# # Anchor extraction from HTML document
# import os
# from urllib.request import urlopen
# from urllib.request import urlretrieve
# from bs4 import BeautifulSoup
# 
# # reference URL
# with urlopen('https://www.imagesbazaar.com/') as response:
#     # make the object of Beautiful Soap
#     soup = BeautifulSoup(response, 'html.parser')
#     # give the img tag for images
#     for imgSrc in soup.find_all('img'):
#         # get the src of the particular img tag
#         strSrc = imgSrc.get('src')
#         try:
#             # check whether the src is url or not
#             if strSrc.index('://') > 0 :
#                 # define the folder path to store the downloaded image
#                 # os.getcwd() => Get the path of project directory
#                 filePathForImage = "{path}\\downloadedimages".format(path=os.getcwd())
#                 if os.path.exists(filePathForImage) == False:
#                     os.makedirs(filePathForImage)   
#                    
#                 # finally download all the images
#                 # string manipulation to set the image name 
#                 urlretrieve(strSrc, "{path}\\{name}.png".format(path=filePathForImage, name=strSrc[strSrc.rfind('/') + 1:]))
#         except Exception as e:
#             # in case we got the exception
#             continue
