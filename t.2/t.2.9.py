class ExamSubmission:
    def __init__(self, name, points):
        self.name = name
        self.points = points

def passed(submissions, limit):
    result = []
    for sub in submissions:
        if sub.points >= limit:
            result.append(sub)
    return result

e1 = ExamSubmission("Matti", 50)
e2 = ExamSubmission("Maija", 30)
e3 = ExamSubmission("Teppo", 70)

results = passed([e1, e2, e3], 40)
for r in results:
    print(r.name, r.points)

