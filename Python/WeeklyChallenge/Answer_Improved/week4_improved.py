def solution(table, languages, preference):
    pref_dict = {language: score for language, score in zip(languages, preference)}

    max_score = 0
    answer = ''
    for job in table:
        job_total_score = sum([pref_dict.get(lang, 0) * (5 - i) for i, lang in enumerate(job.split(" ")[1:])])
        if job_total_score > max_score:
            max_score = job_total_score
            answer = job[:job.index(' ')]
        elif job_total_score == max_score:
            answer = sorted([answer, job[:job.index(' ')]])[0]

    return answer

def main():
    input1 = [["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]]
    input2 = [["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]]

    print(solution(input1[0], input1[1], input1[2]))
    print(solution(input2[0], input2[1], input2[2]))