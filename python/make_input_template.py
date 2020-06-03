import os
import pandas as pd
from natsort import natsorted

if __name__ == '__main__':
    file_dir = os.path.dirname(os.path.abspath(__file__))
    # data_dir = os.path.join(os.path.expanduser('~'), 'Dropbox', 'timo_video_auswertung', 'cBra_autom_Auslesung', 'Test_Data')
    data_dir = file_dir
    out_path = os.path.join(data_dir, 'selector.xlsx')

    id_list = natsorted( next(os.walk(data_dir))[1] )
    df = pd.DataFrame(data={'ID': id_list, 'Label': None, 'Samplept': None})
    df.to_excel(out_path, index=False)

    print(df)
