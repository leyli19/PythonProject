#Лейли Ылясова
# Лабораторная 1
# Вариант 6. Перечисление ориентированных генных последовательностей
# В задаче 4 впервые приведено понятие синтенных блоков – похожих
# участков геномов двух видов, перемещённых в результате перестроек. В той же
# задаче предлагается использовать перестановки для моделирования упорядоченных синтенных блоков в одной хромосоме.
# Однако каждая цепь молекулы ДНК имеет ориентацию (которая, например, определяет направление, вдоль которого происходит транскрипция РНК),
# поэтому для улучшенного моделирования хромосом при помощи синтенных
# блоков следует для каждого из блоков указать ориентацию, которая определяет,
# в которой из цепей находится этот блок. Добавление ориентации синтенных блоков потребует дополнительных обозначений для перестановок.
# Задача. Перестановка со знаком длины n – это упорядоченная последовательность положительных чисел {1, 2, 3, …, n}, в которой для каждого числа
# 10
# затем выбирается положительный либо отрицательный знак (положительный
# знак обычно опускается). Например, (5, –3, –2, 1, 4) – перестановка со знаком
# длины 5.
# Входные данные: натуральное число
# n < 6.
# Выходные данные: общее число перестановок со знаком длины n, а также
# список всех таких перестановок (в любом порядке).

# import itertools
#
#
# def generate_signed_permutations(n):
#     numbers = list(range(1, n + 1))
#     permutations = itertools.permutations(numbers)
#     result = []
#     for perm in permutations:
#         signs_combinations = itertools.product([1, -1], repeat=n)
#         for signs in signs_combinations:
#             signed_perm = [sign * num for sign, num in zip(signs, perm)]
#             result.append(signed_perm)
#
#     return len(result), result
#
#
# n = int(input("Введите число n (n <= 6): "))
# count, signed_permutations = generate_signed_permutations(n)
#
# print(f"Общее количество перестановок со знаком: {count}")
# for perm in signed_permutations:
#     print(perm)


# Лабораторная 2. Вариант 5.
# Задача. Пусть даны две строки s и t. Строка t является подстрокой строки
# s, если t содержится целиком как единая последовательность символов в строке
# s (отсюда следует, что t должна быть не длиннее s).
# Индексом символа в строке называется общее число символов слева от
# него, исключая его самого, например, индексы всех вхождений символа U в
# строке AUGCUUCAGAAAGGUCUUACG равны 1, 4, 5, 14, 16 и 17. В Python символ с индексом i в строке s обозначается s[i].
# Подстрока строки s обозначается через s[j:k]. j означает индекс первого
# элемента подстроки, k – индекс элемента, следующего за последним элементом
# подстроки в строке s. Другими словами, подстрока s[j:k] содержит элементы
# строки s от s[j] включительно до s[k] исключительно. Например, если
# s = “AUGCUUCAGAAAGG UCUUACG”, то s[2:5] = “GCU”.
# Позицией подстроки s[j:k] является начальный индекс j. Заметим, что у
# подстроки t может оказаться несколько позиций, если она входит несколько раз
# в строку s (как в примере ниже).
# Входные данные: Две строки ДНК s и t (каждая длины не более 1 килобазы).
# Выходные данные: Все позиции подстроки t в строке s.


# def find_substring_positions(dna_string, substring):
#     positions = []
#     substring_length = len(substring)
#
#     for i in range(len(dna_string) - substring_length + 1):
#         if dna_string[i:i + substring_length] == substring:
#             positions.append(i + 1)
#
#     return positions
#
#
# dna_string = input("Введите строку ДНК: ")
# substring = input("Введите подстроку: ")
#
# positions = find_substring_positions(dna_string, substring)
#
# print(" ".join(map(str, positions)))




#Лабораторная работа 3. Вариант 2.

# def plot_time_series(data, title):
#     plt.figure(figsize=(10, 5))
#     plt.plot(data.index, data.values)
#     plt.title(title)
#     plt.xlabel('Year')
#     plt.ylabel('Value')
#     plt.grid()
#     plt.show()
#
#
# co2_data = co2.load_pandas().data
# co2_data = co2_data.loc['1958':'1980']
# plot_time_series(co2_data['co2'], 'CO2 Levels (1958-1980)')
#
# copper_data = copper.load_pandas().data
# copper_data = copper_data.loc['1961':'1970']
# plot_time_series(copper_data[['WORLDCONSUMPTION', 'COPPERPRICE']], 'Copper Consumption and Price (1961-1970)')
#
# elnino_data = elnino.load_pandas().data
# elnino_data = elnino_data.loc['1990':'2010']
# plot_time_series(elnino_data['NINO3'], 'Elnino Index (1990-2010)')
#
# grunfeld_data = grunfeld.load_pandas().data
# for firm in grunfeld_data['firm'].unique():
#     firm_data = grunfeld_data[grunfeld_data['firm'] == firm]
#     plot_time_series(firm_data.set_index('year')['value'], f'Grunfeld Firm {firm} Data')
#
# longley_data = longley.load_pandas().data
# longley_data = longley_data.loc[1951:1955]
# for column in ['GNPDEFL', 'UNEMP', 'ARMED']:
#     plot_time_series(longley_data[column], f'Longley Data - {column} (1951-1955)')
#
# macrodata = macrodata.load_pandas().data
# macrodata = macrodata.loc[1990:2009]
# for column in ['realgdp', 'realcons', 'realgovt']:
#     plot_time_series(macrodata[column], f'Macrodata - {column} (1990-2009)')
#
# nile_data = nile.load_pandas().data
# nile_data = nile_data.loc[1890:1910]
# plot_time_series(nile_data['flow'], 'Nile River Flow (1890-1910)')
#
# stackloss_data = stackloss.load_pandas().data
# stackloss_subset = stackloss_data.iloc[4:15]
# plot_time_series(stackloss_subset['stack.loss'], 'Stackloss Data (Days 5 to 15)')
#
# sunspots_data = sunspots.load_pandas().data
# sunspots_data = sunspots_data.loc[1990:2008]
# plot_time_series(sunspots_data['sunspots'], 'Sunspots Data (1990-2008)')