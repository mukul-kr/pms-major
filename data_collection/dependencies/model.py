


# Example usage
import marshal, pickle, types
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
predict = types.FunctionType(marshal.loads(model), globals())

# if __name__ == '__main__':
#     tds = 1600
#     ph = 14
#     turbidity = 250
#     X = [[tds, ph, turbidity]]

#     print(predict(X))

