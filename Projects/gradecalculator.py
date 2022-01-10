Ramesh = { "name":"Ramesh Thapa",
		"assignment" : [60, 70, 80, 20],
		"test" : [75, 75],
		"lab" : [77.30, 67.50]
	}
		
Anju = { "name":"Anju Khatri",
		"assignment" : [72, 66, 54, 60],
		"test" : [70, 70],
		"lab" : [77.80, 68.52]
		}
Kumar = { "name" : "Kumar Sanu",
		"assignment" : [67, 72, 43, 89],
		"test" : [88, 75],
		"lab" : [80, 70]
		}

Hari = { "name" : "Hari Ram",
		"assignment" : [77, 56, 87, 41],
		"test" : [60, 60],
		"lab" : [68, 54.76]
	}

Ram = { "name" : "Ram Sharan",
		"assignment" : [39, 79, 70, 66],
		"test" : [65, 46],
		"lab" : [60, 45.6]
	}
def get_average(marks):
	total_sum = sum(marks)
	total_sum = float(total_sum)
	return total_sum / len(marks)

def calculate_total_average(students):
	assignment = get_average(students["assignment"])
	test = get_average(students["test"])
	lab = get_average(students["lab"])

	return (0.1 * assignment +
			0.7 * test + 0.2 * lab)

def assign_letter_grade(score):
	if score >= 90: return "A"
	elif score >= 80: return "B"
	elif score >= 70: return "C"
	elif score >= 60: return "D"
	else : return "E"

def class_average_is(student_list):
	result_list = []

	for student in student_list:
		stud_avg = calculate_total_average(student)
		result_list.append(stud_avg)
		return get_average(result_list)

students = [Ramesh, Anju, Kumar, Hari, Ram]

for i in students :
	print(i["name"])
	print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
	print("Average marks of %s is : %s "(i["name"],
						calculate_total_average(i)))
						
	print("Letter Grade of %s is : %s" %(i["name"],
	assign_letter_grade(calculate_total_average(i))))
	
	print()

class_av = class_average_is(students)

print(f"Class Average is {class_av}")
print(f"Letter Grade of the class is {(assign_letter_grade(class_av))} ")