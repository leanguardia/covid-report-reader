from os import walk

import cv2
import pandas as pd
import pytesseract as ocr

from readers.parsers import OcrDataParser
from readers.report_reader import ReportReader
from img.processing import process#, grayscale, threshold 

def show_img(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

reports_path = 'img/reportes_salud/'
_, _, filenames = next(walk(reports_path))
# filenames = ['1353866415820955648_0.png']

failed_files = ['.DS_Store',
          '1343723603758604292_0.png',
          '1350611856755470338_0.png',
          '1348071689251393540_0.png',
          '1337599696790020096_0.png',
          '1343007009491329029_0.png',
          '1345896948281257984_0.png',
          '1354235109247954945_0.png',
          '1339744745611022341_0.png',
          '1346620363992662020_0.png',
          '1344487124720996352_0.png',
        ]

df_data = {
  'number': [],
  'date': [],
  'time': [],
  'new_cases': [],
  'new_deaths': [],
  'recovered': [],
  'active': [],
  'deaths': [],
  'suspicious': [],
  'accumulated': [],
  'discarted': [],
  'beni': [],
  'chuquisaca': [],
  'cochabamba': [],
  'la_paz': [],
  'pando': [],
  'santa_cruz': [],
  'tarija': []
}
for filename in filenames:
    print("\n> Processing:", filename)
    if filename in failed_files: print('skip'); continue
    
    img = cv2.imread(reports_path + filename)
    # show_img(img)
    print("Shape:", img.shape)
    reader = ReportReader(img)
    report = reader.read()
    print(report)
    df_data['number'].append(report['number'])
    df_data['date'].append(report['date'])
    df_data['time'].append(report['time'])
    df_data['new_cases'].append(report['new_cases'])
    df_data['new_deaths'].append(report['new_deaths'])
    df_data['recovered'].append(report['recovered'])
    df_data['active'].append(report['active'])
    df_data['deaths'].append(report['deaths'])
    df_data['suspicious'].append(report['suspicious'])
    df_data['accumulated'].append(report['accumulated'])
    df_data['discarted'].append(report['discarted'])
    df_data['beni'].append(report['beni'])
    df_data['chuquisaca'].append(report['chuquisaca'])
    df_data['cochabamba'].append(report['cochabamba'])
    df_data['la_paz'].append(report['la_paz'])
    df_data['pando'].append(report['pando'])
    df_data['santa_cruz'].append(report['santa_cruz'])
    df_data['tarija'].append(report['tarija'])

print(df_data)
df = pd.DataFrame(df_data)
df.to_csv('full.csv', index=False)

    # :::::: OCR ::::::
    
    # processed = process(img)
    # ocr_data = ocr.image_to_data(processed)
    # conf = r'--oem 3 --psm 6'
    # string = ocr.image_to_data(processed, config=conf)
    # print(ocr_data)

    ## :::::: THE PARSER ::::::

    # rows = OcrDataParser().parse(string)
    # print("ROWS: {}".format(len(rows)))
    # for row in rows[1:-1]:
    #     # print(row.text())
    #     top_left = (row.left(), row.top())
    #     # print(top_left)
    #     bottom_right  = (row.left() + row.width(), row.top() + row.height())
    #     # print(bottom_right)
    #     processed = cv2.rectangle(processed, top_left, bottom_right, (0, 0, 0), 2)
    # show_img(processed)

