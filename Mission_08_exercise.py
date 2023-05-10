pass_test = "This student passed the test!"
fail_test = "This student did not pass the test."


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def pass_test(self):
        if self.grade >= 75:
            return pass_test
        else:
            return fail_test


student1 = Student("Danny", 40)
student2 = Student("Patrick", 64)

print(str(student2.name) + " got a score of " + str(student2.grade) + " out of 100.")
print(student2.pass_test())

