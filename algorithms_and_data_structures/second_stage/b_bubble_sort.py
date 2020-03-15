from algorithms_and_data_structures.second_stage.a_abstract_sort import AbstractSort


class BubbleSort(AbstractSort):
    def sort(self):
        self.sort3()

    def sort1(self):
        end = len(self.array) - 1
        while end > 0:
            begin = 1
            while begin <= end:
                if self.cmp(begin, begin - 1) < 0:
                    self.swap(begin, begin - 1)
                begin += 1
            end -= 1

    def sort2(self):
        end = len(self.array) - 1
        array_sorted = True
        while end > 0:
            begin = 1
            while begin <= end:
                if self.cmp(begin, begin - 1) < 0:
                    self.swap(begin, begin - 1)
                    array_sorted = False
                begin += 1
            if array_sorted:
                break
            end -= 1

    def sort3(self):
        end = len(self.array) - 1
        array_sorted = True
        while end > 0:
            begin = 1
            sorted_index = 1
            while begin <= end:
                if self.cmp(begin, begin - 1) < 0:
                    self.swap(begin, begin - 1)
                    array_sorted = False
                    sorted_index = begin
                begin += 1
            if array_sorted:
                break
            end = sorted_index - 1
