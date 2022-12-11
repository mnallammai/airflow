txt_file = "/Users/nallammai/airflow-docker/dags/day1.txt"
 total_score = 0
 with open(txt_file, 'r') as fp:
     contents = fp.read()
     contents = contents.split('\n')
     for p in contents:
         p = p.split(',')
         s1, e1, s2, e2 = int(p[0].split('-')[0]), int(p[0].split('-')[1]), int(p[1].split('-')[0]), int(p[1].split('-')[1])
         if s1 >= s2 and e1 <= e2:
             total_score += 1
         elif s2 >= s1 and e2 <= e1:
             total_score += 1
 print(total_score)