def test():
    # check if exist
    # replace or add client rate
    # re-write the file
    import pandas as pd
    test_dic = {
        "client1": {"rate": 0.2},
        "client2": {"rate": 0.1},
        "client3": {"rate": 0.4},
        "client4": {"rate": 0.05},
        "client5": {"rate": 0.03},
        "client6": {"rate": 0.08},
        "client7": {"rate": 0.3},
        "client8": {"rate": 0.23},
        "client9": {"rate": 0.1},
        "client10": {"rate": 0.1}
    }
    df = pd.DataFrame.from_dict(test_dic)
    df.to_json('test.json')

    read_df = pd.read_json("test.json")
    read_dic = read_df.to_dict()
    read_dic["client1"]["rate"] = 1

    df = pd.DataFrame.from_dict(read_dic)
    df.to_json('test.json')


if __name__ == "__main__":
    test()
