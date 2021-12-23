
from sklearn import metrics
from tkinter import messagebox as mb
from sklearn.naive_bayes import GaussianNB, MultinomialNB


from sklearn.preprocessing import LabelEncoder

def answer1():
    mb.showinfo("Naïve Bayes Classifier", "Classification has done!")
def classify(train, test,path):






    # Gaussian Naive Bayes with alpha =2

    gnb = MultinomialNB(alpha=2)

    train_set = train
    test_set= test



    class_idx = train_set.shape[1] - 1
    test_idx= test_set.shape[1]-1


    # split train set
    X_train = train_set.iloc[:, :class_idx]
    y_train = train_set.iloc[:, class_idx]

    # split test set
    X_test = test_set.iloc[:, :test_idx]
    y_test = test_set.iloc[:, test_idx]

   # gnb.param.probability = 1



   # print(X_train, y_train)
    gnb.fit(X_train, y_train)




        # predict current set

    out=[]
    pred = gnb.predict(X_test)
    for i in pred:
        if(i==1):
            out.append("Y")
        else:
            out.append("N")
    path= path+'/output.txt'
    to_text(path,out)
    answer1()

    def answer():
        mb.showinfo("message", "classification is done!")
    #print(gnb.score(X_test, y_test))




#write the predicton in y/n instead 1/0 to text file
def to_text(path,pred):
    j=0
    output = open(path, "w")
    for i in pred:
        output.write(str(j) + " " + i + "\n")
        j+=1
    output.flush()
    output.close()



