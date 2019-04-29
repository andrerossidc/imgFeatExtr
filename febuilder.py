from featmethods.femethods import FEMethods
import os
import pickle

##  @package classifier_builder
#
#   This module defines routines to manage classifier creation.

##  Classifier builder class.
class FeaturesBuilder:

    ##  Class constructor
    def __init__(self):
        pass
        #self.extractor_obj_list = self.build_feat_extractor_obj(param)

    ##  Save feature extractor obj to file
    #
    #   Args:
    #                   filepath: Classifier file.
    #   Returns:
    #             classifier_obj: Classifier object
    #
    def save_febuilder(self, dir, filename, febuilder_obj):
        filepath = os.path.join(dir, filename + ".obj")
        file = open(filepath,'wb')
        pickle.dump(febuilder_obj, file)
        file.close()


    ##  Load feature extractor obj  from file.
    #
    #   Args:
    #                   filepath: feature extractor obj file;
    #   Returns:
    #             feature extractor obj : feature extractor  object;
    #
    def load_febuilder(self, dir, filename):
        filepath = os.path.join(dir, filename + ".obj")
        file = open(filepath,'rb')
        unpickled = pickle.load(file)
        file.close()
        return unpickled

    ##  Splits arguments taken from the parser.
    #
    #   Args:
    #                      args: Argument object.
    #   Returns:
    #            args_dict_list: A list of dictionaries, one for each object
    #                            composing the classifier.
    def __parse_arguments(self,args):

        # Cria uma lista vazia para retornar
        param_dict_list = []

        # Process feature extraction methods arguments
        if (args.glcm == True):
            glcm_arguments = {}
            glcm_arguments['extractor'] = 'glcm'
            glcm_arguments['axis'] = args.axis
            param_dict_list.append(glcm_arguments)
            print("\n TEM GLCM \n")

        if (args.lbp == True):
            lbp_arguments = {}
            lbp_arguments['extractor'] = 'lbp'
            lbp_arguments['numPoints'] = args.numPoints
            lbp_arguments['radius'] = args.radius
            lbp_arguments['method'] = args.method
            param_dict_list.append(lbp_arguments)
            print("\n TEM LBP \n")

        if (args.hog == True):
            hog_arguments = {}
            lbp_arguments['extractor'] = 'hog'
            hog_arguments['orientations'] = args.orientations
            hog_arguments['pixels_per_cell'] = arg.pixels_cells
            param_dict_list.append(hog_arguments)
            print("\n Tem HOG \n")

        # Retorna a lista de dicionarios
        return param_dict_list




    ##  Handles creation and bundling of Classifier object parts.
    #   Args:
    #                    param: Arguments dicitonary list;
    #   Returns:
    #           classifier_obj: Classifier object ready for training;
    #
    def build_feat_extractor_obj(self,param):
        #print("Parametros: \n" + str(param))
        extractor_param_list = param #self.__parse_arguments(param)
        print("Parametros: \n" + str(extractor_param_list))


        # Constroi os objetos que compoem o FE method
        extractor_obj_list = FEMethods(extractor_param_list)

        # Monta o classificador
        return extractor_obj_list
