import paramread
#import parser3
import febuilder
from featmethods import femethods
import argparse

def main():
	print("main")

	#params = paramread.readParams("/Users/alrossi/Downloads/codNatAux/cfg.txt")

	parser = argparse.ArgumentParser()
	parser.add_argument("-p", "--paramf", help="Parameters file", required=True)
	parser.add_argument("-i", "--imgdir", help="Images directory", required=True)
	parser.add_argument("-o", "--outdir", help="Output directory", required=True)
	args = parser.parse_args()

	print(args)

	images_dir = args.imgdir
	#output_dir = "/Users/alrossi/Downloads/"
	output_dir = args.outdir
	#output_filename = "saidaOBJ"

	params = paramread.readParams(args.paramf)

	print("\n Params no main: ", params)

	for k, args in params.items():
		# SAVE OBJ FILE

		print("\n k: ", k)
		print("\n args: ", args)
		builder_obj = febuilder.FeaturesBuilder()
		femethods_obj = builder_obj.build_feat_extractor_obj(args)
		builder_obj.save_febuilder(output_dir, k, femethods_obj)

		#LOAD THE OBJ FILE AND CREATE THE DATASET
		builder_obj = febuilder.FeaturesBuilder()
		femethods_obj = builder_obj.load_febuilder(output_dir, k)
		X, y = femethods_obj.create_data_set(images_dir, output_dir, k)

if __name__ == '__main__':
    main()
