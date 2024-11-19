from sklearn.tree import DecisionTreeClassifier
X=[[180,75,42],
   [160, 60, 38],  
    [170, 65, 40],  
    [155, 55, 36],  
    [165, 62, 39],  
    [175, 70, 41],
   [158, 64, 36],
   [177,73,42],
   [157,66,38]
   
]

Y=[1,0,1,0,0,1,0,1,0]

clf=DecisionTreeClassifier()

clf.fit(X,Y)

x=eval(input("enter specifications"))

prediction=clf.predict(x)

if(prediction[0]==1):
    print("Predicted Gender: Male")
else:print("Predicted Gender: Female")
