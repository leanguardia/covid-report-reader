from os import walk

import cv2
import pandas as pd
import pytesseract as ocr

from readers.parsers import OcrDataParser
from readers.report_reader import ReportReader
from img.processing import process, show_img#, grayscale, threshold 


df_data = {
  'number': [], 'date_time': [], 'new_cases': [], 'new_deaths': [], 'recovered': [],
  'active': [], 'deaths': [], 'suspicious': [], 'accumulated': [], 'discarted': [],
  'beni': [], 'chuquisaca': [], 'cochabamba': [], 'la_paz': [], 'pando': [], 'santa_cruz': [], 'tarija': []
}

def accumulate_report(report):
    df_data['number'].append(report['number'])
    df_data['date_time'].append(report['date_time'])
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
    return df_data

reports_path = 'img/reportes_salud_casos/'

_, _, filenames = next(walk(reports_path))
# filenames = ['299_.png']

failed_files = ['.DS_Store']

for filename in filenames:
    print("\n> Processing:", filename)
    if filename in failed_files: print('skip'); continue
    
    img = cv2.imread(reports_path + filename)
    # show_img(img)
    print("Shape:", img.shape)
    processed = process(img)
    reader = ReportReader(processed)
    try:
      report = reader.read()
      print(report)
      accumulate_report(report)
    except IndexError as e:
      print("Failed " + filename)

print(df_data)
df = pd.DataFrame(df_data)
df = df.sort_values(by="number")
df.to_csv('full_report.csv', index=False)

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

