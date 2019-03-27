import sys
from sklearn.externals import joblib
from corpus import *
from classifier import *

def main():
    args = get_args()
    
    with open(sys.argv[1],"rb") as FI:
        model = joblib.load(FI)
        qa = JurQA()
        qa.question.init_text(sys.argv[2])
        feat = args.features
        result = model.predict([FEAT[feat](qa)])
        print(result)

if __name__ == "__main__":
    main()