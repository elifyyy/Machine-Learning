import logisticRegression as lr

print("Predicted classes (1 is for female , 0 is for male)")
print(lr.y_pred)
print("****")
print("Real classes (1 is for female, 0 is for male)")
print(lr.Y)
print("****")
print("Accuracy : ")
print(lr.score)