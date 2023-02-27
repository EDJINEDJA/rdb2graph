from utils import utils


parser = utils.Preprocessing()

parser.DatasetPreparation("/home/lnit/rdb2graph/inputs/data/mimic3","/home/lnit/rdb2graph/inputs/newData","/ADMISSIONS.csv","/ADMISSIONS_.csv")