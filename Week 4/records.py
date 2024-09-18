def average_grade(records):
    total_grade=sum(record[2] for record in records)
    return total_grade/len(records)
students=(('harsh',20,85),('abhi',22,90),('naman',20,95))
def main():
    avg_grade=average_grade(students)
    print("Average grade:", avg_grade)
main()