from formatter import TAG_EXPLANATIONS

class Cases():
    """ Класс определяет количество слов из запроса в тексте. """
    def __init__(self):
        """ Список неключевых слов."""
        self.stop_words = set()
        """ Построчный текст записан как список списков."""
        self.matrix = []
        """ Список ключевых слов - поисковый запрос."""
        self.query = []
        """ Количество строк текста."""
        self.number = 0
        """ Словарь для совпадений ключевых слов в тексте."""
        self.RELEVANCE = {}

    def load_from_file(self) -> None:
        """ Метод считывает из файла информацию. """
        try:
            file1 = open("input.txt","r")
            self.stop_words = set(file1.readline().split())
            self.number = int(file1.readline())
            for _ in range(self.number):
                self.matrix.append(file1.readline().strip().split())
            self.query = file1.readline().split()
            file1.close()
        except FileNotFoundError:
            print(TAG_EXPLANATIONS['no_file'])
        except UnicodeError:
            print(TAG_EXPLANATIONS['lang'])
        except ValueError:
            print(TAG_EXPLANATIONS['empty'])
        except IndexError:
            print(TAG_EXPLANATIONS['index'])
        finally:
            return

    def run_on_solution(self) -> None:
        """ Метод создает словарь слов (ключ) и списка пар. """
        for i in range(self.number):
            document_set = set()
            document_set = set(self.matrix[i])
            vector = [0,0]
            dict_key = ''
            for j in range(len(self.query)):
                if (self.query[j] in document_set
                    and self.query[j] not in self.stop_words):
                    vector[0] = i
                    vector[1] += 1
                    dict_key = self.query[j] + str(i)
                    self.RELEVANCE[dict_key] = vector
        return


    def output_result(self) -> list:
        """ Метод выводит отсортированный список пар. """
        output_set = set()
        for key in self.RELEVANCE:
            output_set.add(tuple(self.RELEVANCE[key]))
        sorted_result = list(output_set)
        sorted_result.sort()
        return sorted_result


if __name__ == '__main__':
    case = Cases()
    case.load_from_file()
    case.run_on_solution()
    result = case.output_result()
    for i in range(len(result)):
         print('{ document_id =', str(result[i][0])
         + ', relevance =', str(result[i][1]) + ' }')
