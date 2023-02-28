from utils import utils


parser = utils.Preprocessor("/home/lnit/rdb2graph/data/raw/mimic3","/home/lnit/rdb2graph/data/processed","/ADMISSIONS.csv","/ADMISSIONS_.csv")

parser.Preprocess()