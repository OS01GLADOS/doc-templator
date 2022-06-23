from inspect import ArgInfo
import sys
import json
import codecs
from docxtpl import DocxTemplate


def main(args):       
    try:
        path_to_template = args[1]
        path_to_data = args[2]
        new_files_name = args[3]
    except:
        print(''' 
        ОШИБКА.
        требует 3  параметра через пробел:
        1. имя шаблона (например document.doc)
        2. имя файла с данными в формате:
                    [
                        {
                            'заменяемый текст':'текст для замены'
                        },
                    ]
        3. постфикс новых файлов (например решение.doc)
        
        !!!! работает только с .doc .docx файлами !!!!

        попробуйте еще раз''')
        input('нажмите любую клавишу чтобы выйти')
        return 0
    print (f"opening file:\n{path_to_template}")
    opened_doc = DocxTemplate(path_to_template)
    data = {}
    with codecs.open (path_to_data, 'r', 'utf-8') as file:
        data = json.loads(file.read())
    index = 1
    for item in data:
        print(item)
        opened_doc.render(item)
        opened_doc.save(f"{index}_{new_files_name}")
        index +=1

        

if __name__ == '__main__':
    main(sys.argv)