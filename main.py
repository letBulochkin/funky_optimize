from math import sqrt
from inspect import getsource
from vector import Vektor

def evaluate(args):
	res = (args[0]**3)-(75*args[0])+(3*args[0]+args[1])**2
	#res = (args[0]**3)-18*(args[0]**2)-(39*args[0])+(3*args[0]+args[1])**2
	return res

'''
class Expression(object):
	"""docstring for Expression"""
	def __init__(self, *args):
		for i in args:
			self.arguments.append(i)

	def evaluate():
		res = self.arguments[0]**3-75*self.arguments[0]+
			(3*self.arguments[0]+self.arguments[1])**2 
'''

def hook_jeeves(start_p, delta, prec):

	print("Инициализирую метод Хука и Дживса.")

	prev_p = start_p
	curr_p = start_p

	while True:

		if (delta < prec):
			print("Приращение меньше требуемой точности.")
			break

		curr_res = evaluate(curr_p)
		print("Шаг 1. Значение F = {} в точке ({}, {})".format(curr_res, curr_p[0], curr_p[1]))

		print("Шаг 2. Исследующий поиск по первой координате.")

		buff_p = curr_p
		if (evaluate(Vektor(curr_p[0]+delta, curr_p[1])) < curr_res):  # исследующий поиск по х
			curr_p = Vektor(curr_p[0]+delta, curr_p[1])
			curr_res = evaluate(curr_p)
			print("Приращение первой координаты. Значение F = {} в точке ({}, {})".format(curr_res, curr_p[0], curr_p[1]))
		elif (evaluate(Vektor(curr_p[0]-delta, curr_p[1])) < curr_res):
			curr_p = Vektor(curr_p[0]-delta, curr_p[1])
			curr_res = evaluate(curr_p)
			print("Уменьшение первой координаты. Значение F = {} в точке ({}, {})".format(curr_res, curr_p[0], curr_p[1]))
		else:
			print("Исследующий поиск результатов не дал.")

		print("Шаг 3. Исследующий поиск по второй координате.")
		if (evaluate(Vektor(curr_p[0], curr_p[1]+delta)) < curr_res):  # исследующий поиск по у
			curr_p = Vektor(curr_p[0], curr_p[1]+delta)
			curr_res = evaluate(curr_p)
			print("Приращение второй координаты. Значение F = {} в точке ({}, {})".format(curr_res, curr_p[0], curr_p[1]))
		elif (evaluate(Vektor(curr_p[0], curr_p[1]-delta)) < curr_res):
			curr_p = Vektor(curr_p[0], curr_p[1]-delta)
			curr_res = evaluate(curr_p)
			print("Уменьшение второй координаты. Значение F = {} в точке ({}, {})".format(curr_res, curr_p[0], curr_p[1]))
		else:
			print("Исследующий поиск результатов не дал.")

		if (buff_p == curr_p):
			print("Изменение базисной точки результатов не дало.")
			print("Переход на следующую итерацию с уменьшением приращения.")
			delta /= 2
			continue

		print("Шаг 4. Поиск по образцу")
		while True:  # поиск по образцу
			next_p = Vektor(2*curr_p[0] - prev_p[0], 2*curr_p[1] - prev_p[1])
			print("Следующая опорная точка по направлению ({},{})".format(next_p[0], next_p[1]))
			if (evaluate(next_p) < curr_res):
				curr_res = evaluate(next_p)
				prev_p = curr_p
				curr_p = next_p
				print("Значение F = {} в точке ({}, {})".format(curr_res, curr_p[0], curr_p[1]))
				print("Улучшение функции. Продолжение поиска по образцу.")
			else:
				print("Ухудшение функции. Переход на новую итерацию.")
				break

		delta /= 2

	print("Поиск окончен.")
	print("Значение F = {} в точке ({}, {})".format(evaluate(curr_p), curr_p[0], curr_p[1]))

def nelder_mead(start_p, simplex_l, refl, shr, stch, iters):

	count = 0

	print("Инициализирую метод Нельдера-Мида.")
	print("Вычисление начального симплекса...")
	simplex = [[Vektor(start_p[0]-(simplex_l/2), start_p[1]-(simplex_l*0.29)), None],
				[Vektor(start_p[0]+(simplex_l/2), start_p[1]-(simplex_l*0.29)), None],
				[Vektor(start_p[0], start_p[1]+(simplex_l*0.58)),None]]
	for i in range(len(simplex)):
		simplex[i][1] = evaluate(simplex[i][0])

	print("Начальный симплекс:\n", [i[0] for i in simplex])
	#print("Значения в точках:\n", [i[1] for i in simplex])

	while True:
		#print("Начинаю итерацию ", count)
		print("Шаг 0. Вычисление значений функции в точках начального симплекса.")
		for i in range(len(simplex)):
			simplex[i][1] = evaluate(simplex[i][0])

		print("Начальный симплекс:\n", [i[0] for i in simplex])
		print("Значения в точках:\n", [i[1] for i in simplex])

		print("Шаг 1. Сортировка точек симплекса по значениям функции.")
		simplex.sort(key = lambda x: x[1])

		print("Начальный симплекс:\n", [i[0] for i in simplex])
		print("Значения в точках:\n", [i[1] for i in simplex])

		print("Шаг 2. Определение центра отражения симплекса.")
		mid = (simplex[0][0] + simplex[1][0]) / 2
		print(mid)

		print("Шаг 3. Отражение симплекса от худшей точки.")
		xr = mid + (mid - simplex[2][0])*refl
		print("Отраженная ", xr, "=> xr")

		print("Шаг 4. Анализ точек.")
		if (evaluate(xr) < evaluate(simplex[1][0])):
			simplex[2][0] = xr
			print("Точка xr лучше хорошей точки. Обновление точки w.")
		else:
			if (evaluate(xr) < evaluate(simplex[2][0])):
				simplex[2][0] = xr
				print("Точка xr лучше худшей точки. Обновление точки w.")
			c = (simplex[2][0] + mid)/2
			print("??????")
			if (evaluate(c) < evaluate(simplex[0][0])):
				simplex[2][0] = c
				print("?????? ??????")

		if (evaluate(xr) < evaluate(simplex[0][0])):
			xe = mid + (xr - mid)*stch
			print("Шаг 4.1. Растяжение симплекса.")
			print("Растяжение до ", xe, "=> xe")
			if (evaluate(xe) < evaluate(xr)):
				simplex[2][0] = xe
				print("Точка xe лучше точки xr. Обновление точки w.")
			else:
				simplex[2][0] = xr
				print("Точка xr лучше точки xe. Обновление точки w.")

		if (evaluate(xr) > evaluate(simplex[1][0])):
			xc = mid + (simplex[2][0]-mid)*shr
			print("Шаг 4.1. Сжатие симплекса.")
			print("Сжатие до ", xc, "=> xс")
			if (evaluate(xc) < evaluate(simplex[2][0])):
				simplex[2][0] = xc
				print("Точка xc лучше худшей точки. Обновление точки w.")

		count = count + 1
		if (count==iters):
			print("Условие окончания поиска выполнено. Окончание поиска.")
			print(simplex[0][0], " Значение функции F = ", evaluate(simplex[0][0]))
			break
		else:
			print("Условие окончания поиска не выполнено. Продолжаю поиск.")

def box_wilson(start_p, interval, prec):

	print("Инициализирую метод Бокса-Уилсона.")
	print("Шаг 0. Вычисление начальных значений...")

	point = start_p
	val = evaluate(point)

	print(point, " Значение функции: ", val)

	while True:

		print("Шаг 1. Вычисление матрицы плана эксперимента.")

		plan_matrix = [[Vektor(point[0]-1*interval, point[1]-1*interval), None],
						[Vektor(point[0]+1*interval, point[1]-1*interval), None],
						[Vektor(point[0]-1*interval, point[1]+1*interval), None],
						[Vektor(point[0]+1*interval, point[1]+1*interval), None]]

		for i in range(len(plan_matrix)):
			plan_matrix[i][1] = evaluate(plan_matrix[i][0])

		print("Матрица плана:")
		for i in plan_matrix:
			print(i[0], " Значение функции: ", i[1])

		print("Шаг 2. Вычисление коэффициентов уравнения регрессии.")
		b1 = (-plan_matrix[0][1]+plan_matrix[1][1]-plan_matrix[2][1]+plan_matrix[3][1])/4
		b2 = (-plan_matrix[0][1]-plan_matrix[1][1]+plan_matrix[2][1]+plan_matrix[3][1])/4

		print("Коэффициенты уравнения регрессии: b1 = {}, b2 = {}".format(b1, b2))

		print("Шаг 3. Вычисление величины шага.")
		hx1 = b1*0.01
		hx2 = b2*0.01

		print("Величина шага для координат: hx1 = {}, hx2 = {}".format(hx1, hx2))

		print("Шаг 4. Начинаем движение по поверхности отклика.")
		search_i = 0
		while True:
			temp_x = Vektor(point[0]-search_i*hx1, point[1]-search_i*hx2)
			print("Итерация поиска №{}".format(search_i))
			print(temp_x, "Значение функции:", evaluate(temp_x))
			if (evaluate(temp_x) > val):
				print("Значение функции в новой точке больше предыдущего. Прекращаю движение.")
				break
			elif (search_i > 10):
				print("Достигнуто ограничение количества итераций поиска. Принудительный переход.")
				break
			else:
				print("Значение функции в новой точке меньше предыдущего. Продолжаю движение.")
				point = temp_x
				val = evaluate(temp_x)
				search_i += 1

		if (sqrt(b1**2+b2**2) < prec):
			print("Условие прекращение поиска выполнено. Прекращаю поиск.")
			print(point, " Значение функции F = ", val)
			break
		else:
			print("Условие прекращение поиска не выполнено. Продолжаю поиск.")

def floatTryParse(line_to_print):
	value = input(line_to_print)
	try:
		return float(value)
	except ValueError:
		return floatTryParse(line_to_print)

def intTryParse(line_to_print):
	value = input(line_to_print)
	try:
		return int(value)
	except ValueError:
		return intTryParse(line_to_print)

if __name__ == '__main__':
	print("Демонстрация методов оптимизации.")
	print("Данная функция:")
	print(getsource(evaluate).split('\n')[1])

	while True:
		args = input("Введите координаты точки через пробел: ").split(' ')
		if 2 != len(args):
			print("Необходимо скорректировать данные.")
			continue
		else:
			for i in args:
				if not i.isdigit():
					print(i + " - должно быть числом")
					continue

		point = Vektor(*[int(i) for i in args])
		print(point)

		print("Каким методом оптимизировать?\n1. Хука и Дживса\n2. Нельдера-Мида\n3. Бокса-Уилсона")
		choice = intTryParse("Ответ: ")
		while choice not in [1, 2, 3]:
			print("Необходимо указать число в заданном диапазоне.")
			choice = intTryParse("Ответ: ")

		if choice == 1:
			d = floatTryParse("Укажите приращение координат: ")  # 2
			p = floatTryParse("Укажите точность: ") # 0.06
			hook_jeeves(point, d, p)
		elif choice == 2:
			l = floatTryParse("Укажите длину стороны симплекса: ")  # 2
			r = floatTryParse("Укажите коэффициент отражения: ")  # 1
			sh = floatTryParse("Укажите коэффициент сжатия: ")  # 0.5
			st = floatTryParse("Укажите коэффициент растяжения: ")  # 2
			p = floatTryParse("Укажите точность: ")
			nelder_mead(point, l, r, sh, st, 10)
		elif choice == 3:
			trv = floatTryParse("Укажите интервал приращения: ")  # 1
			p = floatTryParse("Укажите точность: ") # 0.06
			box_wilson(point, trv, p)

		again = intTryParse("Еще разок? 0/1: ")
		while again not in [0, 1]:
			again = intTryParse("Еще разок? 0/1: ")

		if again == 0:
			break
