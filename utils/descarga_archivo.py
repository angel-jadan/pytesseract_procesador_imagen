# libreria excel 
import xlsxwriter

# datetime
from datetime import datetime

def descarga_xlsx(data):
    workbook = xlsxwriter.Workbook('lista_estudiantes.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})

    # celdas de cabeceras 
    worksheet.write('A1', 'FECHA', bold)
    worksheet.write('B1', 'ESTUDIANTE', bold)
    worksheet.write('C1', 'CEDULA', bold)
    worksheet.write('D1', 'VALIDACION CEDULA', bold)
    worksheet.write('E1', 'ASISTENCIA', bold)

    row = 1
    # celdas de detalle
    for i in data:
        worksheet.write_string(row, 0, str(datetime.now().strftime("%b %d %Y "))), 
        worksheet.write_string(row, 1, i.get('estudiante', ''))
        worksheet.write_string(row, 2, i.get('cedula', ''))
        worksheet.write_string(row, 3, i.get('cedula_valida', ''))
        worksheet.write_string(row, 4, i.get('asistencia', ''))
        row +=1
    workbook.close()