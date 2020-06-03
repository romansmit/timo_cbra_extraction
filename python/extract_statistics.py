import os
import pandas as pd

if __name__ == '__main__':
    file_dir = os.path.dirname(os.path.abspath(__file__))
    # data_dir = os.path.join(os.path.expanduser('~'), 'Dropbox', 'timo_video_auswertung', 'cBra_autom_Auslesung', 'Test_Data')
    data_dir = file_dir
    selector_path = os.path.join(data_dir, 'selector.xlsx')
    out_path = os.path.join(data_dir, 'output.xlsx')

    keys = ['HRVmeanErr', 'HRVmedian', 'HRVStd', 'poincareMeanXX', 'poincareMeanYY', 'SD1', 'SD2']

    df = pd.read_excel(selector_path)

    def extract_value(data_dir, id_string, label_nr, key, sample_pt):
        path = os.path.join(data_dir, id_string, 'Label'+str(label_nr), key+'.csv')
        data = pd.read_csv(path, header=None)
        row_index = sample_pt - 1
        return data.iloc[row_index, 0]

    for key in keys:
        df[key] = df.apply(lambda row: extract_value(data_dir, row.ID, row.Label, key, row.Samplept), axis=1)

    df.to_excel(out_path, index=False)

    print(df)