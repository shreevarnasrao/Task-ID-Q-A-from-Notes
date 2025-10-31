# Task-ID-Q-A-from-Notes
We will using python NLTK to make this code happen.
To Install NLTK go to termianl and type python3 -m pip install nltk.
Then go to import nltk vs code terminal and run this code 
nltk.download('punkt')        
nltk.download('stopwords')    
nltk.download('wordnet')    
nltk.download('averaged_perceptron_tagger')
First the text file sentences and paragraph will be extracted.Every letter will be convered to lowercase to avoid counting 2 same letter as different.Stop words such as a,the,is will be removed using nltk.stopword.It is spilt into different paragraphs and tokenized i.e dividing text input into smaller units.Overlap of letter in the question and each paragraph is looked.Whichever matches the most is presented as relevant paragraph. the vscode flags up bugs in my code which i cant seem to be figure out.
