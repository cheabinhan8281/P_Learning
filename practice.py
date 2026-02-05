class Student:
  def __init__(self, num, name, kor, eng, math):
    self.num = num
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math

  # Instance method to calculate total score for the student object
  def get_total(self):
    return self.kor + self.eng + self.math

  # Instance method to calculate average score for the student object
  def get_avg(self):
    return self.get_total() / 3

  def grade(self):
    avg = self.get_avg()
    match(avg//10):
      case 10|9: return 'A'
      case 8: return 'B'
      case 7: return 'C'
      case 6: return 'D'
      case _: return 'F'
      


def main():
  s1 = Student(1, '홍길동', 86, 90, 74)
  s2 = Student(2, '아이유', 95, 93, 97)
  s3 = Student(3, '이제훈', 88, 85, 90)
  students = [s1, s2, s3]
  for s in students:
    print(f'{s.name}, {s.get_total()},{s.get_avg():.2f},{s.grade()}')



if __name__ == "__main__":
  main()