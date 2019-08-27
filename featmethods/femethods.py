#featmethods : nome da pasta e glcm: nome do arquivo .py
from featmethods import glcm
from featmethods import lbp
from featmethods import hog
from featmethods import colorhist
from featmethods import humoments 
import pandas as pd
from scipy import misc
import os
import numpy as np

#import hog

class FEMethods:

    def __init__(self, param_list):
        self.extractor_list = self.__build_feature_extractor(param_list)

    #def extract(self):
    #    raise NotImplementedError("Please Implement this method")

    ##  Read images from specified path. Extracts images descriptors and labels.
    #
    #   This function takes the path to an image set and a classifier object.
    #   It extracts features according to the feature extractor configured
    #   in classifier.
    #
    #   The labels are assigned from the first character in the images filename.
    #   A image named A1.bmp will be interpreted as a representative of class "0",
    #   B156.bmp is labed as being of class "1", C will be labeled as class "2"
    #   and so forth.
    #
    #   Args:
    #       path_to_dir: String containing the path of images source dir.
    #
    #
    #   Returns:
    #                    X: Numpy bidimensional array containing a vector of
    #                       features for each image.
    #                    y: Numpy column array with a int value for the label of
    #                       corresponding element in X.
    #
    def create_data_set(self, path_to_dir, dataset_output_dir, dataset_output_filename):

        filepath = os.path.join(dataset_output_dir, dataset_output_filename + ".csv")

        # Creating lists
        sample_list = []
        label_list  = []

        # Feedback for user
        print("Creating data set...")
        print("\tPath to images: " + path_to_dir)
        print("\tReading images...")

        list_files = sorted(os.listdir(path_to_dir))
        fileinfos = os.path.join(dataset_output_dir, dataset_output_filename + ".info")
        with open(fileinfos, "w") as file:
            file.write(str(list_files))

        # Iterates over dir listage.
        for name in list_files:

            # Load image
            img = misc.imread(os.path.join(path_to_dir,name))

            # Color channel reduction
            img = img[:,:,0]

            # Asks the classifier feature extractors for the image descriptors.
            sample = self.describe_img(img)

            # The labeling requires the first character in filename to be a capital
            # letter indicating that sample known class.
            #label = name[0]
            #label = label_map(label)

            # Converting data types
            sample_list.append(np.array(sample, dtype=float))
            label_list.append(name[0])
            #label_list.append(np.array(label, dtype=int))

        # Constructing arrays
        X = np.array(sample_list, dtype=float)
        #s = pd.Series(list(label_list)).astype('category')
        y = (pd.Series(label_list).astype('category')).cat.codes
        y = np.array(y, dtype=int).reshape(y.size, 1)
        #y = y.reshape(y.size, 1) #y.values.reshape


        # Ensures correct dimension
        X = np.concatenate(sample_list, axis=0)

        print("\t\tRead %d images" % y.size)

        #print("\n shape X: " + str(X.shape))
        #print("\n shape Y: " + str(y.shape))

        #save data set
        header_list = ["A" + str(i) for i in range(X.shape[1])]
        header_list.append("Class")
        print("\n Header list size: " + str(len(header_list)))
        data = np.concatenate((X,y), axis=1)
        #data = pd.DataFrame(data=[X, y], columns=header_list)
        data = pd.DataFrame(data=data, columns=header_list)
        data.to_csv(filepath)



        return (X, y)

    ##  Asks classifier to describe a image, but not to predict it's label
    #
    #   Args:
    #                    img: Image loaded as numpy array;
    #   Returns:
    #             descriptor: Image features;
    #
    def describe_img(self,img):

        # Aplica todos os processos a imagem
        sample = img
        #for process in self.img_proc_list:
        #    sample = process.apply(sample)

        # Calcula o vetor descritor
        descriptor = []
        for extractor in self.extractor_list:
            descriptor.append(extractor.calculate(sample))
            #descriptor = np.concatenate(descriptor,extractor.calculate(sample))

        # Retorna a predicao do modelo
        desc = np.concatenate(descriptor, axis=0)
        desc = desc.reshape(1,-1)

        return desc


    ##  Handles feature extraction objects creation.
    #   Args:
    #               param_list: Parameters dicitonary list;
    #   Returns:
    #              object_list: List of feature extraction objects;
    #
    def __build_feature_extractor(self,param_list):
        ftr_extractor_obj_list = []
        # Itera pela lista de dicionarios
        print("param_list: ", param_list)
        for k, param in param_list.items():
            # Gray Level Coocurence Matrix (GLCM)
            if k == 'glcm':
                print("\n GLCM: \n")
                ftr_extractor_obj_list.append(glcm.GLCM(**param))
            # Local Binary Patterns (LBP)
            elif (k == "lbp"):
                print("\n LBP: \n")
                ftr_extractor_obj_list.append(lbp.LBP(**param))
            # Histogram of oriented Gradients (HOG)
            elif (k == "hog"):
                print("\n HOG: \n")
                ftr_extractor_obj_list.append(hog.HOG(**param))
            elif (k == "colorHist"):
                print("\n Color Histogram \n")
                ftr_extractor_obj_list.append(colorhist.colorHist(**param))
            elif (k == "huMoments"):
                print("\n Hu Moments \n")
                ftr_extractor_obj_list.append(humoments.huMoments(**param))

            # Precisa de tratamento de erros
            else:
                print("Invalid extractor type")
        return ftr_extractor_obj_list
