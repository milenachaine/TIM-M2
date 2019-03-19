
import sys
import os
phrase = str(sys.argv[1])
os.system('echo "'+phrase.replace('"','\"')+'" | tree-tagger-french > phrase.conll')

    
 
