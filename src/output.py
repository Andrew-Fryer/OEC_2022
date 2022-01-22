import os

def save_file(df, file_name):
    f = os.path.join('../output', file_name)
    df.to_csv(f, header=False)
    return f
