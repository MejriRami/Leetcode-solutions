/*# Write your MySQL query statement below
select student_id , student_name , subjet_name, count( *)
from  Students
cross join subjects 
left join  on Examintation where (studet_id =examnantion.student_id and subject nae = subjecyt name)
group by student_id 
group by subejt name ,
order by subject name*/
SELECT 
    s.student_id, 
    s.student_name, 
    subj.subject_name, 
    COUNT(e.subject_name) AS attended_exams
FROM Students s
CROSS JOIN Subjects subj
LEFT JOIN Examinations e 
    ON s.student_id = e.student_id 
    AND subj.subject_name = e.subject_name
GROUP BY 
    s.student_id, 
    s.student_name, 
    subj.subject_name
ORDER BY 
s.student_id ASC,
subj.subject_name;
