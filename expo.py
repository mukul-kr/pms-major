
def predict(X):
    def scaled_exponential_map_ph(value, power, extra):
        value = 1 - abs((value - 7) / 7)
        return 1 - abs(((value - 1 + extra) ** power - extra**power) / extra**power)


    def mapFromTo(x: float, a: float, b: float, c: float, d: float) -> float:
        if x > b:
            x = b
        if x < a:
            x = a
        y = (x - a) / (b - a) * (d - c) + c
        return y


    def scaled_exponential_map_tds(value):
        _value = mapFromTo(value, 0, 1000, 0, 1000)
        a = 0.000001875
        b = -0.002875
        c = 1

        return abs(a * _value**2 + b * _value + c)


    def scaled_exponential_map_turbidity(value):
        return mapFromTo(mapFromTo(value, -50, 80, 0, 5), 0, 5, 1, 0)


    tds, ph, turbidity = X[0][0], X[0][1], X[0][2]
    ph_score = scaled_exponential_map_ph(ph, 4, 2)
    tds_score = scaled_exponential_map_tds(tds)
    turbidity_score = scaled_exponential_map_turbidity(turbidity)
    print(ph_score, tds_score, turbidity_score)
    return (ph_score + tds_score + turbidity_score) / 3


# Example usage
import marshal
import pickle
if __name__ == '__main__':
    tds = 1600
    ph = 14
    turbidity = 250
    X = [[tds, ph, turbidity]]
    # print(predict(X))
    print(predict)
    # with open('model.pkl', 'wb') as file:
    #     pickle.dump(marshal.dumps(predict.__code__), file)
    # print(cs)
    with open('model.pkl', 'rb') as f:
        c = pickle.load(f)
        # print(loaded_function)

    import marshal, types

    func = types.FunctionType(marshal.loads(c), globals())
    print(func(X))

