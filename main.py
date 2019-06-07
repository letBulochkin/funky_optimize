def eval(*args):
	res = (args[0]**3)-(75*args[0])+(3*args[0]+args[1])**2
	return res

'''
class Expression(object):
	"""docstring for Expression"""
	def __init__(self, *args):
		for i in args:
			self.arguments.append(i)

	def eval():
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

		curr_res = eval(*curr_p)
		print("Шаг 1. Значение F = {} в точке ({}, {})".format(curr_res, curr_p[0], curr_p[1]))

		print("Шаг 2. Исследующий поиск по первой координате.")
		
		buff_p = curr_p
		if (eval(curr_p[0]+delta, curr_p[1]) < curr_res):  # исследующий поиск по х
			curr_res = eval(curr_p[0]+delta, curr_p[1])
			curr_p = [curr_p[0]+delta, curr_p[1]]
			print("Приращение первой координаты. Значение F = {} в точке ({}, {})".format(curr_res, curr_p[0], curr_p[1]))
		elif (eval(curr_p[0]-delta, curr_p[1]) < curr_res):
			curr_res = eval(curr_p[0]-delta, curr_p[1])
			curr_p = [curr_p[0]-delta, curr_p[1]]
			print("Уменьшение первой координаты. Значение F = {} в точке ({}, {})".format(curr_res, curr_p[0], curr_p[1]))
		else:
			print("Исследующий поиск результатов не дал.")

		print("Шаг 3. Исследующий поиск по второй координате.")
		if (eval(curr_p[0], curr_p[1]+delta) < curr_res):  # исследующий поиск по у
			curr_res = eval(curr_p[0], curr_p[1]+delta)
			curr_p = [curr_p[0], curr_p[1]+delta]
			print("Приращение второй координаты. Значение F = {} в точке ({}, {})".format(curr_res, curr_p[0], curr_p[1]))
		elif (eval(curr_p[0], curr_p[1]-delta) < curr_res):
			curr_res = eval(curr_p[0], curr_p[1]-delta)
			curr_p = [curr_p[0], curr_p[1]-delta]
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
			next_p = []
			next_p.append(2*curr_p[0] - prev_p[0])
			next_p.append(2*curr_p[1] - prev_p[1])
			print("Следующая опорная точка по направлению ({},{})".format(next_p[0], next_p[1]))
			if (eval(*next_p) < curr_res):
				curr_res = eval(*next_p)
				prev_p = curr_p
				curr_p = next_p
				print("Значение F = {} в точке ({}, {})".format(curr_res, curr_p[0], curr_p[1]))
				print("Улучшение функции. Продолжение поиска по образцу.")
			else:
				print("Ухудшение функции. Переход на новую итерацию.")
				break

		delta /= 2

	print("Поиск окончен.")
	print("Значение F = {} в точке ({}, {})".format(eval(*curr_p), curr_p[0], curr_p[1]))

if __name__ == '__main__':
	hook_jeeves([20, 25], 2, 0.06)
