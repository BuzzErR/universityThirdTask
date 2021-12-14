import unittest
import random
import functools
import main
import time

def generate_random_data():
    result = []
    n = random.randint(0, 10 ** 5)
    for i in range(n):
        result.append(random.uniform(-10 ** 6, 10 ** 6))
    return result


class TestMethods(unittest.TestCase):
    numbers = generate_random_data()

    def test_min(self):
        # print(self.numbers)
        try:
            self.assertEqual(min(self.numbers), main.find_min(self.numbers))
        except AssertionError as e:
            with open('bot_buffer.txt', 'a') as f:
                f.write(str(e) + ' test_min\n')
            raise Exception(e)

    def test_max(self):
        # print(self.numbers)
        try:
            self.assertEqual(max(self.numbers), main.find_max(self.numbers))
        except AssertionError as e:
            with open('bot_buffer.txt', 'a') as f:
                f.write(str(e) + ' test_max\n')
            raise Exception(e)
        
            

    def test_sum(self):
        # print(self.numbers)
        try:
            self.assertEqual(sum(self.numbers), main.sum_of_numbers(self.numbers))
        except AssertionError as e:
            with open('bot_buffer.txt', 'a') as f:
                f.write(str(e) + ' test_sum\n')
            raise Exception(e)
            

    def test_multiplication_no_overflow(self):
        # print(self.numbers)
        try:
            self.assertEqual(functools.reduce((lambda x, y: x * y), self.numbers),
                            main.multiplication_of_numbers(self.numbers))
        except AssertionError as e:
            with open('bot_buffer.txt', 'a') as f:
                f.write(str(e) + ' test_multiplication_no_overflow\n')
            raise Exception(e)

    def test_execution_speed_sum(self):
        start_time = time.time()
        _ = main.sum_of_numbers(self.numbers)
        end_time = time.time()
        first_exec_time = end_time - start_time

        new_numbers = self.numbers * 100
        start_time = time.time()
        _ = main.sum_of_numbers(self.numbers)
        end_time = time.time()
        second_exec_time = end_time - start_time
        statement = round(second_exec_time / first_exec_time) < 100
        try:
            self.assertTrue(statement)
        except AssertionError as e:
            with open('bot_buffer.txt', 'a') as f:
                f.write(str(e) + ' test_multiplication_no_overflow\n')
            raise Exception(e)

    def test_import_of_data(self):
        # возможно предусмотреть создание уникального файла, но в задании подобного не требуется
        with open('generator_for_tests.txt', 'w') as f:
            for item in self.numbers:
                f.write("%s " % item)
        try:
            self.assertEqual(self.numbers, main.get_numbers_from_file('generator_for_tests.txt'))
        except AssertionError as e:
            with open('bot_buffer.txt', 'a') as f:
                f.write(str(e) + ' test_import_of_data\n')
            raise Exception(e)